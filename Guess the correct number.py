n = 18
number_of_gusses = 1
print("You have only 9 times fo guesses")
while (number_of_gusses<=9):
    gusses_number = int(input("guess the number : \n"))
    if (gusses_number<18):
        print("you entered smaller number try big one : \n")
    elif (gusses_number>18):
        print("you entered bigger number try small one : \n")
    else:
        print("you win")
        print(number_of_gusses, "no. of guesses you took to finished")
        break
    print(9 - number_of_gusses, "no. of gusses left")
    number_of_gusses = number_of_gusses +1
if number_of_gusses>9:
    print("game over")