import pygame 
from gui_func import *


pygame.init()
scrn = pygame.display.set_mode((600,600))
pygame.display.set_caption("my game")
back_img = pygame.image.load('back.jpg')

font = pygame.font.Font('freesansbold.ttf',32)
global sqr
sqr = new_grid()
sqr[3][2] = 2
sqr[3][0] = 2



#controls
def move_down():
    global sqr
    sqr = transverse(sqr)
    sqr = reverse(sqr)
    sqr = move(sqr)
    merge(sqr)
    sqr = move(sqr)
    sqr = reverse(sqr)
    sqr = transverse(sqr)
    add_new(sqr)


def move_left():
    global sqr
    sqr = move(sqr)
    merge(sqr)
    sqr = move(sqr)
    add_new(sqr)


def move_right():
    global sqr
    sqr = reverse(sqr)
    sqr = move(sqr)
    merge(sqr)
    sqr = move(sqr)
    sqr = reverse(sqr)
    add_new(sqr)

def move_up():
    global sqr
    sqr = transverse(sqr)
    sqr = move(sqr)
    merge(sqr)
    sqr = move(sqr)
    sqr = transverse(sqr)
    add_new(sqr)


def score(stps):
    score = 0 
    for u in range(4):
        for v in range(4):
            score += sqr[u][v]
    return score - stps


def score_print(stps):
    font = pygame.font.Font('freesansbold.ttf',32)
    scor_prnt = font.render("Score : " +str(score(stps)),True,white)
    scrn.blit(scor_prnt,(20,20))

def game_over():
    font = pygame.font.Font('freesansbold.ttf',32)
    scor_prnt = font.render("GAME OVER",True,white)
    scrn.blit(scor_prnt,(250,500))

def winner():
    font = pygame.font.Font('freesansbold.ttf',32)
    scor_prnt = font.render("YOU WIN",True,white)
    scrn.blit(scor_prnt,(250,500))

def heading():
    font = pygame.font.Font('freesansbold.ttf',40)
    scor_prnt = font.render("2048 Game",True,white)
    scrn.blit(scor_prnt,(200,100))

def fill_color(u,v,x,y):
    if sqr[u][v] == 0:
        img = pygame.image.load('0_color.png')
        scrn.blit(img,(x,y))
    elif sqr[u][v] == 2:
        img = pygame.image.load('2_color.jpg')
        scrn.blit(img,(x,y))
    elif sqr[u][v] == 4:
        img = pygame.image.load('4_color.jpg')
        scrn.blit(img,(x,y))
    elif sqr[u][v] == 8:
        img = pygame.image.load('8_color.jpg')
        scrn.blit(img,(x,y))
    elif sqr[u][v] == 16:
        img = pygame.image.load('16_color.jpg')
        scrn.blit(img,(x,y))
    elif sqr[u][v] == 32:
        img = pygame.image.load('32_color.png')
        scrn.blit(img,(x,y))
    elif sqr[u][v] == 64:
        img = pygame.image.load('64_color.png')
        scrn.blit(img,(x,y))
    elif sqr[u][v] == 128:
        img = pygame.image.load('128_color.png')
        scrn.blit(img,(x,y))
    elif sqr[u][v] == 256:
        img = pygame.image.load('256_color.png')
        scrn.blit(img,(x,y))
    elif sqr[u][v] == 512:
       img = pygame.image.load('512_color.png')
       scrn.blit(img,(x,y))
    elif sqr[u][v] == 1024:
       img = pygame.image.load('1024_color.png')
       scrn.blit(img,(x,y))
    else:
       img = pygame.image.load('2048_color.png')
       scrn.blit(img,(x,y))



black = (0,0,0)
white = (255,255,255)
def grid_rect():
    rect_y = 100
    for u in range(0,4):
        rect_y += 70
        rect_x = 170
        for v in range(0,4):
            rect = pygame.Rect(rect_x,rect_y,70,70)
            pygame.draw.rect(scrn,black,rect,border_radius=1)
            #print number
            fill_color(u,v,rect_x,rect_y)
            if sqr[u][v] >= 99:
                f = pygame.font.Font('freesansbold.ttf',25)
                nu_prn = f.render(str(sqr[u][v]),True,black)
                x = rect_x + 15
                y = rect_y + 25
            if sqr[u][v] >= 999:
                f = pygame.font.Font('freesansbold.ttf',20)
                nu_prn = f.render(str(sqr[u][v]),True,black)
                x = rect_x + 10
                y = rect_y + 28
            if sqr[u][v] <= 99:
                nu_prn = font.render(str(sqr[u][v]),True,black)
                x = rect_x + 25
                y = rect_y + 25
            scrn.blit(nu_prn,(x,y))
            rect_x += 70
            

running = True
steps = 0
while running:
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            running = False
        if evnt.type == pygame.KEYDOWN:
            if evnt.key == pygame.K_UP:
                move_up()
                steps += 1
            if evnt.key == pygame.K_DOWN:
                move_down()
                steps += 1
            if evnt.key == pygame.K_LEFT:
                move_left()
                steps += 1
            if evnt.key == pygame.K_RIGHT:
                move_right()
                steps += 1

            

    scrn.fill((0,0,0))
    scrn.blit(back_img,(0,0))
    grid_rect()
    heading()
    score_print(steps)
    if win_check(sqr):
        winner()
        
    elif game_over_check(sqr):
        game_over()
        break


    pygame.display.update()