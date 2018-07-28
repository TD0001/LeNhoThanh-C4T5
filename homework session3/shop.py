selection = ["c", "r", "u", "d"]
items = ["T-shirt", "Sweater"]
choose = input("what do you want to do? (C,R,U,D)? ")
while choose == "c" or "r" or "u" or "d":
    if choose == "r":
        print(*items, sep = ", ")
        # choose = input("what do you want to? (C,R,U,D)? ")
    elif choose == "c":
        new = input("Enter new item: ")
        items.append(new)
        print(*items, sep = ", ")
        # choose = input("what do you want to? (C,R,U,D)? ")
    elif choose == "u":
        pos = int(input("update position? "))
        new = input("Enter new item: ")
        items.insert(pos-1,new)
        print(*items, sep = ", ")
    elif choose == "d":
        pos = int(input("choose the position to delete: "))
        items.pop(pos-1)
        print(*items, sep=", ")
    choose = input("what do you want to do? (C,R,U,D)? ")
