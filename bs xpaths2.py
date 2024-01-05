from bs4 import BeautifulSoup

def replace_words_with_uppercase(html, word_list):
    soup = BeautifulSoup(html, 'html.parser')
    for word in word_list:
        for tag in soup.find_all(lambda tag: tag.name not in ['script', 'style'] and tag.string and word in tag.string and not any(word in value for _, value in tag.attrs.items())):
            new_text = tag.string.replace(word, word.upper())
            tag.string.replace_with(new_text)
    return str(soup)


html = "<html><body><p class='hello'>Hello world</p></body></html>"
word_list = ['hello', 'world']
new_html = replace_words_with_uppercase(html, word_list)
print(new_html)
