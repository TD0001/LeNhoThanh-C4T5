for i in range (20):
    print(i, end = " ")
print()
print()
n = int(input("n = "))
for i in range (n):
    print(i, end = " ")
print()
print()
for i in range (20):
    print((i+1) % 2, end = " ")
print()
print()
for i in range (n):
    print((i+1) % 2, end = " ")
print()
print()
for i in range (1,10):
    for j in range (i,10*i,i):
        if j < 10:
            print(j,end = "      ")
        else:
            print(j, end="     ")
    print()
    print()
for i in range (1,n+1):
    for j in range (i,(n+1)*i,i):
        if j < 10:
            print(j,end = "      ")
        elif j < 100:
                print(j, end = "     ")
        else: print(j, end ="    ")
    print()
