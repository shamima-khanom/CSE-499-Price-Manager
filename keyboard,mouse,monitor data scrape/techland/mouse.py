from bs4 import BeautifulSoup
import requests
import time

filename = "tmouse.csv"

f = open(filename, 'w', encoding='utf-8')

headers = "Product_Title,Price,Shop_Name,URL,Image_Url,Product_Code,Category_Id\n"

f.write(headers)

def webscrapTechlandk():

    pages = [1,2,3,4,5,6,7,8,9,10,11,12]
    for page in pages:

        source_link = requests.get(
            'https://www.techlandbd.com/accessories/shop-computer-mouse?page={}'.format(page)).text
        soup = BeautifulSoup(source_link, 'lxml')


        body = soup.find('body')

        product_thumb = soup.find_all('div', class_='product-thumb')


        for product in product_thumb:

            product_name = product.find('div', class_='name')

            title = product_name.a.text.replace(",","").upper()

            product_price = product.find('span', class_='price-normal')
            if(product_price):
                tk = product_price.text.replace("Tk","").replace(",","").replace("৳ ","").strip()
            else:
                tk = '0000'

            product_link = product.find('div',class_='name')

            link = product_link.a['href']

            image_url = product.find('a',class_='product-img')

            url = image_url.img['src'].replace(",","")

            data = (title + "," + tk.replace("৳","").replace(",","") + "," + "TECHLAND" + ","+ link +"," + url + "," + "1" + ","+ "1"+"\n")

            f.write(data)

        time.sleep(5)

webscrapTechlandk()
