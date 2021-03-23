list = ["alex", 8, 4, "ilu", 3, "leena", 6]

for item in list:
    if str(item).isnumeric() and item>=6:
        print(item)