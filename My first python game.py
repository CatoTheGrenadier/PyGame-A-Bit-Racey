import pygame
import random

pygame.init()

display_width=800
display_height=600

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

bright_red=(150,0,0)
bright_blue=(0,0,150)

car_width=73

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("A bit Racey")
clock=pygame.time.Clock()

carimg=pygame.image.load("C:\\Users\\Clementine\\Desktop\\Projects\\PyGame A Bit Racey\\racecar.png")

pygame.display.set_icon(carimg)

pause = False

def things_dodged(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Dodged"+" "+str(count),True, black)
    gameDisplay.blit(text,(10,10))

def hint():
    font = pygame.font.SysFont(None,25)
    text = font.render("Press 'P' to pause",True, black)
    gameDisplay.blit(text,(600,10))

def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def car(x,y):
    gameDisplay.blit(carimg,(x,y))

def text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def crash():
    largeText = pygame.font.Font("C:\\Users\\Clementine\\Desktop\\Projects\\PyGame A Bit Racey\\FreeSansBold.ttf",115)
    TextSurf, TextRect = text_objects("You Crashed",largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("PLAY AGAIN",325,400,175,50,blue,bright_blue,"play")
        button("BACK TO MENU",325,500,175,50,red,bright_red,"back")

        pygame.display.update()
        clock.tick(30)

def unpause():
    global pause
    pause = False

def action(text):
    if text == "play":
        game_loop()
    elif text == "back":
        unpause()
        game_intro()
    elif text == "quit":
        pygame.quit()
        quit()
    elif text == "continue":
        unpause()

def button(msg,x,y,w,h,ic,ac,text = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0] == 1 and text != None:
            action(text)
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
        
    smallText = pygame.font.Font("C:\\Users\\Clementine\\Desktop\\Projects\\PyGame A Bit Racey\\FreeSansBold.ttf",20)
    TextSurf,TextRect = text_objects(msg,smallText)
    TextRect.center = ((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(TextSurf,TextRect)

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        gameDisplay.fill(white)
        largeText = pygame.font.Font("C:\\Users\\Clementine\\Desktop\\Projects\\PyGame A Bit Racey\\FreeSansBold.ttf",115)
        TextSurf, TextRect = text_objects("A Bit Racey",largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf,TextRect)

        button("PLAY",150,450,100,50,blue,bright_blue,"play")
        button("QUIT",550,450,100,50,red,bright_red,"quit")

        pygame.display.update()
        clock.tick(30)

def paused():
    global pause
    pause = True

    while pause:
        
        
        largeText = pygame.font.Font("C:\\Users\\Clementine\\Desktop\\Projects\\PyGame A Bit Racey\\FreeSansBold.ttf",115)
        TextSurf, TextRect = text_objects("Paused",largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf,TextRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("CONTINUE",325,400,175,50,blue,bright_blue,"continue")
        button("BACK TO MENU",325,500,175,50,red,bright_red,"back")

        pygame.display.update()
        clock.tick(30)

def game_loop():
    global pause

    x=(display_width*0.45)
    y=(display_height*0.8)

    x_change=0
    
    thing_width = 100
    thing_startx = random.randrange(0,display_width-thing_width)
    thing_starty = -600
    thing_speed = 7
    thing_height = 100

    dodged = 0

    blockcolor=(0,0,0)

    gameExit=False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_p:
                    pause = True
                    paused()
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        
        if 0<=x+x_change<=display_width-car_width:
            x+=x_change
        
        gameDisplay.fill(white)

        things(thing_startx,thing_starty,thing_width,thing_height,blockcolor)
        thing_starty += thing_speed
        car(x,y) 
        things_dodged(dodged)
        hint()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width-thing_width)
            dodged += 1
            if thing_speed<=10:
                thing_speed+=0.5
            blockred=random.randrange(0,255)
            blockgreen=random.randrange(0,255)
            blockblue=random.randrange(0,255)
            blockcolor=(blockred,blockgreen,blockblue)
        
        
        if y < thing_starty + thing_height:
            if not (x >= thing_startx + thing_width or x + car_width <= thing_startx):
                crash()
        
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()

