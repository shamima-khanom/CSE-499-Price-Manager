from bs4 import BeautifulSoup
import requests
import time


filename = "dkeyboard.csv"

f = open(filename, 'w', encoding='utf-8-sig')

headers = "Product_Title,Price,Shop_Name,URL,Image_Url,Product_Code,Category_Id\n"

f.write(headers)



def webscrapDolphin():
    source_link = requests.get('https://dolphin.computer/products?category=keyboard').text

    
    soup = BeautifulSoup(source_link, 'lxml')

    

    body = soup.find('body')

    

    product_thumb = body.find_all('a', class_='product-card')

    

    for product in product_thumb:

        product_name = product.find('span', class_='product-name')

        title = product_name.text.upper()

        product_price = product.find('span', class_='product-price')

        tk = product_price.text.replace(",", "").replace("Tk", "")

        link = product['href']
        
        image_url = product.find('div',class_='image-holder')

        url = image_url.img['src']

        data =title + "," + tk + "," + "DOLPHIN" + ","+ link + "," + url + "," + "1" + "," + "2" + "\n"

        f.write(data)

    time.sleep(5)

webscrapDolphin()
