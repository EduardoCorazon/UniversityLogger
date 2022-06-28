'''
Made by: Eduardo Corazon
Description: Python script used to protect agaisnt shoulder surfing attacks and automates log in for University websites  & other ? (future work)
For configuration please modify the config.py file in this repo (The config has both manual and GUI configuration)
Will use electron + react to develop GUI ; Goal: protect from shoulder surfing and employ automation
'''

# imports
import json
from crypto import *
from config import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By



#import Data from Json file
with open('Defaults.json') as f:
    data = json.load(f)

def loadconfig():
    #check which WebBrowser to use
    for item in data['Defaults']:
        web = item['WebBrowser']

        if web == "Chrome":
            pass
        elif web == "Firefox":
            pass
        else:
            #use chrome
            pass

    #load up the main website 



#main code
def main():
    loadconfig()

    for item in data['Defaults']:
        print(item['MainURL'])
    

if __name__ == "__main__":
    main()