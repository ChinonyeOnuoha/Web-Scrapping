from bs4 import BeautifulSoup
import requests

# html_file = open('index.html', 'r')
# html_data = html_file.read()

# soup = BeautifulSoup(html_data, features = 'html.parser')
# print(soup)

# filter = soup.find('p')
# print(filter.text)

jumia_url = 'https://www.jumia.com.ng/smartphones/'
jumia_request = requests.get(jumia_url)

jumia_html = jumia_request.content

# print(jumia_html)

jumia_soup = BeautifulSoup(jumia_html, features = 'html.parser')

h3_filter = jumia_soup.find_all('h3')

for product in h3_filter:
    print(product.text)