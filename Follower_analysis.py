#!/usr/bin/env python
# coding: utf-8

# In[5]:


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
import random

username = ""
pw = ""
#インスタグラムのuser名とpassを代入

class InstaAnalise:
    def Login(self, username, pw):
        self.driver= webdriver.Chrome(executable_path = '')
        #executable_pathには、pythonで使う用のWebdriverの位置を代入
        self.driver.implicitly_wait(3)
        url_login = "https://www.instagram.com/?hl=ja"
        self.driver.get(url_login)
        time.sleep(3)
        print("ログインしました")

        element = self.driver.find_element_by_name("username")
        element.clear()
        element.send_keys(username)
        element = self.driver.find_element_by_name("password")
        element.clear()
        element.send_keys(pw)
        print("フォームを送信")

        browser_from =self. driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div')
        time.sleep(5)
        browser_from.click()
        print("情報を入力してログインしました")
        time.sleep(5)
        not_now = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
        not_now.click()
        time.sleep(5)
        not_now2 = self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm")
        not_now2.click()
        self.driver.find_elements_by_class_name('Fifk5')[4].click()
        time.sleep(3)
        myprofile = self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div")
        myprofile.click()
        time.sleep(3)
        following = self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()

        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            time.sleep(3)
            scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = self.driver.find_elements_by_tag_name('a')
        followingnames = [name.text for name in links if name.text != '']
        time.sleep(3)
        close_button = self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div:nth-child(1) > div > div:nth-child(3) > button")
        close_button.click()
        # close button
        time.sleep(3)
        follower = self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
        time.sleep(3)
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            time.sleep(3)
            scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = self.driver.find_elements_by_tag_name('a')
        followernames = [name.text for name in links if name.text != '']
        time.sleep(3)
        
        close_button = self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div:nth-child(1) > div > div:nth-child(3) > button")
        close_button.click()
        # close button


        not_following_back = set(followingnames)-set(followernames)
        not_following_back.remove("人物")
        not_following_back.remove("ハッシュタグ")
        print(not_following_back)
        self.driver.quit()
        
mybot= InstaAnalise()
mybot.Login(username, pw)


# In[6]:





# In[ ]:




