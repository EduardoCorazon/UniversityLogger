
from cryptography.fernet import Fernet


def loadkey():
    #create key
    key = Fernet.generate_key()
    with open ('mykey.key', 'wb') as mykey:
        mykey.write(key)
    

def encrypt():
    #read key
    with open('mykey.key', 'rb') as mykey:
        key = mykey.read()
    print(key)

    #Encrypt
    f = Fernet(key)
    with open('Config.json', 'rb') as original_file:
        original = original_file.read()
    encrypted = f.encrypt(original)
    with open ('encrypt_Config.json', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def decrypt():
    #read key
    with open('mykey.key', 'rb') as mykey:
        key = mykey.read()
    print(key)
    
    #decrypt
    f = Fernet(key)
    with open('encrypt_Config.json', 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    decrypted = f.decrypt(encrypted)
    with open('decrypted_Config.json', 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
