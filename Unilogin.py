

# imports
from cgi import print_arguments
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')

url = 'https://myeagle.hccs.edu/'

driver.get(url)


deflog = 'https://hccsaweb.hccs.edu:8080/psp/csprd/?cmd=login&languageCd=ENG&'

text = driver.find_element_by_xpath(
    '/html/body/section/main/div/div[2]/a/div').text
print(text)

selection = input('Where do you want to go? (x): ')
if selection == "x":
    driver.get(deflog)
driver.implicitly_wait(3)

# for loggin in
driver.find_element_by_xpath(
    '//*[@id="userid"]').send_keys('username')
driver.find_element_by_xpath(
    '//*[@id="pwd"]').send_keys('testing')
# driver.find_element_by_xpath('//*[@id="loginbox"]/font/div[6]/input').click()
