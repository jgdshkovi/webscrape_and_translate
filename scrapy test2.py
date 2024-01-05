import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
from translate import Translator

def get_xpath(element):
    """
    Recursive function to generate XPath expressions for each element
    """
    xpath = Selector(element=element).xpath('descendant-or-self::text()').extract()
    if not xpath:
        return None
    xpath = '/'.join(xpath)
    if element.getparent() is not None:
        parent_xpath = get_xpath(element.getparent())
        if parent_xpath is None:
            return None
        xpath = parent_xpath + '/' + xpath
    return xpath

class MySpider(scrapy.Spider):
    name = 'example.com'
    start_urls = ["https://www.classcentral.com/"]
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers={'User-Agent': self.user_agent})

    def parse(self, response):
        # Generate all XPath expressions for readable text elements
        xpaths = []
        for element in response.xpath('//*[not(self::script)]'):
            xpath = get_xpath(element.root)
            if xpath is not None:
                xpaths.append(xpath)

        # Return the list of XPath expressions as the result of the spider
        return xpaths

# Create a Scrapy crawler
crawler = CrawlerProcess()

# Start the crawler with the MySpider spider
results = crawler.crawl(MySpider)

# Extract the XPath expressions from the results
xpaths = results.pop().result

# Print the list of XPath expressions
print(xpaths)
