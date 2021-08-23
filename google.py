#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time 
import urllib.request 
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com.au/imghp?hl=en&authuser=0&ogbl")
elem = driver.find_element_by_name("q")
elem.send_keys("조코딩")
elem.send_keys(Keys.RETURN)
images=driver.find_elements_by_css_selector(".rg_i.Q4LuWd")


SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
            # time.sleep(SCROLL_PAUSE_TIME)
        except:
            break
    last_height = new_height

count=1
# for image in images:
    # try:
        # image.click()
        # time.sleep()
        # driver.implicitly_wait(10)
        # imgUrl=driver.find_element_by_xpath_selector("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img").get_attribute("src")
        # urllib.request.urlretrieve(imgUrl, str(count)+".jpg")
        # count=count+1
    # except:
        # pass

driver.close()



