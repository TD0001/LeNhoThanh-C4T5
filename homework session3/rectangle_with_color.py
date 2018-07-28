from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
c = 1

for i in range (5):
    color(colors[c-1])
    c = c + 1
    begin_fill()
    forward(50)
    for j in range (2):
            right(90)
            forward(100)
            right(90)
            forward(50)
    end_fill()
mainloop()