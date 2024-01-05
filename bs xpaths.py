from bs4 import BeautifulSoup
import requests
from lis2 import lis2
# from translate import Translator
from englisttohindi.englisttohindi import EngtoHindi

# translator= Translator(to_lang="Hindi")

# Sample list of texts
text_list = lis2

url = "https://www.classcentral.com/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
# # Send a request to the website and get the HTML content
# res = requests.get(url)
# html = res.text

# Parse the HTML using BeautifulSoup
# soup = BeautifulSoup(html, 'html.parser')

# Find all text elements
# text_elements = soup.find_all(text=True)

def replace_words_with_uppercase(soup, word_list):
    # soup = BeautifulSoup(html, 'html.parser')
    for i in range(460, len(word_list)):
        temp = soup.find(lambda tag: tag.name not in ['script', 'style'] and tag.string and word_list[i] in tag.string and not any(word_list[i] in value for _, value in tag.attrs.items()))
        if temp:
            for tag in temp:
                # print(tag)
                # print('--------------------------------')
                # break
                # print( word_list[i] )
                word = word_list[i].replace('(','').replace(')','')
                print(word_list[i], i, word)
                translated_word = word
                try:
                    translated_word = EngtoHindi(word).convert
                    # translated_word = translator.translate(word)
                except:
                    pass
                
                print(translated_word, "--------------------------------")
                new_text = tag.string.replace(word_list[i], translated_word)
                tag.string.replace_with(new_text)
    return str(soup)

# html = "<html><body><p class='hello'>Hello world</p></body></html>" 217
word_list = text_list
new_html = replace_words_with_uppercase(soup, word_list)
print("Done")

with open('modified.html', 'w', encoding="utf-8") as file:
    file.write(new_html)