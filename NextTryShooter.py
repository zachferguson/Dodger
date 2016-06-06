import pygame
import time
import random

pygame.init()
display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
#thing_width = 100
#thing_height = 100
ast_width = 55
ast_height = 54
ast_startx = random.randrange(0, display_width)
ast_starty = -600
ship_width = 77

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Shooter')
clock = pygame.time.Clock()

shipImg = pygame.image.load('AlienFighter1.png')
astImg = pygame.image.load('Asteroid.png')

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


#def things(thingx, thingy, thingw, thingh, color):
#   pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def asteroid(ast_startx, ast_starty):
    gameDisplay.blit(astImg, (ast_startx, ast_starty))


def ship(x, y):
    gameDisplay.blit(shipImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width * 0.5), (display_height * 0.5))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)
    game_loop()


def crash():
    message_display('You died.')


def game_loop():
    global ast_startx
    global ast_starty
    x = (display_width * 0.45)
    y = (display_height * .84)

    x_change = 0
    ast_startx = random.randrange(0, display_width)
    ast_starty = -600
    ast_speed = 7
    #thing_startx = random.randrange(0, display_width)
    #thing_starty = -600
    #thing_speed = 7
    #thing_width = 100
    #thing_height = 100
    dodged = 0

    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -9
                elif event.key == pygame.K_RIGHT:
                    x_change = 9

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0


        x += x_change
        gameDisplay.fill(white)

        #                       things(thingx, thingy, thingw, thingh, color)
        #things(thing_startx, thing_starty, thing_width, thing_height, black)
        #thing_starty += thing_speed
        asteroid(ast_startx, ast_starty)
        ast_starty += ast_speed
        ship(x, y)
        things_dodged(dodged)

        if x > display_width - ship_width or x < 0:
            crash()
        #if thing_starty > display_height:
        #    thing_starty = 0 - thing_height
        #    thing_startx = random.randrange(0, display_width)
        #    dodged += 1
        #    thing_speed += 0.5

        if ast_starty > display_height:
            ast_starty = 0 - ast_height
            ast_startx = random.randrange(0, display_width)
            dodged += 1
            ast_speed += 0.5

        #if y < thing_starty + thing_height:
        #    print('Y vertical crossover')
        #    if x > thing_startx and x < thing_startx + thing_width or x + ship_width > thing_startx and x + ship_width < thing_startx + thing_width:
        #        print('X horizontal crossover.')
        #        crash()

        if y < ast_starty + ast_height:
            print('Y vertical crossover')
            if x > ast_startx and x < ast_startx + ast_width or x + ship_width > ast_startx and x + ship_width < ast_startx + ast_width:
                print('X horizontal crossover.')
                crash()

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()