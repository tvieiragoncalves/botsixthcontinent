from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get("https://pt.sixthcontinent.com/")
login = driver.find_element_by_css_selector('sxc-popover.col > a:nth-child(1) > i:nth-child(1)')
login.click()
search = driver.find_element_by_id("loginEmail")
search.send_keys("USERNAME")
searchpwd = driver.find_element_by_id("pwdReg")
searchpwd.send_keys("PASSWORD")
log = driver.find_element_by_id("get-login")
log.click()
driver.close()
print('Sucesso!!!!')
