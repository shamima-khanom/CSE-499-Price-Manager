from bs4 import BeautifulSoup
import requests
import time


filename = "bsmouse.csv"

f = open(filename, 'w', encoding='utf-8-sig')

headers = "Product_Title,Price,Shop_Name,URL,Image_Url,Product_Code,Category_Id\n"

f.write(headers)


def webscrapBdstall():
    pages = [1,2]

    
    for page in pages:
        source_link = requests.get('https://www.bdstall.com/mouse/{}'.format(page)).text

        
        soup = BeautifulSoup(source_link, 'lxml')

        

        body = soup.find('body')

        

        product_thumb = body.find_all('div', class_='row product-cat-box s-top')

        

        for product in product_thumb:

            product_name = product.find(
                'div', class_='six columns product-cat-box-text')

            title = product_name.a.text.upper()

            product_price = product.find('div', class_='product-price')

            tk = product_price.text.replace(",","").replace("৳","")

            product_link = product.find('div',class_='six columns product-cat-box-text')
            
            link = product_link.a['href']

            image_url = product.find('div', class_='seven columns')

            url = image_url.img['src']

            data =title + "," + tk + "," + "BDSTALL" + ","+ link + "," + url + "," + "1" + "," + "1" + "\n"

            f.write(data)

        time.sleep(5)

webscrapBdstall()
