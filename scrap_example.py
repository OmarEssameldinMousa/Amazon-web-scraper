from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_title(new_soup):
    product_title = new_soup.find('span', attrs={'class': 'a-size-large product-title-word-break'})
    return product_title.text.strip() if product_title else 'N/A'

def get_price(new_soup):
    price = new_soup.find('span', attrs={'class': 'a-price-whole'})
    return price.text.strip() if price else 'N/A'

def get_rating(new_soup):
    rating = new_soup.find('span', attrs={'class': 'a-icon-alt'})
    return rating.text.strip() if rating else 'N/A'

# Defining connections to Amazon
URL = 'https://www.amazon.com/s?k=ps+4&crid=1N5Z2N0QD3LC3&sprefix=ps+%2Caps%2C363&ref=nb_sb_noss_2'

HEADER = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Content-Type': 'text/plain;charset=UTF-8'
}

webpage = requests.get(URL, headers=HEADER)
soup = BeautifulSoup(webpage.text, 'html.parser')

links = soup.findAll('a', attrs={'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})

amazon_products = {'title': [], 'price': [], 'rating': []}

for link in links:
    href = link.get('href')
    full_url = href if href.startswith('http') else 'https://www.amazon.com' + href
    new_soup = BeautifulSoup(requests.get(full_url, headers=HEADER).text, 'html.parser')
    amazon_products['title'].append(get_title(new_soup))
    amazon_products['price'].append(get_price(new_soup))
    amazon_products['rating'].append(get_rating(new_soup))

df = pd.DataFrame(amazon_products)

df.to_csv('amazon_data.csv')
