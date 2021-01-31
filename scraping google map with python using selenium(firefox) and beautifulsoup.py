#Import neccesary libraries

import pandas as pd
import time
from selenium import webdriver
from bs4 import BeautifulSoup

#intiate the firefox webdriver instance

driver=webdriver.Firefox()

#enter the filename

print("Enter the filename")
filename=str(input())

#https://www.google.com/search?tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!1m4!1u16!2m2!16m1!1e1!1m4!1u16!2m2!16m1!1e2!2m1!1e2!2m1!1e16!2m1!1e3!3sIAE,lf:1,lf_ui:2&tbm=lcl&sxsrf=ALeKk01oHwnkPHJqSfYYG6kHUVA_2cW1Ng:1612103736231&q=marketing%20agency%20in%20usa&rflfq=1&num=10&sa=X&ved=2ahUKEwibw6e0ssbuAhXBmuYKHUSNBvEQjGp6BAgCEFY&biw=1920&bih=937&rlst=f#rlfi=hd:;si:;mv:[[29.325622905405524,123.63917898523557],[9.55843841313825,82.33058523523559],null,[19.74699878271197,102.98488211023557],5]

print("Enter the link of google map to scrap")
url=str(input())
driver.get(url)
time.sleep(3)
record=[]
for i in range(8):
    try:
        page=driver.find_element_by_link_text(str(i+2))
        driver.set_page_load_timeout(30)
        driver.implicitly_wait(50)
        page.click()
        time.sleep(3)
        r=driver.page_source
#Beautiful soup for scraping the html source
        soup=BeautifulSoup(r,'html.parser')
        list= soup.find_all('div',{"class":"cXedhc"})
        for l in list:
            name=l.find('div').text
            detail=l.find_all('span')
            details=detail[0].text.replace('0','/0')
            record.append((name,details))
        df=pd.DataFrame(record,columns=['name','details'])
        df.to_csv(filename,index=False,encoding='utf-8')        
   
          

        
    except:
        driver.implicitly_wait(50)
        print("error at")
    
          

