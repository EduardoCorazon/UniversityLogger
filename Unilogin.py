

# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# setups
driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
url = 'https://myeagle.hccs.edu/'
driver.get(url)


# get a list of all options
text = driver.find_element(
    By.XPATH, '/html/body/section/main/div/div[2]/a/div').text
print(text)


china = driver.find_element(By.CLASS_NAME, 'block-content')
print(china)
# print(driver.find_elements_by_class_name('block-content'))


defl = 'https://hccsaweb.hccs.edu:8080/psp/csprd/?cmd=login&languageCd=ENG&'


selection = input('Where do you want to go? (x): ')
if selection == "x":

    lik = driver.find_elements(By.TAG_NAME, "a")
    links = []  # list to store all the links found on website
    titles = []
    for i in lik:
        titles.append(i.get_attribute('title'))
        links.append(i.get_attribute('href'))
    print("-----------------------------------------\n")
    print(links)
    print("--------------------------\n")
    print(titles)

    print("-----")
    for a, b in zip(titles, links):
        print(a, b)
driver.implicitly_wait(3)
'''

# for loggin in
driver.find_element_by_xpath(
    '//*[@id="userid"]').send_keys('username')
driver.find_element_by_xpath(
    '//*[@id="pwd"]').send_keys('testing')
# driver.find_element_by_xpath('//*[@id="loginbox"]/font/div[6]/input').click()

'''
