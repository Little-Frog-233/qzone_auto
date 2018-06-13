#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 19:21:46 2018

@author: ruicheng
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains###专门用来对于element invisiable

url = 'https://qzone.qq.com/'
path = '/Users/ruicheng/chromedriver01/chromedriver'
browser = webdriver.Chrome(path)
wait = WebDriverWait(browser,10)###限定显式等待时间

username = '囧...-_-o'
qq_number = '1342468180'
password = '1995_ruicheng'
text = '这是一条自动发的说说'

def auto_login():
    browser.get(url)
    browser.switch_to_frame("login_frame")###iframe
    bottom = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#bottom_qlogin .link')))
    print('正在进行',bottom.text)
    bottom.click()
    input_qq = wait.until(EC.presence_of_element_located((By.ID,'u')))
    input_qq.clear()
    input_qq.send_keys(qq_number)
    input_password = wait.until(EC.presence_of_element_located((By.ID,'p')))
    input_password.clear()
    input_password.send_keys(password)
    login = browser.find_element_by_css_selector('.login_button #login_button')
    login.click()
    time.sleep(5)
    html = browser.page_source
    if html.find(username) != -1:
        print('login successfully')
        return True
    else:
        print('login failly')
        return False

def send_twitter():
    center = browser.find_element_by_css_selector('#aIcenter')###先切换到个人中心
    center.click()
    m = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.textinput.textarea.c_tx3')))
    ActionChains(browser).move_to_element(m).click().send_keys(text).perform()
    bottom = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.op a.btn-post.gb_bt.evt_click')))
    ActionChains(browser).click(bottom).perform()

if __name__ == '__main__':
    if auto_login():
        send_twitter()
    else:
        pass
    browser.close()
        
                                                        
    