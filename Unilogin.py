'''
Made by: Eduardo Corazon
Description: Python script used to protect agaisnt shoulder surfing attacks and automates log in for University websites  & other ? (future work)
For configuration please modify the config.py file in this repo (The config has both manual and GUI configuration)
Will use electron + react to develop GUI ; Goal: protect from shoulder surfing and employ automation
'''

# imports
import json
import webbrowser
from config import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By



#import Data from Json file
with open('Config.json') as f:
    data = json.load(f)

def loadconfig():
    #display primary message
    print("This program will run on default settings, please run config.py to customize your experince!")
    #fix terminal bug
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #import Json file values
    for item in data['Defaults']:
        Webbrowser = item['WebBrowser']
        DriverLocation = item['ChromedriverLocation']
        MainURL = item['MainURL']
        SubURL = item['SubURL']

    #check what web Browser to use
    if Webbrowser == "Chrome":
        driver = webdriver.Chrome(executable_path=DriverLocation, options=options)
    elif Webbrowser == "Firefox":
        pass
    else:
        print("There was a problem determining what Web Browser to use, Please re-run configurator")
    
    #check if user has input for a subURL
    if SubURL == '':
        driver.get(MainURL)
    else:
        driver.get(SubURL)


#main code
def main():
    loadconfig()

if __name__ == "__main__":
    main()