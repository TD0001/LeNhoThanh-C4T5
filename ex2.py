price ={
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock ={
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
total = 0
for i in price:
    print(i)
    print("+price:", price[i])
    for z in stock:
        if z == i:
            print("+stock:", stock[z])
            total = total + stock[z]*price[i]
print(total)