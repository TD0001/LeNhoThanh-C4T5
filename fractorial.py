n= int(input("n = "))
if n <= 0:
    print("math error")
f = 1
for i in range (1,n+1):
    f = f * i
print(n,"! = ",f)