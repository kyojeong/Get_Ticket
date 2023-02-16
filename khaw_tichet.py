# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 12:49:42 2023

@author: user
"""

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from PIL import Image
import ddddocr


options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}
options.add_experimental_option('prefs', prefs) 
options.add_argument("disable-infobars") 

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window() 

#輸入帳密
driver.get("https://kham.com.tw/application/UTK13/UTK1306_.aspx") # 到登入頁面

driver.find_element("name", "ctl00$ContentPlaceHolder1$ACCOUNT").send_keys('E225148115') #輸入帳號
driver.find_element("name", "ctl00$ContentPlaceHolder1$M_PASSWORD").send_keys('chichi88') #輸入密碼

#驗證碼輸入
driver.save_screenshot('pictures.png') 
element = driver.find_element(By.XPATH,'//*[@id="chk_pic"]')
left = element.location['x']
right = element.location['x'] + element.size['width']
top = element.location['y']
bottom = element.location['y'] + element.size['height']
img = Image.open('pictures.png')
big = 1.25
img = img.crop((left*big, top*big, right*big, bottom*big))
#img = img.convert("RGB")

ocr = ddddocr.DdddOcr()
res = ocr.classification(img)
res = res.upper()

print(res)
driver.find_element("name", "ctl00$ContentPlaceHolder1$CHK").send_keys(res) #輸入密碼

driver.find_element('name',"ctl00$ContentPlaceHolder1$LOGIN_BTN").click()


driver.get("https://kham.com.tw/application/UTK02/UTK0201_.aspx?PRODUCT_ID=P02GVWP1")
#driver.get("https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=8820259&mdiv=shopCart")
#driver.find_element('name',"ctl00$ContentPlaceHolder1$BUY_BTN").click()

while 1:
    try:
        driver.find_element('name',"ctl00$ContentPlaceHolder1$BUY_BTN").click()
        break # 後面結帳部分就不寫囉

    except:
        driver.refresh() # 重整頁面


#buy = WebDriverWait(driver, 1, 0.5).until(EC.presence_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_DataGrid_ctl02_ACTION'))) # 顯性等待
#buy.click() # 偵測到可以購買按鈕就點擊按鈕
while 1:
    try:
        driver.find_element(By.XPATH,"//*[contains(text(),'立即訂購')][2]").click()
        break
    except:
        driver.refresh() # 重整頁面
        
driver.find_element(By.XPATH,"//*[contains(text(),'VIP區')]").click()

driver.find_element('name',"ctl00$ContentPlaceHolder1$DataGrid$ctl02$AMOUNT").send_keys("2")

#驗證碼輸入
driver.save_screenshot('pictures.png') 
element = driver.find_element(By.XPATH,'//*[@id="chk_pic"]')
left = element.location['x']
right = element.location['x'] + element.size['width']
top = element.location['y']
bottom = element.location['y'] + element.size['height']
img = Image.open('pictures.png')
big = 1.25
img = img.crop((left*big, top*big, right*big, bottom*big))


ocr = ddddocr.DdddOcr()
res = ocr.classification(img)
res = res.upper()

print(res)
driver.find_element('name',"ctl00$ContentPlaceHolder1$CHK").send_keys(res)

driver.find_element('name',"ctl00$ContentPlaceHolder1$AddShopingCart").click()
time.sleep(100)