from bs4 import BeautifulSoup
import requests
import time

filename = "starkeyboard.csv"

f = open(filename, "w", encoding='utf-8')

headers = "Product_Title,Price,Shop_Name,URL,Image_Url,Product_Code,Category_Id\n"

f.write(headers)

def webscrapStartech():
    pages = [1,2,3,4,5,6,7,8]

    for page in pages:
        source_link = requests.get('https://www.startech.com.bd/accessories/keyboards?page={}'.format(page)).text

        soup = BeautifulSoup(source_link, 'lxml')


        body = soup.find('body')


        productInfo = body.find_all('div', class_='col-xs-12 col-md-4 product-layout grid')


        for product in productInfo:

            product_name = product.find('h4', class_='product-name')

            title = product_name.a.text.upper()

            product_price = product.find('div', class_='price space-between')

            tk = product_price.span.text.replace(",","").replace("৳","")

            product_link = product.find('h4', class_='product-name')

            link = product_link.a['href']

            image_url = product.find('div',class_ = 'img-holder')

            url = image_url.img['src']

            data =title + "," + tk + "," + "STARTECH" + ","+ link + "," + url + "," + "1" + "," + "1" + "\n"

            f.write(data)
        time.sleep(5)

webscrapStartech()
