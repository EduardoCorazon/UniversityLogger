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



###########################################################################
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



###########################################################################
#import the Json Config File
import json
with open('Config.json') as f:
    data = json.load(f)


###########################################################################
# aks user to choose their web browser
def SelWebBrowser():
    #added this to fix Selenium driver log issue
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    global driver
    #Initiate prompt
    print("##################################################################\n") 
    print("Please select a web browser")
    print("Note: By default Chrome will be used\n")
    webchoice = ["Chrome", "Firefox", "Safari", "Edge"]
    webchoicenum = [1,2,3,4]
    #Display a selection for the user
    for a,b in zip(webchoicenum, webchoice):
        print(a,b)
    webselec = input("\nselect Number: ")
    #let the user choose
    WebBrowserFinal = ''
    match webselec:
        case "1":
            driver = webdriver.Chrome(executable_path='C:\\Users\\coraz\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe', options=options)
            WebBrowserFinal = "Chrome"
        case "2":
            WebBrowserFinal = "Firefox"
        case default:
            driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        
    #update config file   
    for item in data['Defaults']:
        item['WebBrowser'] = item['WebBrowser'].replace('Chrome', WebBrowserFinal)
        print(item['WebBrowser'])
    return driver

###########################################################################    
#modify the main Website URL based on University
def SelMainURL(driver):
    print("##################################################################\n")
    print("Please select your university")
    print("Note: By default HCC will be used")
    Unichoice = ["HCC", "HBU"]
    Unichoicenum = [1,2,]
    for a,b in zip(Unichoicenum, Unichoice):
        print(a,b)
    sel = input("Select Number: ")
    mainUrl=''
    match sel:
        case "1":
            mainUrl = 'https://myeagle.hccs.edu/'
        case "2":
            mainUrl = 'https://hbu.edu/portal/'
    driver.get(mainUrl)

###########################################################################
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
    SelMainURL(driver)

    #Update the Users Config file
    with open('new_data.json','w') as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    main()

