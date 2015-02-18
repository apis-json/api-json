api.json
========

This is a proposed specification for an api.json file, which can be placed in the root of any domain, providing a single inventory of all API resources available within that domain, as well as pointers to other associated api.json files.

* name
* description
* image
* tags
* url
* specificationVersion
* type
* apis (collection)
  * name
  * description
  * image
  * humanURL
  * machineURL
  * tags
  * properties (collection)
    * type
    * url
  * contact (collection)
    * email
    * x-twitter
  * meta (collection)
    * key
    * value
* include (collection)
    * name
    * url
* maintainer (collection)
  * name
  * email
  * twitter
* modified

This is a fast evolving spec, make your contributions via the issue management page. 

Here is the api.json for the API Commons:

```
{
  "name": "API Commons",
  "description": "An API for adding and pulling APIs that are in the commons.",
  "image": "https://s3.amazonaws.com/kinlane-productions/api-commons/api-commons-icon.png",
  "tags": [
      "application programming interface",
      "API",
      "News",
      "Analysis"
  ],
  "url": "https://api-commons.3scale.net/docs",
  "specificationVersion":"0.14",
  "type": "default",
  "apis": [
    {
      "name": "API Commons",
      "description": "An API for adding and pulling APIs that are in the commons.",
      "image": "https://s3.amazonaws.com/kinlane-productions/api-commons/api-commons-icon.png",
      "humanURL": "https://api-commons.3scale.net/docs",
      "machineURL": "http://api.apicommons.org/swagger-spec.json",
      "tags": "API, Application Programming Interface, Copyright",
      "properties": [
        {
          "type": "signup",
          "url": "https://api-commons.3scale.net/signup"
        },
        {
          "type": "swagger",
          "url": "http://api.apicommons.org/swagger-spec.json"
        }
      ],
      "contact": [
        {
          "email": "apicommons@gmail.com"
          "x-twitter": "apicommons"
        }
      ],
      "meta": [
        {
          "key": "interface-license",
          "value": "CC BY 3.0"
        },
        {
          "type": "pricing",
          "url": "Free"
        }
      ]
    }
  ],
  "include": [],
  "maintainer": [
    {
	"name": "Kin",
	"twitter": "apievangelist",
	"email": "kin@email.com"
    }
  ],
  "modified": "02/18/2015"
}
```
