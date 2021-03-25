print("Enter your age or Date of birth in year and know how will you look in 2090")
a = int(input())

if a > 0 and a <= 33:
    print("you look like old and your age in 1990 will be ", 2090 - 2021 + a)

elif a > 33 and a <= 44:
    print("you may be dead, and your age will be => ", 2090 - 2021 + a, "in 2090")

elif a > 44 and a <= 1950:
    print("you must be dead in 1990 and your age will be", 2090 - 2021 + a)

elif a > 1950 and a <= 1988:
    print("you must be dead 1n 1990 and your age in 1990 is", 2090 - a)

elif a > 1988 and a < 2021:
    print("You will look like old, and your age will be", 2090 - a, "in 2090")

else:
    print("You Entered something Wrong")