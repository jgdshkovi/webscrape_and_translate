from bs4 import BeautifulSoup
import requests

# Make a request to the webpage
# url = 'https://www.example.com'
url = "https://www.google.com"
# response = requests.get(url)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all links to CSS and JS files
links = soup.find_all('link') + soup.find_all('script')

for l in links:
    if '.js' in l.get('href') or '.js' in l.get('href'):
        print(l)
# print(links)
# Extract the href or src attribute from each link
file_links = [link.get('href') or link.get('src') for link in links]

# Filter out links that don't end in .css or .js
file_links = []
for link in file_links:
    if link!="" and link!=None:
        if link.endswith('.css') or link.endswith('.js'):
            file_links.append(link)
# file_links = [link for link in file_links if link.endswith('.css') or link.endswith('.js')]

print(len(file_links))
# Download the files using requests library
# for link in file_links:
#     file_content = requests.get(link).content
#     # Save the content to a file
#     with open(link.split('/')[-1], 'wb') as f:
#         f.write(file_content)
