from bs4 import BeautifulSoup
import requests
import time

filename = "techland Keyboard.csv"

f = open(filename, 'w', encoding='utf-8')

headers = "Product_Title,Price\n"

f.write(headers)
source_link = requests.get(
    'https://www.techlandbd.com/accessories/computer-keyboard?sort=pd.name&order=ASC&limit=189').text
soup = BeautifulSoup(source_link, 'lxml')

body = soup.find('body')


caption = soup.find_all('div', class_='caption')

for product in caption:

    product_name = product.find('div', class_='name')

    title = product_name.a.text.strip()

    product_price = product.find('span', class_='price-normal')
    if(product_price):
        tk = product_price.text
    else:
        tk = '0000'
    

    data = (title + "," + tk +"\n")

    f.write(data)

    time.sleep(0.5)
