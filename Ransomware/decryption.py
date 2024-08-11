import os
from cryptography.fernet import Fernet as cryp

files=[]

link_folder=r"C:\Users\ADMIN\OneDrive - Hanoi University of Science and Technology\Desktop\Test"

def find_file(link_path):
    for file in os.listdir(link_path):
        newlink = os.path.join(link_path, file)
        if os.path.isfile(newlink):
            files.append(newlink)
        else:
            find_file(newlink)

def decryp_file(key_decrypt, files):
    for file in files:
        with open(file, "rb") as read:
            data=read.read()
        decrypted_data=cryp(key_decrypt).decrypt(data)
        with open(file, "wb") as write:
            write.write(decrypted_data)


find_file(link_folder)

# key = cryp.generate_key()
with open(r"C:\Users\ADMIN\OneDrive - Hanoi University of Science and Technology\Desktop\key.key", "rb") as thekey_decrypt:
    keydecrypt=thekey_decrypt.read()
    decryp_file(keydecrypt, files)