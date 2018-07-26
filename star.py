from turtle import *

color('red')
left(120)
for j in range(2):
    for i in range (0,2):
        forward(100)

        if i ==0:
            right(60)
        else: left(60)

        forward(100)

        if i ==0:
            right(120)
        else: left(120)

        forward(100)

        if i ==0:
            right(60)
        else: left(60)
        forward(100)
    right(90)
mainloop()