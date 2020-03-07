from bs4 import BeautifulSoup
import requests
import time


filename = "dmonitor.csv"

f = open(filename, 'w', encoding='utf-8-sig')

headers = "Product_Title,Price,Shop_Name,URL,Image_Url,Product_Code,Category_Id\n"

f.write(headers)



def webscrapDolphin():

    pages = [1,2,3]
    for page in pages:
        source_link = requests.get('https://dolphin.computer/products?category=monitor&sort=latest&page={}'.format(page)).text

        
        soup = BeautifulSoup(source_link, 'lxml')

        

        body = soup.find('body')

        

        product_thumb = body.find_all('a', class_='product-card')

        

        for product in product_thumb:

            product_name = product.find('span', class_='product-name')

            title = product_name.text.upper().replace(",", "")

            product_price = product.find('span', class_='product-price')

            tk = product_price.text.replace(",", "").replace("Tk", "").replace(".00 34000.00", "").replace(".00 6500.00", "")

            link = product['href']
            
            image_url = product.find('div',class_='image-holder')

            url = image_url.img['src']

            data =title + "," + tk + "," + "DOLPHIN" + ","+ link + "," + url + "," + "1" + "," + "1" + "\n"

            f.write(data)

        time.sleep(5)

webscrapDolphin()
