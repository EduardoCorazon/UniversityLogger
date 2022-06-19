'''
This is the configuration file 
'''
#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from simple_term_menu import TerminalMenu


#Makes sure the user wants to run the configurator
def Checkrunconf():
    runconfig = input("Would you like to run the configurator now: [y/n]")
    if runconfig == "n":
        exit()
    elif runconfig == "y":
        pass
    else:
        print("please type in either 'y' or 'n'")
        Checkrunconf()


'''
def main():
    options = ["entry 1", "entry 2", "entry 3"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")

if __name__ == "__main__":
    main()
'''



# aks user to choose their web browser
def SelWebBrowser(): 
    print("Please select a web browser to use: ")
    print("By default Chrome will be used")
    sel = input("")
    driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
    return driver


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
