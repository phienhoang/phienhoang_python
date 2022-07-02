from driver_chrome import *
t1 = 1
t2 = 2
HO = ['Hoang','Dao','Tran']
TEN = ['Phien','Minh','Manh']
MXN = '64850'
driver.get('https://facebook.com')
sleep(random.uniform(t1,t2))
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a').click()
sleep(random.uniform(t1,t2))
ten = driver.find_element_by_name("firstname")
ten.send_keys(random.choice(TEN))
sleep(random.uniform(t1,t2))
ho = driver.find_element_by_name('lastname')
ho.send_keys(random.choice(HO))
sleep(random.uniform(t1,t2))
mail = driver.find_element_by_name('reg_email__')
mail.send_keys('hoangphiendaik@outlook.com')
sleep(random.uniform(t1,t2))
mail2 = driver.find_element_by_name('reg_email_confirmation__')
mail2.send_keys('hoangphiendaik@outlook.com')
sleep(random.uniform(t1,t2))
mk = driver.find_element_by_name('reg_passwd__')
mk.send_keys('phienhoang1234')
sleep(random.uniform(t1,t2))
select1 = Select(driver.find_element_by_id('day'))
select1.select_by_value(str(random.randint(1,28)))
sleep(random.uniform(t1,t2))
select2 = Select(driver.find_element_by_id('month'))
select2.select_by_value(str(random.randint(1,12)))
sleep(random.uniform(t1,t2))
select3 = Select(driver.find_element_by_id('year'))
select3.select_by_value(str(random.randint(1990,2000)))
sleep(random.uniform(t1,t2))
nu = driver.find_element_by_xpath('''//label[contains(text(), "Женщина")]''')
nam = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[2]/input')
random.choice([nam,nu]).click()
sleep(random.uniform(t1,t2))
driver.find_element_by_name('websubmit').click()
sleep(random.uniform(t1,t2))
ma = driver.find_element_by_id('code_in_cliff')
ma.send_keys(MXN)
sleep(random.uniform(t1,t2))
driver.find_element_by_name('confirm').click()
with open('D://tool/accface.txt', 'a') as file :
	file.write('tk mk\n')


