'''
Made by: Eduardo Corazon
Description: Python script used to protect agaisnt shoulder surfing attacks and automates log in for University websites  & other ? (future work)
For configuration please modify the config.py file in this repo (The config has both manual and GUI configuration)
Will use electron + react to develop GUI ; Goal: protect from shoulder surfing and employ automation
'''

# imports
# from config import *  # import config file

import json
with open('configProfiles.json') as f:
    data = json.load(f)

for item in data['Defaults']:
    item['Web Browser'] = item['Web Browser'].replace('Chrome', 'test2')

with open('new_data.json','w') as f:
    json.dump(data, f, indent=2)