print("Enter the first number")
var1 = int(input())
print("Enter the second number")
var2 = int(input())
print("What do you want + , - , * , / , %")
var3 = input()

if var1 == 45 and var2 == 3 and var3 == '*':
    print("555")
elif var1 == 56 and var2 == 9 and var3 == '+':
        print("77")
elif var1 == 56 and var2 == 6 and var3 == '/':
        print("4")
elif var3 == '+':
    print(var1 + var2)
elif var3 == '-':
    print(var1 - var2)
elif var3 == '*':
    print(var1 * var2)
elif var3 == '/':
    print(var1 / var2)
elif var3 == '%':
    print(var2 % var1, "%")
else:
    print("Error ! Try again")