# import scrapy
# from translate import Translator

# translator= Translator(to_lang="Hindi")
# main_lis = []

import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ["https://www.classcentral.com/"]
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers={'User-Agent': self.user_agent})

    def parse(self, response):
        css_urls = response.css('link[rel="stylesheet"]::attr(href)').extract()
        js_urls = response.css('script::attr(src)').extract()

        for url in css_urls:
            yield scrapy.Request(url, callback=self.parse_css)

        for url in js_urls:
            yield scrapy.Request(url, callback=self.parse_js)

    def parse_css(self, response):
        print("parse css")
        # Process the downloaded CSS file here
        # For example, you could save it to a file on disk

    def parse_js(self, response):
        print("parse js")
        # Process the downloaded JS file here
        # For example, you could extract further information from it


# class MySpider(scrapy.Spider):
#     name = 'myspider'
#     start_urls = ["https://www.classcentral.com/"]
#     user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

#     def start_requests(self):
#         for url in self.start_urls:
#             yield scrapy.Request(url, headers={'User-Agent': self.user_agent})

#     def parse(self, response):
#         # Extract all the text
#         text = response.xpath('//*[not(self::script)][not(self::style)]/text()').extract()
        
#         # Print the text
#         for t in text:
#             if t.strip()==None or t.strip()=="":
#                 pass
#             else:
#                 # translation = translator.translate(t.strip())
#                 main_lis.append(t.strip())
#             # print(t.strip())


from scrapy.crawler import CrawlerProcess

# Create a new CrawlerProcess
process = CrawlerProcess()

# Start the spider
process.crawl(MySpider)
process.start()

# print(len(main_lis))
# print(main_lis)

# text_xpaths = [element.get('xpath') for element in main_lis[:20]]

# for xpath in text_xpaths:
#     print(xpath)