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


# key generation
key = Fernet.generate_key()
 
# string the key in a file
with open('filekey.key', 'wb') as filekey:
   filekey.write(key)

# opening the key
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
 
# using the generated key
fernet = Fernet(key)
 
# opening the original file to encrypt
with open('nba.csv', 'rb') as file:
    original = file.read()
     
# encrypting the file
encrypted = fernet.encrypt(original)
 
# opening the file in write mode and
# writing the encrypted data
with open('nba.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

# using the key
fernet = Fernet(key)
 
# opening the encrypted file
with open('nba.csv', 'rb') as enc_file:
    encrypted = enc_file.read()
 
# decrypting the file
decrypted = fernet.decrypt(encrypted)
 
# opening the file in write mode and
# writing the decrypted data
with open('nba.csv', 'wb') as dec_file:
    dec_file.write(decrypted)



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



#main code
def main():
    loadconfig()
    for item in data['Defaults']:
        print(item['MainURL'])


if __name__ == "__main__":
    main()