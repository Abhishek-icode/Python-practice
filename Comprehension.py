
no_of_list = int(input("how many do you want add in list"))
input_strimg = input("type your items with space")
list = input_strimg.split()
user_input = int(input("which type of comprihansion do you want---------\n1- List Comprehension\n2- Set Comprehension"))
if user_input==1:
    ls = [i for i in list]
    print(ls)
    print(type(ls))

elif user_input==2:
    set = {i for i in list}
    print(set)
    print(type(set))