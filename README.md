# APIs.json

## What is APIs.json? 
It is a machine readable JSON specification, that anyone can use to define their API operations. APIs.json does not describe your APIs like [OpenAPI Spec](https://github.com/OAI/OpenAPI-Specification) do, but it describes your surrounding API operations, with entries that can reference your OpenAPI, or any other format that you desire.

**APIs.json Is An Index For API Operations**  
APIs.json provides a machine readable approach that API providers can put work in describing their API operations, similar to how web site providers describe their websites using [sitemap.xml](https://www.xml-sitemaps.com/). 

**APIs.json Indexes Can Be Created By 3rd Parties**  
One important thing to add, is that these APIs.json files can also be crafted, and published by external parties. We regularly are creating APIs.json and then coordinate with providers to get published under their own domain, making it an authoritative APIs.json file.

**APIs.json Can Be Used To Describe API Collections**  
Beyond describing a single API, within a single domain, APIs.json can also be used to describe entire collections of APIs, providing a machine readable way to organize, and share valuable collections of API resources. Here are a few examples of projects that are producing APIs.json driven collections.

**APIs.json Can Be Used To Describe Collections of Collections**  
Then taking things up another rung up the chain, APIs.json can also provide a collection of collections, something I do with my own APIs. Each Github organization on my network has a master APIs.json, providing include links to all other APIs.json within the organization. 

**The First Open Source Tooling For APIs.json**  
Up until now, this post is all about APIs.json, where in reality the format is useless without their being any tooling built on top of the specification, bringing value to the table. This is why the 3Scale team got to work building an open source APIs.json driven search engine:

*   [APIs.io](http://apis.io/) as an open source API search engine using APis.json.

**APIs.json Driving Other Open Tooling**  
APIs.io is just the beginning. It won't be enough to convince all API providers that they should be producing APIs.json index of their site operations, just for the API discovery boost. We are going to need APIs.json driven tooling that will service every other stop along the life cycle, including:

*  *   *HTTP Client / Hub / Workbenches**
*  *   *Documentation**
*  *   *Testing**
*  *   *Monitoring**
*  *   *Virtualization**
*  *   *Visualization**

**APIs.json Integrated Into Existing Platforms**  
What areas would you like to see served? Personally, I would like to have the ability to load / unload my APIs.json collections into any service that I use. Allowing me to organize my internal, public, and 3rd party APIs I depend within any platform out there that is servicing the API space.

**APIs.json Linking To The Human Aspects Of API Operations**  
APIs.json is just the scaffolding to hang links to essential aspects of your operations, it doesn't care what you link to. You can start by referencing essential links for your API operations like:

*  *   *Signup** - How to signup for a service.
*  *   *Support** - Where to get support. 
*  *   *Terms of Service** - Where are the terms of service.
*  *   *Pricing** - Where to find the pricing for a service.

**APIs.json Linking to Machine Readable Aspects of API Operations**  
These do not have to be machine readable links, they can reference important things the humans will need first. However, ultimately the goal is to make as much of the APIs.json index as machine readable as possible, using a variety of existing API definition formats, available for a variety of purposes.

*   [OpenAPI Spec](https://github.com/OAI/OpenAPI-Specification), for API description.
*   [API Common](http://apicommons.org/), for API licensing.
*   [AsyncAPI](https://asyncapi.com), for event-driven APIs.
*   [JSOn SChema](https://json-schema.org), for defining schema.
*   [Postman](https://www.getpostman.com/docs/collections), for run-time.

**Defining New, Machine Readable Property Elements For APIs.json**  
While the APIs.json spec will evolve, something I talk about below, its real strength lies in its ability to incentivize the development of entirely new, machine readable API definitions, bringing even more value to the API discovery process. Here are a few of the additional specs being crafted independent of, but inspired by APIs.json:

*   [API Plans](http://apievangelist.com/2016/02/13/my-tooling-and-api-for-gathering-and-organizing-the-details-of-the-plans-and-pricing-for-apis/), for pricing, plans & rate limits.
*   API Monitoring, for monitoring & testing.
*   API Changelog, for operational monitoring.
*   API SDK, for SDK reference.
*   API Conversations - for the stream around API operations

I doubt we will see many new additions like commons and country. In the future most of the structural changes to APis.json will be derived from first class property elements (ie. adding documentation or Github), making this the proving ground for defining what are truly the most important aspects of API operations, and what should be machine readable vs human readable.

**The Hard Work That Lies Ahead for APIs.json**  

*   Getting more API providers to <span style="text-decoration: underline;">describe their API operations</span> using APIs.json, and publish in the root of the domain for their API ecosystem.
*   Encourage more API evangelists, brokers & analysts using to <span style="text-decoration: underline;">describe their collections</span>, using APIs.json, building more meaningful indexes and directories of high value APIs.
*   Encourage platforms to <span style="text-decoration: underline;">build APIs.json into their operations</span>, as a storage and organization schema, but also as import / export format.
*   Incentivize the development of more <span style="text-decoration: underline;">meaningful tooling that employs APIs.json</span>, and uses it to better serve the API life cycle.
*   Continue to <span style="text-decoration: underline;">add new API property elements</span>, making sure as many of them as possible evolve to be machine readable, as well as first class citizens in the APIs.json specification.

**Other LInks**
* [APIs.json Website](http://apisjson.org/)
* [APIs.json Github Repo](https://github.com/apis-json/api-json) 
* [APis.io via the website](http://apis.io/)
* [Submit Issues](https://github.com/apis-json/api-json/issues/new). 
* 
**Next Steps**
* Stories, stories, and more stories.
* Next 0.17 release
  *   Overlay
  *   Unique Identifier