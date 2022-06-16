

# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

# setups
driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
url = 'https://myeagle.hccs.edu/'
driver.get(url)

# create dictionary to store name and URL
sel_dict = {
    'name': [],
    'url': [],
}


# get a list of all options
text = driver.find_element_by_xpath(
    '/html/body/section/main/div/div[2]/a/div').text
print(text)
sel_dict["name"].append(text)
print(sel_dict)

print(driver.find_element_by_class_name('block-content'))
print(driver.find_elements_by_class_name('block-content'))


defl = 'https://hccsaweb.hccs.edu:8080/psp/csprd/?cmd=login&languageCd=ENG&'


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
