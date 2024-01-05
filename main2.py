import scrapy
from bs4 import BeautifulSoup
import requests
from englisttohindi.englisttohindi import EngtoHindi
# from translate import Translator


# from lis2 import lis2=
# translator= Translator(to_lang="Hindi")

main_lis = []

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
#                 main_lis.append(t.strip())
#             # print(t.strip())

# from scrapy.crawler import CrawlerProcess

# # Create a new CrawlerProcess
# process = CrawlerProcess()

# # Start the spider
# process.crawl(MySpider)
# process.start()

# print(len(main_lis))
# # print(main_lis)

# '''----------------------------------------------------------------'''
# '''----------------------------------------------------------------'''




# translator= Translator(to_lang="Hindi")

# Sample list of texts
text_list = main_lis

url = "https://www.classcentral.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

def translate_and_replace(soup):
    for tag in soup.find_all(lambda tag: tag.name not in ['script', 'style'] and tag.string):
        # new_text = tag.string.replace(word, word.upper())
        # tag.string.replace_with(new_text)
        x = tag.string.strip().replace('(','').replace(')','').replace('“', '').replace('”', '').replace('’', '').replace('&','and')
        if x!=None and x!="":
            # word_list.append(x)
            translated_word = tag.string
            try:
                translated_word = EngtoHindi(x).convert
                # translated_word = translator.translate(word)
            except:
                pass
            # print(translated_word, "--------------------------------")
            new_text = tag.string.replace(tag.string, translated_word)
            tag.string.replace_with(new_text)
    return str(soup)

# def translate_and_replace(soup, word_list):
#     # soup = BeautifulSoup(html, 'html.parser')
#     for tag in soup.find_all(lambda tag: tag.name not in ['script', 'style'] and tag.string):
#         x = tag.string.strip().replace('(','').replace(')','').replace('“', '').replace('”', '').replace('’', '').replace('&','and')
#         if x!=None and x!="":
#             word_list.append(x)
#     for i in range(len(word_list)):
#         temp = soup.find_all(lambda tag: tag.name not in ['script', 'style'] and tag.string and word_list[i] in tag.string and not any(word_list[i] in value for _, value in tag.attrs.items()))
#         for tag in temp:
#             # print(tag)
#             # print('--------------------------------')
#             # break
#             # print( word_list[i] )
#             print(i)
#             word = word_list[i].replace('(','').replace(')','').replace('“', '').replace('”', '').replace('’', '').replace('&','and')
#             print(word_list[i], i, word)
#             translated_word = word
#             try:
#                 translated_word = EngtoHindi(word).convert
#                 # translated_word = translator.translate(word)
#             except:
#                 pass
#             print(translated_word, "--------------------------------")
#             new_text = tag.string.replace(word_list[i], translated_word)
#             tag.string.replace_with(new_text)
#     return str(soup)

# word_list = text_list
# individual_words = []
# for w in word_list:
#     for x in w.split():
#         if x not in individual_words:
#             individual_words.append(x)
# print(len(individual_words),'individual words')
# The individual words translation doesn't work as well, so we are good with translation of whole sentences

new_html = translate_and_replace(soup)
print("Done")

with open('modified_main1.html', 'w', encoding="utf-8") as file:
    file.write(new_html)