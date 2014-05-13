api.json
========

This is a proposed specification for an api.json file, which can be placed in the root of any domain, providing a single inventory of all API resources available within that domain, as well as pointers to other associated api.json files.

* name
* description
* image
* url
  * apis (collection)
  * name
  * description
  * image
  * humanURL
  * machineURL
  * tags
  * urls (collection)
    * type
    * url
contact (collection)
type
url
meta (collection)
key
value
include (collection)
name
url
maintainer (collection)
type
url
tags
modified
