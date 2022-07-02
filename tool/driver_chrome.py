from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from time import sleep
import random

used_webdriver = "Chrome"

if used_webdriver =="Chrome":
    option = Options()
    option.add_experimental_option("useAutomationExtension", False)  # an auto
    option.add_experimental_option("excludeSwitches",["enable-automation"])
    option.add_argument("--disable-infobars")  #
    option.add_argument("start-maximized")     # Mo full man hinh
    option.add_argument("--disable-extensions") # tat add on
    option.add_argument("--incognito")   # tab an danh

    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", { 
        "profile.default_content_setting_values.notifications": 1 
    })

    # driver = webdriver.Chrome(chrome_options=option, executable_path='D:/tool/chromedriver.exe')
    driver = webdriver.Chrome(chrome_options=option, executable_path='driver/chromedriver')
else:
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
    options = webdriver.FirefoxOptions()
    # if useragent:
    #     firefox_profile.set_preference("general.useragent.override", custom_user_agent['firefox'])
    # if headless:
    #     options.add_argument('-headless')
    driver = webdriver.Firefox(executable_path="driver/geckodriver", firefox_profile=firefox_profile, options=options)

actions = webdriver.ActionChains(driver)
driver.implicitly_wait(60)