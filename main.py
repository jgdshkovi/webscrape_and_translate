from bs4 import BeautifulSoup
import requests
from englisttohindi.englisttohindi import EngtoHindi

url = "https://www.classcentral.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

def translate_and_replace(soup):
    for tag in soup.find_all(lambda tag: tag.name not in ['script', 'style'] and tag.string):
        x = tag.string.strip().replace('(','').replace(')','').replace('“', '').replace('”', '').replace('’', '').replace('&','and')
        if x!=None and x!="":
            translated_word = tag.string
            try:
                translated_word = EngtoHindi(x).convert
            except:
                pass
            new_text = tag.string.replace(tag.string, translated_word)
            tag.string.replace_with(new_text)
    return str(soup)

new_html = translate_and_replace(soup)
print("Done")

with open('modified_main1.html', 'w', encoding="utf-8") as file:
    file.write(new_html)