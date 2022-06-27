
from cryptography.fernet import Fernet

#create key
key = Fernet.generate_key()
with open ('mykey.key', 'wb') as mykey:
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
with open ('encrypt_test.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

#decrypt
f = Fernet(key)
with open('encrypt_test.csv', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()
decrypted = f.decrypt(encrypted)
with open('decrypted_test.csv', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)