from bs4 import BeautifulSoup
import requests
import time


filename = "cvkeyboard.csv"

f = open(filename,"w",encoding='utf-8-sig')

headers = "Product_Title,Price,Shop_Name,URL,Image_Url,Product_Code,Category_Id\n"

f.write(headers)

def webscrapCvillage():

    pages = [1,2,3,4,5,6,7]

    
    for page in pages:
        source_link = requests.get('https://www.village-bd.com/keyboard/{}'.format(page)).text

        soup = BeautifulSoup(source_link,'lxml')


        

        body = soup.find('body')

        

        productInfo = soup.find_all('li',class_='col-sm-3')


        

        for product in productInfo:


            product_name = product.find ('div',class_='pro-name')

            title = product_name.a.text.upper()

            product_price = product.find('div',class_='price')

            tk = product_price.text.replace(",","").replace("৳","")

            product_link = product.find('div', class_='pro-name')

            link = product_link.a['href']

            image_url = product.find('div', class_='img-box')

            url = image_url.img['src']
            
            data =title + "," + tk + "," + "COMPUTER VILLAGE" + ","+ link + "," + url + "," + "1" + "," + "1" + "\n"

            f.write(data)

        time.sleep(5)

webscrapCvillage()






