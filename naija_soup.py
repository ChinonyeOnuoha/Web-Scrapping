from bs4 import BeautifulSoup
import requests


wiki_url = 'https://en.wikipedia.org/wiki/Nigeria'           
wiki_request =  requests.get(wiki_url)
wiki_html = wiki_request.content
# print(wiki_html)

wiki_soup = BeautifulSoup(wiki_html, features = 'html.parser')

access_side_bar = wiki_soup.find('table')
side_bar_soup = access_side_bar.find('tbody')
soupy_soup = side_bar_soup.find_all(['tr', 'th'])

for i in soupy_soup:
    text = i.get_text()
    if "Federal Republ" in text:
        print(i.find_all("div")[0].get_text())
    else:
        print(text)
  



'''#FIND COUNTRY
frn = access_side_bar.find('th')
frn_text = frn.text[:27]
print(f'Country : {frn_text}')

#FIND MOTTO
motto = access_side_bar.find_all('tr')
motto_index = motto[2]
motto_soup = motto_index.find('div')
motto_text = motto_soup.text
print(motto_text)

#FIND CAPITAL
capital = access_side_bar.find_all('tr')
capital_index = capital[5]
capital_soup = capital_index.find('th')
capital_soup2 = capital_index.find('td')
capital_text = capital_soup.text
capital_text2 = capital_soup2.text
print(f'{capital_text} : {capital_text2}')

#LARGEST CITY IN NIGERIA
city = access_side_bar.find_all('tr')
city_index = city[6]
city_soup = city_index.find('th')
city_soup_text = city_soup.text
city_soupy_soup = city_index.find('td')
city_soup_txt = city_soupy_soup.text
print(f'{city_soup_text} : {city_soup_txt}')


#OFFICIAL LANGUAGES
lang = access_side_bar.find_all('tr')
lang_index = lang[7]
lang_soup = lang_index.find('th')
lang_soup_text = lang_soup.text
lang_soupy = lang_index.find('td')
lang_soupy_txt = lang_soupy.text
print(f'{lang_soup_text} : {lang_soupy_txt}') 


#NATIONAL LANGUAGES
n_lang = access_side_bar.find_all('tr')
n_lang_index = n_lang[8]
n_lang_soup = n_lang_index.find('th')
n_lang_soup_text = n_lang_soup.text
n_lang_soupy = n_lang_index.find('td')
n_lang_soupy_txt = n_lang_soupy.text
print(f'{n_lang_soup_text} : {n_lang_soupy_txt}') 


#GOVERNMENT
govt = access_side_bar.find_all('tr')
govt_index = govt[11]
govt_soup = govt_index.find('th')
govt_soup_text = govt_soup.text
govt_soupy = govt_index.find('td')
govt_soupy_txt = govt_soupy.text
print(f'{govt_soup_text} : {govt_soupy_txt}') '''