<<<<<<< HEAD
sizes = ["","","","","","",""]
from  random import randint
l = len(sizes)
c = 0
for i in range (l):
    sizes[i] = randint(1, 500)

print("hello, my name is Fuc, these are my sheep sizes")
print(*sizes, sep = " ")
max=0
for i in range (l):
    if max < sizes[i]:
        max = sizes[i]
        c = i
print("Now my biggest sheep has size:",max,". Let's shear it")
sizes[c]= 8

print("After shearing, here is my flock")
print(*sizes, sep = ", ")
print()

for i in range (l):
    sizes[i] +=50
print("Month 1:")
print("One month has passed, now here is my flock")
print(*sizes, sep = ", ")
max=0
for i in range (l):
    if max < sizes[i]:
        max = sizes[i]
        c = i
print("Now my biggest sheep has size:",max,". Let's shear it")
sizes[c]= 8
print()
print("After shearing, here is my flock")
print(*sizes, sep = ", ")
print()

for i in range (l):
    sizes[i] +=50
print("Month 2:")
print("One month has passed, now here is my flock")
max=0
print(*sizes, sep = ", ")
for i in range (l):
    if max < sizes[i]:
        max = sizes[i]
        c = i
print("Now my biggest sheep has size:",max,". Let's shear it")
sizes[c]= 8
print()
print("After shearing, here is my flock")
print(*sizes, sep = ", ")
print()

for i in range (l):
    sizes[i] +=50
print("Month 3:")
print("One month has passed, now here is my flock")
print(*sizes, sep = ", ")
max=0
for i in range (l):
    if max < sizes[i]:
        max = sizes[i]
        c = i
print("Now my biggest sheep has size:",max,". Let's shear it")
sizes[c]= 8
print()
print("After shearing, here is my flock")
print(*sizes, sep = ", ")
print()

s = 0
for i in range (l):
    s = s + sizes[i]
print("my flock has size in total:",s)
print("I would get",s,"* 2$ = ", s*20)
=======
num = int(input("how many?: "))
sizes = []
from  random import randint
l = len(sizes)
c = 0
for i in range (num):
    sizes.append(randint(1, 500))

print("hello, my name is Fuc, these are my sheep sizes")
print(*sizes, sep = " ")
max=0
for i in range (l):
    if max < sizes[i]:
        max = sizes[i]
        c = i
print("Now my biggest sheep has size:",max,". Let's shear it")
sizes[c]= 8

print("After shearing, here is my flock")
print(*sizes, sep = ", ")
print()

for i in range (l):
    sizes[i] +=50
print("Month 1:")
print("One month has passed, now here is my flock")
print(*sizes, sep = ", ")
max=0
for i in range (l):
    if max < sizes[i]:
        max = sizes[i]
        c = i
print("Now my biggest sheep has size:",max,". Let's shear it")
sizes[c]= 8
print()
print("After shearing, here is my flock")
print(*sizes, sep = ", ")
print()

for i in range (l):
    sizes[i] +=50
print("Month 2:")
print("One month has passed, now here is my flock")
max=0
print(*sizes, sep = ", ")
for i in range (l):
    if max < sizes[i]:
        max = sizes[i]
        c = i
print("Now my biggest sheep has size:",max,". Let's shear it")
sizes[c]= 8
print()
print("After shearing, here is my flock")
print(*sizes, sep = ", ")
print()

for i in range (l):
    sizes[i] +=50
print("Month 3:")
print("One month has passed, now here is my flock")
print(*sizes, sep = ", ")
max=0
for i in range (l):
    if max < sizes[i]:
        max = sizes[i]
        c = i
print("Now my biggest sheep has size:",max,". Let's shear it")
sizes[c]= 8
print()
print("After shearing, here is my flock")
print(*sizes, sep = ", ")
print()
l= len(sizes)
s = 0
for i in range (l):
    s = s + sizes[i]
print("my flock has size in total:",s)
print("I would get",s,"* 2$ = ", s*20)
>>>>>>> origin/master
