from bs4 import BeautifulSoup
import pandas as pd
import requests
import string 

url = 'https://www.yuppiechef.com/chargers.htm'
page = requests.get(url)
urlSoup = BeautifulSoup(page.text, "html.parser")

brands = []
for b in urlSoup.find_all(class_='product-card__brand'):
    brands.append(b.get_text())

names = []
for n in urlSoup.find_all(class_='product-card__name'):
    names.append(n.get_text())

prices = []
for p in urlSoup.find_all(class_='card-price-list__item'):
    p = p.get_text()
    p = p.translate({ord(c): None for c in string.whitespace})
    if p.startswith("Was"):
        pass
    else:
        str1, str2 = p.split('R')
        str2 = str2.replace('"', '')
        prices.append(str2)
        
products = pd.DataFrame(
    {'Brand': brands,
     'Name': names,
     'Price': prices,
    })

products.to_csv('products.csv')
