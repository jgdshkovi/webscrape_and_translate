import scrapy
from bs4 import BeautifulSoup
import requests
from englisttohindi.englisttohindi import EngtoHindi


home_url = "https://www.classcentral.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(home_url, headers=headers)

main_soup = BeautifulSoup(response.text, 'html.parser')
link_list = []

def find_links(main_soup):
    with open('modified_main_soup.html', encoding='utf-8') as f:
        contents = f.read()
        temp_soup = BeautifulSoup(contents, 'html.parser')
        # print(contents)
        
        all_a_tags = temp_soup.find_all('a')
        print(len(all_a_tags))
        # for i in range(1, len(all_a_tags)):
        for i in range(370, 376):    
            # new_text = tag.string.replace(word, word.upper())
            # tag.string.replace_with(new_text)
            link = all_a_tags[i].get('href')
            if link:
                if(link[0]=='/'):
                    # link_list.append(home_url+link)
                    all_a_tags[i]['href'] = "file"+str(i)+".html"
                    translate_and_replace(home_url+link, i)
                else:
                    # link_list.append(link)
                    all_a_tags[i]['href'] = "file"+str(i)+".html"
                    translate_and_replace(link, i)
        with open("modified_main_soup.html", 'w', encoding="utf-8") as file:
            file.write(str(temp_soup))



def translate_and_replace(url, idx):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    for tag in soup.find_all(lambda tag: tag.name not in ['script', 'style'] and tag.string):

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
            if translated_word!="" and translated_word!=None:
                new_text = tag.string.replace(tag.string, translated_word)
                tag.string.replace_with(new_text)
    
    with open("file"+str(idx)+".html", 'w', encoding="utf-8") as file:
        file.write(str(soup))
    print("file: " + str(idx) + "  created")


new_html = find_links(main_soup)
print("Done")
# print(len(link_list))
# for lk in link_list:
#     print(lk, '\n')
# print(link_list, sep='\n')

# with open('modified_main1.html', 'w', encoding="utf-8") as file:
#     file.write(new_html)