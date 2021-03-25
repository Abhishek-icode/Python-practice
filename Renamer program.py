# You can rename all files in one folder

import os

def manager(path, formate):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    for file in files:
        os.rename(file, f"{i}{formate}")
        i += 1
# Enter file formate
f = ".jpeg"

# Enter path and formate
manager(r"D:\Rudra2", f)