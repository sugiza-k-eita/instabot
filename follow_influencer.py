#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
import random

username = ""
pw = ""
#インスタグラムのuser名とpassを代入

keywords = ["","",""]
#フォローしたい人の名前をリストに入れる

driver= webdriver.Chrome(executable_path = '')
#executable_pathには、pythonで使う用のWebdriverの位置を代入
driver.implicitly_wait(3)
url_login = "https://www.instagram.com/?hl=ja"
driver.get(url_login)
time.sleep(3)
print("ログインしました")

element = driver.find_element_by_name("username")
element.clear()
element.send_keys(username)
element = driver.find_element_by_name("password")
element.clear()
element.send_keys(pw)
print("フォームを送信")

browser_from = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div')
time.sleep(2)
browser_from.click()
print("情報を入力してログインしました")

not_now = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
not_now.click()
time.sleep(5)
print("not_now")
time.sleep(5)
not_now2 = driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm")
not_now2.click()
print("not_now2")
time.sleep(3)


for i in keywords:
    try:
        time.sleep(3)
        serchbox = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
        serchbox.clear()
        time.sleep(3)
        serchbox.send_keys(i)
        time.sleep(3)
        serchbox.send_keys(Keys.ENTER)
        time.sleep(3)
        serchbox.send_keys(Keys.ENTER)
        time.sleep(8)
        followclick = driver.find_element_by_css_selector("#react-root > section > main > div > header > section > div.nZSzR > div.Igw0E.IwRSH.eGOV_.ybXk5._4EzTm > div > div > div > span > span.vBF20._1OSdk > button")
        followclick.click()
        print(i+"さんをフォローしました")
        time.sleep(2)
        home = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[1]")
        home.click()
        time.sleep(3)
    
    
    except WebDriverException:
        f = open('insta.txt','a')
        f.write("エラーが発生しました\n")
        f.close()
driver.quit()


# In[ ]:




