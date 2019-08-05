# Scrapy_Architecture_2

### Scrapy Selector

* Example HTML

```
<html>
 <head>
  <base href='http://example.com/' />
  <title>Example website</title>
 </head>
 <body>
  <div id='images'>
   <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' /></a>
   <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' /></a>
   <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' /></a>
   <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' /></a>
   <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' /></a>
  </div>
 </body>
</html>
```


##### XPath Selector

* Working with relative XPaths

* Keep in mind that if you are nesting selectors and use an XPath that starts with /, that XPath will be absolute to the document and not relative to the Selector you’re calling it from.
```
For example, suppose you want to extract all <p> elements inside <div> elements.
First, you would get all <div> elements:

>>> divs = response.xpath('//div')
At first, you may be tempted to use the following approach,
which is wrong, as it actually extracts all <p> elements from the document, not only those inside <div> elements:

>>> for p in divs.xpath('//p'):  # this is wrong - gets all <p> from the whole document
...     print(p.get())
This is the proper way to do it (note the dot prefixing the .//p XPath):

>>> for p in divs.xpath('.//p'):  # extracts all <p> inside
...     print(p.get())
Another common case would be to extract all direct <p> children:

>>> for p in divs.xpath('p'):
...     print(p.get())
For more details about relative XPaths see the Location Paths section in the XPath specification.
```

##### CSS Selector
* Per W3C standards, CSS selectors do not support selecting text nodes or attribute values.
* But selecting these is so essential in a web scraping context that Scrapy (parsel) implements a couple of non-standard pseudo-elements:

```
to select text nodes, use ::text
to select attribute values, use ::attr(name) where name is the name of the attribute that you want the value of
```

```
Examples:

title::text selects children text nodes of a descendant <title> element:

>>> response.css('title::text').get()
'Example website'

*::text selects all descendant text nodes of the current selector context:

>>> response.css('#images *::text').getall()
['\n   ',
 'Name: My image 1 ',
 '\n   ',
 'Name: My image 2 ',
 '\n   ',
 'Name: My image 3 ',
 '\n   ',
 'Name: My image 4 ',
 '\n   ',
 'Name: My image 5 ',
 '\n  ']
foo::text returns no results if foo element exists, but contains no text (i.e. text is empty):

>>> response.css('img::text').getall()
[]
This means .css('foo::text').get() could return None even if an element exists. Use default='' if you always want a string:

>>> response.css('img::text').get()
>>> response.css('img::text').get(default='')
''
a::attr(href) selects the href attribute value of descendant links:

>>> response.css('a::attr(href)').getall()
['image1.html',
 'image2.html',
 'image3.html',
 'image4.html',
 'image5.html']
```

<img width=600 src="https://user-images.githubusercontent.com/44635266/62413307-d17c5e00-b648-11e9-9805-688f25029f84.png">

```
Scrapy_src/Section8-2/test.py

import scrapy

class TestSpider(scrapy.Spider):

    name = 'test'
    allowed_domains = ['w3schools.com/']
    start_urls = ['https://www.w3schools.com/']

    def parse(self, response):
        # response.css('nav#mySidenav > div a::text').getall()
        # response.css('nav#mySidenav').xpath('./div//a/text()').extract()

        for n, text in enumerate(response.css('nav#mySidenav > div a::text').getall(), 1):
            yield {'num': n, 'learn Title': text}

```