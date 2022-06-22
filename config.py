'''
This is the configuration file 
'''
#!/usr/bin/env python3

import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
#from simple_term_menu import TerminalMenu <- if on UNIX use this, Note to self: expand on this later https://github.com/IngoMeyer441/simple-term-menu




#Makes sure the user wants to run the configurator
def Checkrunconf():
    runconfig = input("Would you like to run the configurator now: [y/n]")
    if runconfig == "n":
        exit()
    elif runconfig == "y":
        SelWebBrowser()
        
    else:
        print("please type in either 'y' or 'n'")
        Checkrunconf()


# aks user to choose their web browser
def SelWebBrowser():
    global driver
    print("##################################################################\n") 
    print("Please select a web browser")
    print("Note: By default Chrome will be used\n")
    webchoice = ["Chrome", "Firefox", "Safari", "Edge"]
    webchoicenum = [1,2,3,4]
    for a,b in zip(webchoicenum, webchoice):
        print(a,b)
    webselec = input("\nselect Number: ")
    match webselec:
        case "1":
            driver = webdriver.Chrome(executable_path='C:\\Users\\coraz\\Downloads\\chromedriver_win32\\chromedriver.exe')
            driver.get('https://myeagle.hccs.edu/')
        case "2":
            pass #add path for firefox
        case default:
            driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
    return driver
            
            
#modify the main Website URL based on University
def SelMainURL():
    print("##################################################################\n")
    print("Please select your university")
    print("Note: By default HCC will be used")
    Unichoice = ["HCC", "HBU"]
    Unichoicenum = [1,2,]
    for a,b in zip(Unichoicenum, Unichoice):
        print(a,b)
    sel = input("Select Number: ")
    match sel:
        case 1:
            mainUrl = 'https://myeagle.hccs.edu/'
            return mainUrl
        case 2:
            mainUrl = 'https://hbu.edu/portal/'
            return mainUrl
    driver.get(mainUrl)


#choose which sub link to go to
def SelSubLink():
    # get all objects that have links in website
    reftag = driver.find_elements(By.TAG_NAME, "a")
    # lists to store all the links found and their names
    links = []
    titles = []
    selection = []
    selnum = 0 #have to dynamically allocate selection list due to variablity in the number or URLs found
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
    return selUrl

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

################################################## Main Code #########################
def main():
    Checkrunconf()


if __name__ == "__main__":
    main()

