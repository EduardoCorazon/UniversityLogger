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


from cryptography.fernet import Fernet

#create key
key = Fernet.generate_key()
with open ('mykey', 'wb') as mykey:
    mykey.write(key)

#load up key
with open('mykey.key', 'rb') as mykey:
    key = mykey.read()
print(key)

#Encrypt
f = Fernet(key)
with open('test.csv', 'rb') as original_file:
    original = original_file.read()
encrypted = f.encrypt(original)
with open ('encrypt_test', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

#decrypt
f = Fernet(key)
with open('enc_grades.csv', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()
decrypted = f.decrypt(encrypted)
with open('dec_grades.csv', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)


'''

#import Data from Json file
with open('Defaults.json') as f:
    data = json.load(f)

def loadconfig():
    #check which WebBrowser to use
    for item in data['Defaults']:
        web = item['webbrowser']
        
        if web == "Chrome":
            pass
        elif web == "Firefox":
            pass
        else:
            #use chrome
            pass

    #load up the main website 


'''
#main code
def main():
    '''
    loadconfig()
    for item in data['Defaults']:
        print(item['MainURL'])
    '''
    

if __name__ == "__main__":
    main()