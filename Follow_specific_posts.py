#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
import random
username = ""
pw = ""
#username pwには自分のユーザー名とパスワードを代入
taglist = ["#猫","#犬"]
#↑はいいねする投稿を検索するときに利用

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
time.sleep(3)

#投稿から最新のものを良いねする
def clicknice():
    target = driver.find_elements_by_class_name('_9AhH0')[10]
    actions = ActionChains(driver)
    #shiftを押した状態で操作している
    actions.move_to_element(target)
    actions.perform()
    f = open('insta.txt','a')
    f.write("最新の投稿まで画面を移動しました\n")
    f.close()
    time.sleep(1)

    try:
        driver.find_elements_by_class_name('_9AhH0')[9].click()
        #[9]の数字をランダムにすると変わる
        time.sleep(random.randint(2, 10))
        f = open('insta.txt','a')
        f.write("投稿をクリックしました\n")
        f.close()
        time.sleep(1)
        driver.find_element_by_class_name('fr66n').click()
        f = open('insta.txt','a')
        f.write("投稿をいいねしました\n")
        time.sleep(2)
        follow_from = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')
        time.sleep(random.randint(2, 10))
        follow_from.click()
        print("followしました")
        time.sleep(1)
        f.close()
        time.sleep(1)

    except WebDriverException:
        f = open('insta.txt','a')
        f.write("エラーが発生しました\n")
        f.close()
        return
    for i in range(random.randint(3, 5)):
        try:
            driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            f = open('insta.txt','a')
            f.write("次の投稿へ移動しました\n")
            f.close()
            time.sleep(random.randint(random.randint(2, 5), random.randint(10, 15)))

        except WebDriverException:
            f = open('insta.txt','a')
            f.write(i+"つ目の位置でエラーが発生しました\n")
            f.close()
            time.sleep(5)

        try:
            driver.find_element_by_class_name('fr66n').click()
            f = open('insta.txt','a')
            f.write("投稿をいいねしました\n")
            f.close()
            time.sleep(2)
        except WebDriverException:
            f = open('insta.txt','a')
            f.write("3つ目の位置でエラーが発生しました\n")
            f.close()
        
for i in taglist:
    serchbox = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
    serchbox.clear()
    serchbox.send_keys(i)
    time.sleep(3)
    serchbox.send_keys(Keys.ENTER)
    serchbox.send_keys(Keys.ENTER)
    time.sleep(8)
    
    clicknice()
    print(i+"の投稿にいいねとフォローをしました")
    close = driver.find_element_by_xpath("/html/body/div[5]/div[3]/button")
    close.click()
    home = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[1]")
    home.click()
    time.sleep(3)
    
driver.quit()


# In[ ]:




