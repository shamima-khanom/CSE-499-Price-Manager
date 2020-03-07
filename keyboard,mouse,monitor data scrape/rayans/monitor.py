from bs4 import BeautifulSoup
import requests
import time

filename = "rmonitor.csv"

f = open(filename, "w", encoding='utf-8-sig')

headers = "Product_Title,Price,Shop_Name,URL,Image_Url,Product_Code,Category_Id\n"

f.write(headers)

def webscrapRyans():

    pages = [1,2,3,4,5,6,7]
    for page in pages:
        source_link = requests.get(
            'https://ryanscomputers.com/grid/all-monitor-all-brand?page={}'.format(page)).text

        soup = BeautifulSoup(source_link, 'lxml')


        body = soup.find('body')


        product_info = body.find_all('div', class_='product-box')


        for product in product_info:

            product_name = product.find('div', class_='product-content-info')

            title = product_name.a.text.replace(",","").upper()

            product_price = product.find('span', class_='price')

            tk = product_price.text.replace("Tk","").replace(",","").replace("BDT","").strip()

            product_link = product.find('div', class_='product-content-info')

            link = product_link.a['href']

            image_url = product.find('div', class_='product-thumb')
            url = image_url.img['src'].replace(",","")

            data =title + "," + tk + "," + "RYANS" + ","+ link + "," + url + "," + "1" + "," + "1" + "\n"

            f.write(data)
        time.sleep(5)

webscrapRyans()
