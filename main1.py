from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.classcentral.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# browser.get(url)
# soup = BeautifulSoup(browser.page_source, 'html.parser')
# browser.close()

pattern = re.compile(r"^\>.*\<$")
soup_txt = soup.prettify()

res = pattern.findall(soup_txt)
print(len(res))

# print(type(soup.prettify()))
# print(soup)



# plain_text = 