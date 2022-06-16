

# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')

url = 'https://myeagle.hccs.edu/'

driver.get(url)


driver.find_element_by_xpath(
    '/html/body/section/main/div/div[2]/a').click()

#text = driver.find_element_by_xpath('/html/body/section/main/div/div[2]/a/div').text
# print(text)

driver.implicitly_wait(3)


driver.find_element_by_xpath(
    '/html/body/div/form/div/div/div[2]/font/div[2]/input').send_keys('testing')


# driver.find_element_by_xpath('//*[@id="pwd"]').send_keys('test')
# driver.find_element_by_xpath('//*[@id="login_form"]/div[3]/div[2]/button').click()
