'''
This is the configuration file 
'''
#!/usr/bin/env python3

import json
import platform
from crypto import *
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
        SetLocation()
        
    else:
        print("please type in either 'y' or 'n'")
        Checkrunconf()
###########################################################################
#import the Json Config File
import json
with open('Defaults.json') as f:
    data = json.load(f)

###########################################################################
#find out what system the User is running to ser chromedriver location
def SetLocation():
    print("##################################################################\n")
    print("Detecting Os type...") 
    global DriverLocation
    #Check what sustem the User is running
    UserOs = platform.system()
    #set path based on OS
    if UserOs == "Windows":                
        DriverLocation = 'C:\\Users\\coraz\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe'
    elif UserOs == "Darwin":
        DriverLocation = "/usr/local/bin/chromedriver"
    else:
        DriverLocation= '/usr/bin/chromedriver'
    for item in data['Defaults']:
        item['ChromedriverLocation'] = item['ChromedriverLocation'].replace('', DriverLocation)
        print("Configuration file will be made for "+ platform.system() + " OS")
    SelWebBrowser()



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
            print(DriverLocation)
            driver = webdriver.Chrome(executable_path=DriverLocation, options=options)
            WebBrowserFinal = "Chrome"
        case "2":
            WebBrowserFinal = "Firefox"
        case default:
            driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        
    #update config file   
    for item in data['Defaults']:
        item['WebBrowser'] = item['WebBrowser'].replace('Chrome', WebBrowserFinal)
        print(item['WebBrowser']+ " will be used")
    SelMainURL(driver)

###########################################################################    
#modify the main Website URL based on University
def SelMainURL(driver):
    #initiate prompt
    print("##################################################################\n")
    print("Please select your university")
    print("Note: By default HCC will be used")
    Unichoice = ["HCC", "HBU"]
    Unichoicenum = [1,2,]
    #display options
    for a,b in zip(Unichoicenum, Unichoice):
        print(a,b)
    #let user choose
    sel = input("Select Number: ")
    mainUrl=''
    match sel:
        case "1":
            mainUrl = 'https://myeagle.hccs.edu/'
        case "2":
            mainUrl = 'https://hbu.edu/portal/'
    #update config file
    for item in data['Defaults']:
        item['MainURL'] = item['MainURL'].replace('https://myeagle.hccs.edu/', mainUrl)
        print("The main URL will be: "+item['MainURL'])
    driver.get(mainUrl)
    SelSubLink(driver)

###########################################################################
#choose which sub link to go to
def SelSubLink(driver):
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
    #update the config files
    for item in data['Defaults']:
        item['SubURL'] = item['SubURL'].replace('', selUrl)
        print("Website will go to: "+item['SubURL'])
    driver.get(selUrl)

def Credentials():
    #input prompt
    print("##################################################################\n")
    print("NOTE* Your credntials will be stored in an encrypted Config.json file")
    print("Please input your credentials for the site you want to access below: \n")
    #ask for username
    username  = input("Username/email: ")
    password = input("Password: ")
    for item in data['Defaults']:
        item['UserName'] = item['UserName'].replace('', username)
        item['PassWord'] = item['PassWord'].replace('', password)
    
    #Guide user to input xpath
    print("It's likely the script won't be a ble to find the the correct xpath to input credentials")
    print("Therefore, you need to manually input the username and password fields, Here's how to do it:")
    print("    1. right click on where you input your username/email")
    print("    2. select 'inspect element'")
    print("    3. right click the highligted element and hover on 'copy'")
    print("    4. click 'xpath' and now simply paste it below!")
    print("repeat for Password field and 'login' button\n")

    xpathUser = input("Paste xpath for username: ")
    xpathpass = input("Paste xpath for password: ")
    xpathButn = input("Paste xpath for Button: ")
    
    #test credentials
    print("Testing credentials...")
    driver.find_element_by_xpath(xpathUser).send_keys('username')
    driver.find_element_by_xpath(xpathpass).send_keys('testing')
    driver.find_element_by_xpath(xpathButn).click()
    '''
    driver.find_element_by_xpath('//*[@id="userid"]').send_keys('username')
    driver.find_element_by_xpath('//*[@id="pwd"]').send_keys('testing')
    driver.find_element_by_xpath('//*[@id="loginbox"]/font/div[6]/input').click()
    '''
    #Verify credentials work
    workcheck = input("Did the credentials work?: [y/n]")
    if workcheck == "y":
        print("Good! \nNow encrypting file...")
        encrypt()
    else:
        print("Retrying Credential input...")
        Credentials()


def encrypt():
    pass


# driver.close()

# driver.implicitly_wait(3)


'''

# for loggin in
driver.find_element_by_xpath('//*[@id="userid"]').send_keys('username')
driver.find_element_by_xpath('//*[@id="pwd"]').send_keys('testing')
driver.find_element_by_xpath('//*[@id="loginbox"]/font/div[6]/input').click()

'''

################################################## Main Code #########################
def main():
    Checkrunconf()
    #Update/create the Users Config file
    with open('Config.json','w') as f:
        json.dump(data, f, indent=2)
    

if __name__ == "__main__":
    main()

