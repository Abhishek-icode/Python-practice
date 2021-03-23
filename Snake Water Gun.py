import random
print("WELCOME TO SNAKE, WATER, GUN Game")
print("What do you to make--\nS- Snake\nW- Water\nG- Gun")


chances = 10
no_of_chances = 0
computer_points = 0
human_points = 0


while (no_of_chances<chances):
    no_of_chances = no_of_chances + 1
    print(f"{chances - no_of_chances} is left out of {chances}")
    swg = str(input())
    cswg = ["Computer - Snake", "Computer - Water", "Computer - Gun"]
    z = random.choice(cswg)
    print(z)
    if (swg == "s") and (z == "Computer - Snake"):
        print("Snake and Snake Try again")
    elif (swg == "s") and (z == "Computer - Water"):
        human_points = human_points + 1
        print("Snake and Water you are Win")
        print(f"computer point is {computer_points} and your's point is {human_points}")
    elif (swg == "s") and (z == "Computer - Gun"):
        computer_points = computer_points + 1
        print("Snake and Gun you are loos")
        print(f"computer point is {computer_points} and your's point is {human_points}")
    elif (swg == "w") and (z == "Computer - Snake"):
        computer_points = computer_points + 1
        print("Water and Snake you are loose")
        print(f"computer point is {computer_points} and your's point is {human_points}")
    elif (swg == "w") and (z == "Computer - Water"):
        print("Water and Water Try again")
    elif (swg == "w") and (z == "Computer - Gun"):
        human_points = human_points + 1
        print("Water and gun you are Win")
        print(f"computer point is {computer_points} and your's point is {human_points}")
    elif (swg == "g") and (z == "Computer - Snake"):
        human_points = human_points + 1
        print("Gun and Snake you are Win")
        print(f"computer point is {computer_points} and your's point is {human_points}")
    elif (swg == "g") and (z == "Computer - Water"):
        computer_points = computer_points + 1
        print("Gun and Water you are loos")
        print(f"computer point is {computer_points} and your's point is {human_points}")
    elif (swg == "g") and (z == "Computer - Gun"):
        print("Gun and Gun Try again")
    else:
        print("You entered wrong key")

print("---------Game over now-------")

if (human_points == computer_points):
    print("Both points are same it's Tail")
elif (human_points > computer_points):
    print("You win and computer loss")
elif (human_points < computer_points):
    print("Computer win and you loss")

print(f"Your point is {human_points} and Computer points is {computer_points}")