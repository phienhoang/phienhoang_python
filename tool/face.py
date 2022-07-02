
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


t1 = 1
t2 = 2
t3 = 0.1
t4 = 0.2
TEN = ["James", "Robert", "John", "Michael", "William", "David", "Richard", "Joseph", "Thomas", "Charles", "Christopher", "Daniel", "Matthew", "Anthony", "Mark", "Donald", "Steven", "Paul", "Andrew", "Joshua", "Kenneth", "Kevin", "Brian", "George", "Edward", "Ronald", "Timothy", "Jason", "Jeffrey", "Ryan", "Jacob", "Gary", "Nicholas", "Eric", "Jonathan", "Stephen", "Larry", "Justin", "Scott", "Brandon", "Benjamin", "Samuel", "Gregory", "Frank", "Alexander", "Raymond", "Patrick", "Jack", "Dennis", "Jerry", "Tyler", "Aaron", "Jose", "Adam", "Henry", "Nathan", "Douglas", "Zachary", "Peter", "Kyle", "Walter", "Ethan", "Jeremy", "Harold", "Keith", "Christian", "Roger", "Noah", "Gerald", "Carl", "Terry", "Sean", "Austin", "Arthur", "Lawrence", "Jesse", "Dylan", "Bryan", "Joe", "Jordan", "Billy", "Bruce", "Albert", "Willie", "Gabriel", "Logan", "Alan", "Juan", "Wayne", "Roy", "Ralph", "Randy", "Eugene", "Vincent", "Russell", "Elijah", "Louis", "Bobby", "Philip", "Johnny"]
HO = ["Johnson" ,"Williams" ,"Brown" ,"Jones" ,"Garcia" ,"Miller" ,"Davis" ,"Rodriguez" ,"Martinez" ,"Hernandez" ,"Lopez" ,"Gonzalez" ,"Wilson" ,"Anderson" ,"Thomas" ,"Taylor" ,"Moore" ,"Jackson" ,"Martin" ,"Lee" ,"Perez" ,"Thompson" ,"White" ,"Harris" ,"Sanchez" ,"Clark" ,"Ramirez" ,"Lewis" ,"Robinson" ,"Walker" ,"Young" ,"Allen" ,"King" ,"Wright" ,"Scott" ,"Torres" ,"Nguyen" ,"Hill" ,"Flores" ,"Green" ,"Adams" ,"Nelson" ,"Baker" ,"Hall" ,"Rivera" ,"Campbell" ,"Mitchell" ,"Carter" ,"Roberts"]


driver.get('https://facebook.com')
driver.implicitly_wait(30)
sleep(random.uniform(t1,t2))
actions.move_to_element(driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a')).click(driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a')).perform()
sleep(random.uniform(t1,t2))
Ten = driver.find_element_by_name("firstname")
actions.move_to_element(Ten)
actions.click(Ten)
actions.perform()
for el in ten:
    Ten.send_keys(el)
    sleep(random.uniform(t3,t4))
Ho = driver.find_element_by_name('lastname')
actions.move_to_element(Ho)
actions.click(Ho)
actions.perform()
for el in ho:
    Ho.send_keys(el)
    sleep(random.uniform(t3,t4))
mail = driver.find_element_by_name('reg_email__')
actions.move_to_element(mail)
actions.click(mail)
actions.perform()
acc = acc + '@outlook.com'
for el in acc:
    mail.send_keys(el)
    sleep(random.uniform(t3,t4))
mail2 = driver.find_element_by_name('reg_email_confirmation__')
actions.move_to_element(mail2).click(mail2).perform()
for el in acc:
    mail2.send_keys(el)
    sleep(random.uniform(t3,t4))
password = driver.find_element_by_name('reg_passwd__')
actions.move_to_element(password).click(password).perform()
for el in mk:
    password.send_keys(el)
    sleep(random.uniform(t3,t4))
actions.move_to_element(driver.find_element_by_id('day')).click(driver.find_element_by_id('day')).perform()
sleep(random.uniform(t1,t2))
select1 = Select(driver.find_element_by_id('day'))
day = select1.select_by_value(str(random.randint(1,28)))
actions.move_to_element(day).click(day).perform()
sleep(random.uniform(t1,t2))
actions.move_to_element(driver.find_element_by_id('month')).click(driver.find_element_by_id('month')).perform()
select2 = Select(driver.find_element_by_id('month'))
month = select2.select_by_value(str(random.randint(1,12)))
actions.move_to_element(month).click(month).perform()
sleep(random.uniform(t1,t2))
actions.move_to_element(driver.find_element_by_id('year')).click(driver.find_element_by_id('year')).perform()
sleep(random.uniform(t1,t2))
select3 = Select(driver.find_element_by_id('year'))
year = select3.select_by_value(str(random.randint(1980,2000)))
actions.move_to_element(year).click(year).perform()
sleep(random.uniform(t1,t2))
sex = driver.find_elements_by_name('sex')
sex_ = random.choice(sex[:2])
actions.move_to_element(sex_).click(sex_).perform()
# nu = driver.find_element_by_xpath('''//label[contains(text(), "Женщина")]''')
# nam = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[2]/input')
# random.choice([nam,nu]).click()
sleep(random.uniform(t1,t2))