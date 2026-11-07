#!/usr/bin/env python3
"""
Validate the APIs.json specification against itself, and report how it fares on real files.

  1. Every spec/schema_*.yml that declares JSON Schema 2020-12 is itself a valid schema.
  2. The JSON and YAML examples in section 4 of the newest apisjson_<v>.txt validate
     against schema_<v>.yml.
  3. Every name in the newest reserved-words listing is accepted by that schema's type
     pattern. 0.23 had to repair a listing 117 types behind the schema; this keeps it from
     drifting again.
  4. (--report) Fetch the live indexes on the apisjson.org showcase, validate them, and
     print the pass rate with the most common errors. Report only: real publishers are
     not the specification's to fail.

Exits non-zero only on 1-3. See issue #132.
"""
import glob
import json
import os
import re
import sys
import urllib.request

import jsonschema
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPEC = os.path.join(ROOT, "spec")
SHOWCASE = "https://raw.githubusercontent.com/apis-json/apis-json-website/master/_data/showcase.yaml"


def version_key(path):
    return [int(x) for x in re.findall(r"\d+", os.path.basename(path))]


def summary(line):
    print(line)
    out = os.environ.get("GITHUB_STEP_SUMMARY")
    if out:
        with open(out, "a") as f:
            f.write(line + "\n")


def examples(text):
    """The JSON example (balanced braces) and the YAML example that follows it, from section 4."""
    sec = text[text.index("4.\tExamples"):text.index("5. Security Considerations")]
    start = sec.index("{")
    depth = 0
    for i, ch in enumerate(sec[start:], start):
        depth += ch == "{"
        depth -= ch == "}"
        if depth == 0:
            break
    as_json = json.loads(sec[start:i + 1])
    rest = sec[i + 1:]
    y = rest[rest.index("aid:") - 6:] if "aid:" in rest else ""
    lines = [l for l in y.splitlines() if l.strip()]
    indent = min(len(l) - len(l.lstrip()) for l in lines) if lines else 0
    as_yaml = yaml.safe_load("\n".join(l[indent:] for l in y.splitlines())) if lines else None
    return as_json, as_yaml


def reserved_names(text):
    sec = text[text.index("----RESERVED WORDS"):]
    props = sec[sec.index("Properties Elements:"):]
    marker = "Synonyms (accepted alternate spellings"
    head, syn = (props.split(marker, 1) + [""])[:2]
    # Property types only: the Contact and Maintainer element lists are not types.
    if "Contact Elements:" in head:
        before, after = head.split("Contact Elements:", 1)
        head = before + (after[after.index(" Registered in"):] if " Registered in" in after else "")
    bullet = r"^ \* ([A-Za-z0-9][A-Za-z0-9 .\-]*?)\s*(?:\[NEW in [0-9.]+\])?\s*$"
    names = set(re.findall(bullet, head, re.M))
    syn = syn.split(":", 1)[1] if ":" in syn else syn
    syn = re.sub(r"\([^)]*\)", "", syn)
    syn = re.sub(r"and, new in [0-9.]+:", ",", syn)
    syn = re.sub(r"\s+", " ", syn)
    names |= {s.strip(" .") for s in re.split(r"[,;]", syn) if s.strip(" .")}
    return names


def main():
    failures = []
    schemas = sorted(glob.glob(os.path.join(SPEC, "schema_*.yml")), key=version_key)
    for path in schemas:
        s = yaml.safe_load(open(path))
        if "2020-12" in str(s.get("$schema", "")):
            try:
                jsonschema.Draft202012Validator.check_schema(s)
            except jsonschema.SchemaError as e:
                failures.append(f"{os.path.basename(path)} is not a valid 2020-12 schema: {e.message}")

    latest = schemas[-1]
    v = re.search(r"schema_([0-9.]+)\.yml", latest).group(1)
    text = open(os.path.join(SPEC, f"apisjson_{v}.txt")).read()
    schema = yaml.safe_load(open(latest))
    validator = jsonschema.Draft202012Validator(schema)
    summary(f"## APIs.json {v}\n")

    as_json, as_yaml = examples(text)
    for label, doc in (("JSON example", as_json), ("YAML example", as_yaml)):
        if doc is None:
            failures.append(f"{label} not found in section 4")
            continue
        errs = list(validator.iter_errors(doc))
        summary(f"- {label}: {'valid' if not errs else f'{len(errs)} errors'}")
        failures += [f"{label}: {e.message[:160]} at /{'/'.join(map(str, e.path))}" for e in errs]

    pattern = re.compile(schema["$defs"]["urls"]["properties"]["type"]["pattern"])
    listed = reserved_names(text)
    unknown = sorted(n for n in listed if not pattern.fullmatch(n))
    summary(f"- Reserved words listed: {len(listed)}; rejected by the schema: {len(unknown)}")
    failures += [f"reserved word '{n}' is listed in the text but rejected by the schema" for n in unknown]

    if "--report" in sys.argv:
        report(validator)

    if failures:
        summary("\n### Failures\n")
        for f in failures:
            summary(f"- {f}")
        sys.exit(1)
    summary("\nSpecification checks passed.")


def report(validator):
    try:
        req = urllib.request.Request(SHOWCASE, headers={"User-Agent": "apis-json-ci"})
        entries = yaml.safe_load(urllib.request.urlopen(req, timeout=30).read())
    except Exception as e:
        summary(f"\nShowcase report skipped: {e}")
        return
    live = [e for e in entries if e.get("status") == "live"]
    ok = fetched = 0
    errors = {}
    for e in live:
        try:
            req = urllib.request.Request(e["url"], headers={"User-Agent": "apis-json-ci"})
            body = urllib.request.urlopen(req, timeout=15).read().decode("utf-8", "replace")
            try:
                doc = json.loads(body)
            except ValueError:
                doc = yaml.safe_load(body)
        except Exception:
            continue
        if not isinstance(doc, dict):
            continue
        fetched += 1
        errs = list(validator.iter_errors(json.loads(json.dumps(doc, default=str))))
        ok += not errs
        for err in errs:
            key = f"{err.validator} at {'/'.join(str(p) for p in err.absolute_schema_path)[-70:]}"
            errors[key] = errors.get(key, 0) + 1
    summary(f"\n### Live showcase indexes (report only)\n\n- {ok} of {fetched} validate")
    for key, n in sorted(errors.items(), key=lambda kv: -kv[1])[:10]:
        summary(f"- {n} x {key}")


if __name__ == "__main__":
    main()
