import re
import requests
from bs4 import BeautifulSoup
import math

url = 'https://www.kabum.com.br/gamer'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
soup = BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')

qtd_items = soup.find('div', id='listingCount').get_text().strip()
index = qtd_items.find(' ')
qtd = qtd_items[:index]
print(qtd)

last_page = math.ceil(int(qtd) / 20)
print(last_page)

dic_products = {'brand': [], 'price': [], 'images': []}

for i in range(1, last_page + 1):
    url_pag = f'https://www.kabum.com.br/gamer?page_number={i}&page_size=20&facet_filters=&sort=most_searched'
    soup = BeautifulSoup(requests.get(url_pag, headers=headers).content, 'html.parser')
    products = soup.find_all('div', class_=re.compile('productCard'))
  
    for product in products:
        brand = product.find('span', class_=re.compile('nameCard')).get_text().strip()
        price = product.find('span', class_=re.compile('priceCard')).get_text().strip()
        images = product.find('img', class_=re.compile('imageCard'))['src']

        print(brand, price, images)
