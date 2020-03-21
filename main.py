import pygame as pg
import random
import math
from pygame import mixer
pg.init()
width=800
height=600
window=pg.display.set_mode((width,height))      #To set main screen weidtth and height
pg.display.set_caption("IronMissile")     #to set title of game
score=0
icon = pg.image.load('blood.png') #favicon of game
pg.display.set_icon(icon)   #to display the favicon
background=pg.image.load('lp.png')
mixer.music.load('background.wav')
mixer.music.play(-1)
#Player
playerimg =pg.image.load('iman.png')      # player image
playerx=370         #player x cordinate
playery=480         #player y cordinate
changeX=0

enemyimg =[]      # player image
enemyX=[]         #player x cordinate
enemyy=[]        #player y cordinate
enemychangeX=[]
enemychangeY=[]
number_of_enemy=5
for i in range(number_of_enemy):
    enemyimg.append(pg.image.load('skull.png'))     # player image
    enemyX.append(random.randint(0,800))      #player x cordinate
    enemyy.append(random.randint(15,150))        #player y cordinate
    enemychangeX.append(3)              #speed of enemy movement
    enemychangeY.append(80)
#Bullet
bullet=pg.image.load('bullet.png')
bulletX=0         #player x cordinate
bullety=480        #player y cordinate
bulletX_change=0
bulletY_change= 10
state="ready"        #state where bullet is not sooting
#
enemyImg=[]
font=pg.font.Font('freesansbold.ttf',35)
textx=10
texty=10

def show_score(x,y):
    scr=font.render('Score: '+ str(score),True,(255,255,255))
    window.blit(scr,(x,y))

def player(x,y):
    '''
    to draw player on screen
    '''
    window.blit(playerimg,(x,y))        #to display player image with its axis
def enemy(x,y,i):
    '''
    to draw player on screen
    '''
    window.blit(enemyimg[i],(x,y))        #to display player image with its axis

def fire_bullet(x,y):
    global state
    state="fire"
    window.blit(bullet,(x+16,y+16))
def collsioin(ex,ey,bx,by):
    d=math.sqrt((math.pow(ex-bx,2))+ (math.pow(ey-by,2)))
    if d< 27:
        return True
    else:
        return False
over_font=pg.font.Font('freesansbold.ttf',55)
def game_over():
        ovr=over_font.render("Game Over",True,(255,255,255))
        window.blit(ovr,(200,250))


def main():
    '''
    The main fuction that keeps our game running
    '''
    global score
    global state
    global bullety
    global bulletX
    global enemyX
    global enemyy
    global changeX
    global playerx
    #Game Infinite loop to keep the game window open till user exits manually
    running= True
    while running:

        window.fill((0,25,25))         #to fill color in screen
        window.blit(background,(0,0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                '''when user press exit button'''
                running=False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    changeX=-10

                if event.key == pg.K_RIGHT:
                    changeX=10

                if event.key ==pg.K_SPACE:
                    if state is "ready":
                        bullet_sound=mixer.Sound('laser.wav')
                        bullet_sound.play()

                        bulletX=playerx #et the current X cordinate of player

                        fire_bullet(bulletX,bullety)    #sotting bullet
            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                    changeX=0

        if bullety<=0:
            bullety=480
            state="ready"
        # Bullet Moveent
        if state is "fire":

            fire_bullet(bulletX,bullety)    #fire bullet from player
            bullety-=10
        playerx+=changeX
        if playerx <=0:
            playerx=0       #left side boundry case
        elif playerx >= 736:
            playerx = 736   #right side boundry case
        for i in range(5):
            if enemyy[i] > 440:
                for j in range(5):
                    enemyy[j]=2000
                game_over()
                break

            enemyX[i]+=enemychangeX[i]
            if enemyX[i] <=0:
                enemyX[i]=4      #left side boundry case
                enemyy[i]=enemyy[i]+40    #update after hitting the boundray
            elif enemyX[i] >= 736:
                enemyX[i] = -100   #right side boundry case
                enemyy[i]=enemyy[i]+40    #update after hitting the boundray

            collision=collsioin(enemyX[i],enemyy[i],bulletX,bullety)
            if collision:
                bullety=480
                state="ready"
                score+=1
                explosion_sound=mixer.Sound('explosion.wav')
                explosion_sound.play()
                enemyX[i]=random.randint(0,735)
                enemyy[i]=random.randint(50,150)
            enemy(enemyX[i],enemyy[i],i)
        player(playerx,playery)     #update player position
        show_score(textx,texty)
        pg.display.update()         #to update the display position


main()
#Tell me about yourself
