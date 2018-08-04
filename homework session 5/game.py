import pygame
from random import randint
#1. initialize
pygame.init()

pygame.display.set_caption("pong game") #đặt tên window

# 2. set up game window
SIZE = (600, 600)
BG_color = (0, 28, 211) #đổ màu

canvas = pygame.display.set_mode(SIZE)

clock = pygame.time.Clock()

paddle_image1 = pygame.image.load("assets/paddle1.png") #load ảnh
paddle_image2 = pygame.image.load("assets/paddle2.png")
ball_image = pygame.image.load("assets/ball.png")
x1 = 0
y1 = 0
x2 = 570
y2 = 500

x3 = 300
y3 =200
ball_v_x = 1.55
ball_v_y = 2
w_pressed = False
s_pressed = False
i_pressed = False
k_pressed = False
i = randint (0,500)
loop = True
while loop:
    # pooling
    events = pygame.event.get() # -> lấy ra event của pygame
    for e in events:
        if e.type == pygame.QUIT:
            print("QUIT")
            loop = False # action -> exit game
        elif e.type == pygame.KEYDOWN:
            # if e.key == pygame.K_w:
            #     y1 -=5
            # if e.key == pygame.K_s:
            #     y1 +=5
            # if e.key == pygame.K_i:
            #     y2 -=5
            # if e.key == pygame.K_k:
            #     y2 +=5
            if e.key == pygame.K_w:
                w_pressed = True
            if e.key == pygame.K_s:
                s_pressed = True
            if e.key == pygame.K_i:
                i_pressed = True
            if e.key == pygame.K_k:
                k_pressed = True
        else:
            if e.type == pygame.KEYUP:
                w_pressed = False
                s_pressed = False
                i_pressed = False
                k_pressed = False

    x3 = x3 + ball_v_x
    if (x3 >= 570 or x3<=0) or ((x3<=(x1+30)) and (y3>=y1 and y3<=(y1+120))) or (((x3+30)>=x2) and (y3>=y2 and y3<=(y2+120))):
        ball_v_x = - ball_v_x

    y3 = y3 + ball_v_y
    if (y3 >= 570 or y3 <=0):
        ball_v_y = - ball_v_y

    if w_pressed:
        if y1> 0:
            y1 -=5
    if s_pressed:
        if y1< 490:
            y1 +=5
    if i_pressed:
        if y2 >0:
            y2 -=5
    if k_pressed:
        if y2 < 490:
            y2 +=5

    canvas.fill(BG_color)
    canvas.blit(paddle_image1, (x1, y1) ) #Vẽ màu
    canvas.blit(paddle_image2, (x2, y2))
    canvas.blit(ball_image, (x3, y3 ))
    clock.tick(60)
    pygame.display.flip() #đảo canvas phụ vs canvas chính

#event: hành động người dùng, mang tính ngẫu nhiên
#action: phản ừng người dùng với event

