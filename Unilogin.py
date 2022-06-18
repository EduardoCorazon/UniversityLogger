'''
Made by: Eduardo Corazon
Description: Python script to automate Univerisity website log in and access main apps
For configuration please modify the config.py file in this repo
'''

# imports

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# setups
driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')

# modify this URL depending on website
mainUrl = 'https://myeagle.hccs.edu/'
driver.get(mainUrl)


# For now im going to act like theres no config


# get all objects that have links in website
reftag = driver.find_elements(By.TAG_NAME, "a")
# lists to store all the links found and their names
links = []
titles = []
selection = []
selnum = 0
# add data to each
for i in reftag:
    titles.append(i.get_attribute('title'))
    links.append(i.get_attribute('href'))
    selnum += 1
    selection.append(selnum)

# combine the lists for selection
print("##################################################################\n")
print("Here is a list of all the links found in the website\n")
for a, b, c in zip(selection, titles, links):
    print(a, b, c)

selchoice = int(input("Please select a number to go to: "))
# set the url to the selected link in the list (use sel-1 due to format)
selUrl = links[selchoice - 1]
driver.get(selUrl)

driver.implicitly_wait(4)

# driver.close()

# driver.implicitly_wait(3)


'''

# for loggin in
driver.find_element_by_xpath(
    '//*[@id="userid"]').send_keys('username')
driver.find_element_by_xpath(
    '//*[@id="pwd"]').send_keys('testing')
# driver.find_element_by_xpath('//*[@id="loginbox"]/font/div[6]/input').click()

'''
