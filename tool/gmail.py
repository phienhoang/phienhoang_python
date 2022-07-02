from driver_chrome import *
t1 = 1
t2 = 2
HO = ['Hoang','Dao','Tran']
TEN = ['Phien','Minh','Manh']
driver.get('https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin')
sleep(random.uniform(t1,t2))
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/button/span').click()
sleep(random.uniform(t1,t2))
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/ul/li[1]/span[2]').click()
sleep(random.uniform(t1,t2))
ho = driver.find_element_by_id('lastName')
ho.send_keys(random.choice(HO))
sleep(random.uniform(t1,t2))
ten = driver.find_element_by_id('firstName')
ten.send_keys(random.choice(TEN))
sleep(random.uniform(t1,t2))
tk = driver.find_element_by_id('username')
tk.send_keys('hoangphien'+ random.choice('abcdefghijklmnopqrstusvwyz') +random.choice('abcdefghijklmnopqrstusvwyz')+random.choice('abcdefghijklmnopqrstusvwyz'))
sleep(random.uniform(t1,t2))
mk1 = driver.find_element_by_name('Passwd')
mk1.send_keys('uiop1234')
sleep(random.uniform(t1,t2))
mk2 = driver.find_element_by_name('ConfirmPasswd')
mk2.send_keys('uiop1234')
sleep(random.uniform(t1,t2))
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()
driver.implicitly_wait(10)
while True:
	try:
		if driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div[2]/div[2]/div').text == "Tên người dùng đã được sử dụng":
			tk = driver.find_element_by_id('username')
			tk.send_keys('hoangphien'+ random.choice('abcdefghijklmnopqrstusvwyz') +random.choice('abcdefghijklmnopqrstusvwyz')+random.choice('abcdefghijklmnopqrstusvwyz'))
			sleep(random.uniform(t1,t2))
			driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[1]').click()
		else:
			break
	except:
		break
sdt = driver.find_element_by_id('phoneNumberId')
sdt.send_keys('+79158967064')
sleep(random.uniform(t1,t2))
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()


