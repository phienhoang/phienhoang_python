# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# import time
# import random

# option = Options()

# option.add_argument("--disable-infobars")  #
# option.add_argument("start-maximized")     # Mo full man hinh
# option.add_argument("--disable-extensions") # tat add on
# option.add_argument("--incognito")   # tab an danh

# # Pass the argument 1 to allow and 2 to block
# option.add_experimental_option("prefs", { 
#     "profile.default_content_setting_values.notifications": 1 
# })


# driver = webdriver.Chrome(chrome_options=option, executable_path='D:/tool/chromedriver.exe')
# driver.implicitly_wait(60)
# driver.get('https://facebook.com')
# tk = driver.find_element_by_id('email')
# tk.send_keys('0335787435')
# time.sleep(random.uniform(1,2))
# # mk = driver.find_element_by_id('pass')
# mk = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input')
# mk.send_keys('phienhoang1234')
# time.sleep(random.uniform(1,2))
# dn = driver.find_element_by_name('login')
# dn.click()


# driver.find_element_by_xpath('//div[@aria-label="Tài khoản"]').click()
# time.sleep(random.uniform(1,2))
# driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div[4]/div/div[1]/div[2]/div/div/div/div/span').click()
# time.sleep(1)
# driver.close()

from driver_chrome import *
driver.delete_all_cookies()