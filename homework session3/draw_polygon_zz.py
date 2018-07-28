from turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey']
c = 0
for n in range (3,8):
    color(colors[c])
    c =c + 1
    forward(69)

    for i in range (n-1):
        left(360/n)
        forward(69)

    left(360/n)

mainloop()