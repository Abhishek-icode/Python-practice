# own program
import datetime

def getdate():
    return datetime.datetime.now()

print("Welcome to health Management System")
print("who are you---\n1- alex\n2- ilu\n3- elon\nEnter number---")
cand = int(input())
if cand == 1:
    print("what do you record---\n1- Fitness records\n2- food record\nEnter number---")
    records = int(input())
    if records == 1:
        f = open("Alex_fitness_record.txt", "a")
        print("Write your records")
        wrcon = input()
        f.write(str(str(getdate())) + " : " + wrcon + "\n")
        f.close()
        print("your records has been recorded")
    else:
        f = open("alex_food_records.txt", "a")
        print("Write your records")
        wrcon = input()
        f.write(str(str(getdate())) + " : " + wrcon + "\n")
        f.close()
        print("your records has been recorded")

elif cand == 2:
    print("what do you record---\n1- Fitness records\n2- food record\nEnter number---")
    records = int(input())
    if records == 1:
        f = open("ilu_fitness_record.txt", "a")
        print("Write your records")
        wrcon = input()
        f.write(str(str(getdate())) + " : " + wrcon + "\n")
        f.close()
        print("your records has been recorded")
    else:
        f = open("ilu_food_records.txt", "a")
        print("Write your records")
        wrcon = input()
        f.write(str(str(getdate())) + " : " + wrcon + "\n")
        f.close()
        print("your records has been recorded")
else:
    print("what do you record---\n1- Fitness records\n2- food record\nEnter number---")
    records = int(input())
    if records == 1:
        f = open("elon_fitness_record.txt", "a")
        print("Write your records")
        wrcon = input()
        f.write(str(str(getdate())) + " : " + wrcon + "\n")
        f.close()
        print("your records has been recorded")
    else:
        f = open("elon_food_records.txt", "a")
        print("Write your records")
        wrcon = input()
        f.write(str(str(getdate())) + " : " + wrcon + "\n")
        f.close()
        print("your records has been recorded")