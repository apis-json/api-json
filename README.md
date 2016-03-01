APIs.json
========

As part of our renewed focus on the [API discovery definition format APIs.json](https://s3.amazonaws.com/kinlane-productions/bw-icons/bw-api-discovery.png), I wanted to revisit the propsed machine readable API discovery specification, and see what is going on. First, what is APIs.json? It is a machine readable JSON specification, that anyone can use to define their API operations. APIs.json does not describe your APIs like [OpenAPI Spec](https://github.com/OAI/OpenAPI-Specification) and [API Blueprint](https://apiblueprint.org/) do, it describes your surrounding API operations, with entries that can reference your Open API Spec, API Blueprint, or any other format that you desire.

**APIs.json Is An Index For API Operations**  
APIs.json provides a machine readable approach that API providers can put work in describing their API operations, similar to how web site providers describe their websites using [sitemap.xml](https://www.xml-sitemaps.com/). Here are the APIs, who are describing their APIs using APIs.json:

 *[**APIStrat Austin API**](http://austin2015.apistrat.com/apis.json)
 *[**API Evangelist**](http://developer.apievangelist.com/apis.json)
 *[**Acuity Scheduling**](https://acuityscheduling.com/apis.json)
 *[**BreezoMeter**](http://breezometer.com/static/apis.json)
 *[**CheckMarket**](https://api.checkmarket.com/3/apis.json)
 *[**Clarify**](http://clarify.io/apis.json)
 *[**Data Validation**](https://developer.datavalidation.com/apis.json)
 *[**DNS Check**](https://www.dnscheck.co/apis.json)
 *[**Email Hunter**](https://emailhunter.co/apis.json)
 *[**FeedbackHub**](https://feedbackhub.co.uk/api/apis.json)
 *[**Fitbit**](https://www.fitbit.com/apis.json)
 *[**Gavagai**](http://gavagai.se/apis.json)
 *[**Kin Lane**](http://developer.kinlane.com/apis.json)
 *[**Link Creation Studio**](https://www.linkcreationstudio.com/developer/apis.json)
 *[**OneMusicAPI**](http://www.onemusicapi.com/apis.json)
 *[**Pandorabots API**](https://s3.amazonaws.com/enterprise-multitenant.3scale.net.3scale.net/pandorabots/2014/11/24/apis-35a2e2943bc0ef78.json?AWSAccessKeyId=AKIAIRYLTWBQ37ZNGBZA&Expires=1455947523&Signature=0RKNkK%2BnlCbkILpfwno6wh2neZo%3D)
 *[**Qalendra**](https://qalendra.com/apis.json)
 *[**RiteTag**](https://ritetag.com/assets/apis.json)
 *[**Singlewire**](https://www.singlewire.com/apis.json)
 *[**SiteCapt**](https://sitecapt.com/apis.json)
 *[**Social Searcher API**](http://www.social-searcher.com/apis.json)
 *[**Super Monitoring**](http://www.supermonitoring.com/apis.json)
 *[**Timekit**](http://api.timekit.io/apis.json)
 *[**Trade.gov**](http://developer.trade.gov/apis.json)
 *[**Twitch Bot Directory**](https://twitchbots.info/apis.json)
 *[**EnClout**](http://enclout.com/api/apis.json)
 *[**frAPI**](http://api.meerkat.com.br/frapi/docs/apis.json)
 *[**Section.io**](https://aperture.section.io/apis.json)
 *[**Spoonacular**](https://spoonacular.com/apis.json)

**APIs.json Indexes Can Be Created By 3rd Parties**  
One important thing to add, is that these APIs.json files can also be crafted, and published by external parties. An example of this is with the Trade.gov APIs. [I originally created that APIs.json file](http://developer.trade.gov.apievangelist.com/apis.json), and coordinated with them to eventually it get published under their own domain, making it an authoritative APIs.json file. Many APIs.json files will be born outside of the API operations they describe, something you can see in my API stack project:

*   [The API Stack](http://theapistack.com/companies.html) - Provides almost 1000 APIs.json files, that describe the API operations of many leading public API platforms. There is also around 300 OpenAPI specifications, for some of the platforms described

**APIs.json Can Be Used To Describe API Collections**  
Beyond describing a single API, within a single domain, APIs.json can also be used to describe entire collections of APIs, providing a machine readable way to organize, and share valuable collections of API resources. Here are a few examples of projects that are producing APIs.json driven collections.

*   [Defining APIs that you depend on for organizational operation.](http://stack.apievangelist.com/apis.json)
*   [Defining a specific category of API operations, using the format.](http://monitoring.apievangelist.com/apis.json)
*   SMS - [http://sms.stack.network/](http://sms.stack.network/)
*   MMS - [http://mms.stack.network/](http://mms.stack.network/)
*   Email - [http://email.stack.network/](http://email.stack.network/)
*   News - [http://news.stack.network/](http://news.stack.network/)

**APIs.json Can Be Used To Describe Collections of Collections**  
Then taking things up another rung up the chain, APIs.json can also provide a collection of collections, something I do with my own APIs. Each Github organization on my network has a master APIs.json, providing include links to all other APIs.json within the organization. In this scenario I have over 30 other APIs.json indexed, which can all operate independently of each other, but can also be considered a collection of API collections.

*   [Master](https://kin-lane.github.io/master/apis.json) - A master collection of API collections I maintain as part of the API Evangelist network operations.

**The First Open Source Tooling For APIs.json**  
Up until now, this post is all about APIs.json, where in reality the format is useless without their being any tooling built on top of the specification, bringing value to the table. This is why the 3Scale team got to work building an open source APIs.json driven search engine:

*   [APIs.io](http://apis.io/) as an open source tool dedicated to APIs.json
*   [APIs.io](http://apis.io/) as a public API search engine, with APIs.json as index.
*   [APIs.io](http://apis.io/) as a private API search engine, with APIs.json as index.

**APIs.json Driving Other Open Tooling**  
APIs.io is just the beginning. It won't be enough to convince all API providers that they should be producing APIs.json index of their site operations, just for the API discovery boost. We are going to need APIs.json driven tooling that will service every other stop along the life cycle, including:

*   **HTTP Client / Hub / Workbenches**
*   **Documentation**
*   **Testing**
*   **Monitoring**
*   **Virtualization**
*   **Visualization**

**APIs.json Integrated Into Existing Platforms**  
What areas would you like to see served? Personally, I would like to have the ability to load / unload my APIs.json collections into any service that I use. Allowing me to organize my internal, public, and 3rd party APIs I depend within any platform out there that is servicing the API space. Here are a handful of those types of integrations that are already happening:

*   **[WarewolfESB](http://warewolf.io/ESB-blog/swagger-apisjson-support/)** - ESB integration and API discovery.
*   **[SwaggerHub](http://swagger.io/integrating-with-the-swaggerhub-api/)** - Public and private API hub discovery.
*   **API Management** - In Progress w/ [3Scale](http://3scale.net)...
*   **API Monitoring** - In Progress with [API Science](http://apiscience.com)...
*   **API Change Log** -  In Progress with [API ChangeLog](http://apichangelog.com)...
*   **[SmartBear](https://smartbear.com/plugins/apis-io-import-export/) -** API discovery for monitoring, testing, virtualization, and security.
*   **[API Evangelist](http://developer.apievangelist.com/)** - API analyst operations.
*   **[Kin Lane](http://developer.kinlane.com/)** - API factory operations (not organic)
*   **[Adopta.Agency](http://adopta.agency)** - Government open data publishing.

**APIs.json Linking To The Human Aspects Of API Operations**  
APIs.json is just the scaffolding to hang links to essential aspects of your operations, it doesn't care what you link to. You can start by referencing essential links for your API operations like:

*   **Signup** - How to signup for a service.
*   **Support** - Where to get support. 
*   **Terms of Service** - Where are the terms of service.
*   **Pricing** - Where to find the pricing for a service.

**APIs.json Linking to Machine Readable Aspects of API Operations**  
These do not have to be machine readable links, they can reference important things the humans will need first. However, ultimately the goal is to make as much of the APIs.json index as machine readable as possible, using a variety of existing API definition formats, available for a variety of purposes.

*   [OpenApI Spec](https://github.com/OAI/OpenAPI-Specification), for API description.
*   [API Blueprint](https://apiblueprint.org/), for API description.
*   [API Common](http://apicommons.org/), for API licensing.
*   [Postman](https://www.getpostman.com/docs/collections), for run-time.

**Defining New, Machine Readable Property Elements For APIs.json**  
While the APIs.json spec will evolve, something I talk about below, its real strength lies in its ability to incentivize the development of entirely new, machine readable API definitions, bringing even more value to the API discovery process. Here are a few of the additional specs being crafted independent of, but inspired by APIs.json:

*   [API Plans](http://apievangelist.com/2016/02/13/my-tooling-and-api-for-gathering-and-organizing-the-details-of-the-plans-and-pricing-for-apis/), for pricing, plans & rate limits.
*   API Monitoring, for monitoring & testing.
*   API Changelog, for operational monitoring.
*   API SDK, for SDK reference.
*   API Conversations - for the stream around API operations

**Roadmap for Version 0.16 of APIs.json**  
That is the 100K view of what is APIs.json now, and the short term plan for the future. Most of the change within the universe APIs.json is mapping will occur add the individual API, and within the machine readable specs that describe them like OpenAPI Spec, API Blueprint, and Postman. Secondarily, there will be additional, machine readable, API types being defined and added into the spec.

Even with this reality, we do have a handful of changes planned for the 0.16 version of APIs.json:

*   **commons** - Establish a top level collection of common property elements that apply to ALL APIs being referenced in an APIs.json
*   **country** - Adding a top level country reference using [ISO 3166](http://www.iso.org/iso/country_codes).
*   New Proper Elements - Suggesting a handful of new property elements to reference common API operation building blocks
    *   Registration
    *   Blog
    *   Github
    *   Twitter

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

