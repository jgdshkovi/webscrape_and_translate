# import re

# text = '''
# <html>
#     <head>
#     xyz inside head
#     </head>
#     <body>
#     abss before parag
#     <p>This is a para</p>
#     after para
#     </body>
# </html>
# '''
# # text_nxtline_strip = text.strip('\n').strip('\t').strip()
# text_nxtline_strip = "".join(text.splitlines())

# # print(text)
# # print("------")
# # print(text_nxtline_strip)
# pattern = re.compile(r"><")
# res = pattern.finditer(text_nxtline_strip)
# for r in res:
#     print(r)
# # print(res)

# from googletrans import Translator
# import translators as ts

# from translate import Translator
# translator= Translator(to_lang="Hindi")
# translation = translator.translate("(HCI)")
# print(translation)

# importing the module
# from englisttohindi.englisttohindi import EngtoHindi

# # message to be translated
# message = "Yes, I am geeks"

# # creating a EngtoHindi() object
# res = EngtoHindi(message)

# # displaying the translation
# print(res.convert)


# translator = Translator()
# result = translator.translate('Mikä on nimesi', src='fi')
# # translated_text = translator.translate(text, dest='hi')
# print(result)

# phrase = 'Mikä on nimesi'
# ts.google(phrase, from_language='fi', to_language='en')

import re
from bs4 import BeautifulSoup
import requests

url = "https://www.classcentral.com/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
word_list = []
from bs4 import BeautifulSoup

def replace_words_with_uppercase(soup):
    for tag in soup.find_all(lambda tag: tag.name not in ['script', 'style'] and tag.string):
        # new_text = tag.string.replace(word, word.upper())
        # tag.string.replace_with(new_text)
        x = tag.string.strip().replace('(','').replace(')','').replace('“', '').replace('”', '').replace('’', '').replace('&','and')
        if x!=None and x!="":
            word_list.append(x)

# def replace_words_with_uppercase(soup):
#     # soup = BeautifulSoup(html, 'html.parser')
#     for tag in soup.find_all(string=re.compile('.+')):
#         word_list.append(tag)
    

# Example usage
# html = "<html><body><p class='hello'>Hello world</p></body></html>"
# word_list = ['hello', 'world']
new_html = replace_words_with_uppercase(soup)

# Print modified HTML to console
print(word_list)
print(len(word_list))




