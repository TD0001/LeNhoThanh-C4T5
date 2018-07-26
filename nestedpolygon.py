from turtle import *

for n in range (3,7):
    if n % 2 == 1:
        color('blue')
    if n % 2 == 0:
            color('red')

    forward(69)

    for i in range (n-1):
        left(360/n)
        forward(69)

    left(360/n)

mainloop()