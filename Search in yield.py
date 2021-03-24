def search():
    list = ["chocolate", "burger", "pizza", "hotdog"]

    while True:
        a = (yield)
        if a in list:
            print("your Item is Available ", )
        else:
            print("Your item is not available")

a = search()
next(a)
a.send("pizza")
