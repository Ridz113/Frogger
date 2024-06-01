from pygame import *
import random

init()

# define global variables
width = 1440
height = 900
screen = display.set_mode((width, height))
main_font = font.SysFont("comicsans", 40)
main_font2 = font.SysFont("comicsans", 200)
lives = 3
count = 0
car_spawn = random.randint(1,2)
clock = time.Clock()
onlog = 0
clock = time.Clock()
black = (0, 0, 0)

red = (200, 0, 0)

bright_red = (255, 0, 0)

white = (255, 255, 255)

green = (0, 200, 0)

bright_green = (0, 255, 0)

#sounds

death_sound = mixer.Sound("kachow.wav")
theme = mixer.Sound("theme.wav")
theme.set_volume(0.5)
dead = mixer.Sound("death.wav")
dead.set_volume(0.5)

# frog globals
froggerImage = image.load("kermit.xcf")
froggerImage = transform.scale(froggerImage,(80,60))
x = 600
y = 690
frog = Rect(x, y, froggerImage.get_width(), froggerImage.get_height())
px = 0
py = 0

# car globals
carImage = image.load("car.xcf")
carImage = transform.scale(carImage,(100,50))
carList = []

#log globals
logImage = image.load("log.png")
logImage = transform.scale(logImage,(150,50))
logList = []

# background globals
backgroundimg = image.load("frogger_background.gif")
backgroundimg = transform.scale(backgroundimg, (width, height - 150))

main_menu_background = image.load("mainmenu.jpg")

death = image.load("death.jpg")
death = transform.scale(death, (width, height))

class carRecord():
    carRect = None
    carSpeed = 0


car1 = carRecord()
car2 = carRecord()
car3 = carRecord()
car4 = carRecord()

# cars
# TASK 3 - Add more cars!


car1.carRect = Rect(0,425,carImage.get_width(), carImage.get_height())
car1.carSpeed = 27
car2.carRect = Rect(width - 200,500,carImage.get_width(), carImage.get_height())
car2.carSpeed = -24
car3.carRect = Rect(0,575,carImage.get_width(), carImage.get_height())
car3.carSpeed = 26
car4.carRect = Rect(width - 100,640,carImage.get_width(), carImage.get_height())
car4.carSpeed = -21

carList.append(car1)
carList.append(car2)
carList.append(car3)
carList.append(car4)

class logRecord():
    logRect = None
    logSpeed = 0


log1 = logRecord()
log2 = logRecord()
log3 = logRecord()
log4 = logRecord()

log1.logRect = Rect(0,120,logImage.get_width(), logImage.get_height())
log2.logRect = Rect(width - 100,185,logImage.get_width(), logImage.get_height())
log3.logRect = Rect(0,250,logImage.get_width(), logImage.get_height())
log4.logRect = Rect(width - 100,315,logImage.get_width(), logImage.get_height())


log1.logSpeed = random.randint(10,15)
log2.logSpeed = random.randint(5,10) * -1
log3.logSpeed = random.randint(5,10)
log4.logSpeed = random.randint(10,15) * -1

logList.append(log1)
logList.append(log2)
logList.append(log3)
logList.append(log4)




''' 
def createCars(count):
    cx = 0
    cy = 250

    while count <= 3:

        car1.carRect = Rect(cx, cy, carImage.get_width(), carImage.get_height())
        car1.carSpeed = 4
        carList.append(car1)

        cy = cy + 60

        count = count + 1



    return carList

cars = createCars(count)  # calls function
'''



# TASK 1 draw the background function!
# define functions
def text_objects(text, font):
    textSurface = font.render(text, True, black)

    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)

    TextSurf, TextRect = text_objects(text, largeText)

    TextRect.center = ((width / 2), (height / 2))

    screen.blit(TextSurface, TextRect)

    screen.update()

def button(msg, x, y, w, h, ic, ac, action=None):
    m = mouse.get_pos()


    click = mouse.get_pressed()

    if x + w > m[0] > x and y + h > m[1] > y:

        draw.rect(screen, ac, (x, y, w, h))

        if click[0] == 1 and action != None:

            action()

            if action == "play":

                game_loop()


            elif action == "quit":

                quit()

    else:

        draw.rect(screen, ic, (x, y, w, h))

    smallText = font.Font("freesansbold.ttf", 20)

    textSurf, textRect = text_objects(msg, smallText)

    textRect.center = ((x + (w / 2)), (y + (h / 2)))

    screen.blit(textSurf, textRect)


# Functions - pause/ un pause, credit to sentdex for tutorial

pause = False


def unpause():
    global pause

    pause = False


def paused():


    while pause:

        for e in event.get():

            if e.type == QUIT:
                quitgame()


        pause_label = main_font2.render("PAUSED", 1, (white))

        screen.blit(pause_label, (475, 250))

        button("CONTINUE?", 325, 450, 150, 50, green, bright_green, unpause)

        button("RAGE QUIT", 1025, 450, 120, 50, red, bright_red, "quit")

        display.update()



# ------------------------------------------------------------------------------------------


#  Function for main menu, Credit to Harsh for helping me with this , and credit to sentdex for tutorial


def game_intro():
    intro = True

    while intro:

        for e in event.get():

            if e.type == QUIT:
                quitgame()

        screen.blit(main_menu_background, (0, 0))

        main_font = font.SysFont("comicsans", 40)

        largeText = font.Font('freesansbold.ttf', 115)


        TextSurf, TextRect = text_objects("Kermits Escape", largeText)
        TextRect.center = (700, 125)
        screen.blit(TextSurf, TextRect)


        TextSurf, TextRect = text_objects("Controls:", main_font)
        TextRect.center = (425, 525)
        screen.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(" P - Pause", main_font)
        TextRect.center = (425, 575)
        screen.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Left/Right/Up/Down arrow keys - move", main_font)
        TextRect.center = (425, 625)
        screen.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Rules:", main_font)
        TextRect.center = (1000, 525)
        screen.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("- Make it to end to win!", main_font)
        TextRect.center = (1000, 575)
        screen.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("- Get hit by a car and you lose a life", main_font)
        TextRect.center = (1000, 625)
        screen.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("- Lose all lives and Kermit Dies", main_font)
        TextRect.center = (1000, 675)
        screen.blit(TextSurf, TextRect)

        button("PLAY", 350, 225, 200, 100, green, bright_green, game_loop)

        button("QUIT", 850, 225, 200, 100, red, bright_red, quit)

        display.update()

        clock.tick(60)

# Function for a game over, when you lose all lives.
def game_over():
    theme.stop()
    death_sound.stop()
    dead.play()
    screen.blit(death, (0,0))


    gameover_label = main_font2.render("YOU ARE DEAD", 1, (white))

    screen.blit(gameover_label, (250, 250))

    while True:

        for e in event.get():

            if e.type == QUIT:
                quitgame()

        button("PLAY AGAIN?", 150, 450, 150, 50, green, bright_green, game_loop)

        button("RAGE QUIT", 850, 450, 120, 50, red, bright_red, "quit")

        display.update()

        clock.tick(15)

def win():
    theme.stop()
    win_label = main_font2.render("YOU WIN", 1, (green))

    screen.blit(win_label, (250, 250))

    while True:

        for e in event.get():

            if e.type == QUIT:
                quitgame()

        button("PLAY AGAIN?", 150, 450, 150, 50, green, bright_green, game_loop)

        button("QUIT", 850, 450, 100, 50, red, bright_red, "quit")

        display.update()

        clock.tick(15)
# function to quit the game


def quitgame():
    quit()


def drawBackground():
    global screen, backgroundimg
    screen.fill((0, 0, 0))
    screen.blit(backgroundimg, (0,0))



# draw your background as you wish!

def drawPlayer():
    global screen, frog, froggerImage
    screen.blit(froggerImage, frog)


def moveFrog():
    global px,py, frog, width
    if frog.x + px > -10 and frog.x + frog.w + px < width - 20 and frog.y + py > 0 and frog.y + frog.h + py < height - 147:
        frog.move_ip(px,py)



# TASK 2 draw cars
def drawCars():
    global screen, carList, carImage

    for c in carList:
        screen.blit(carImage, c.carRect)




# TASK 4 - Move the cars. If they go off the screen then wrap them.
# car width = 100

def moveCars():
    global carList, carImage
    for c in carList:
        c.carRect.move_ip(c.carSpeed,0)

        if c.carRect.x >= 1640:
            c.carRect.x = 1540
            carImage = transform.flip(carImage, True, False)
            c.carSpeed = random.randint(20, 30)
            c.carSpeed = c.carSpeed * -1

        if c.carRect.x <= -200:
            c.carRect.x = -100
            carImage = transform.flip(carImage, True, False)
            c.carSpeed = c.carSpeed * -1

def drawlogs():
    global screen, logList, logImage

    for l in logList:
        screen.blit(logImage, l.logRect)

def movelogs():
    # log width = 150
    global logList, logImage
    for l in logList:
        l.logRect.move_ip(l.logSpeed,0)

        if l.logRect.x >= 1740:
            l.logRect.x = 1590
            l.logSpeed = random.randint(5, 15)
            l.logSpeed = l.logSpeed * -1


        if l.logRect.x <= -300:
            l.logRect.x = -150
            l.logSpeed = l.logSpeed * -1



def draw_lives():
    global lives

    lives_label = main_font.render(f"LIVES: {lives}", 1, (bright_red))

    screen.blit(lives_label, (0, 825))

    display.flip()

def colliderect(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.overlap(obj2, (offset_x,offset_y)) != None

def game_loop():

    gameOver = False
    theme.play()

    global px, py, pause

    while not gameOver:
        for e in event.get():
            # task 5 - Make frogger move up and down.
            if e.type == QUIT:
                gameOver = True


            elif e.type == KEYDOWN:


                if e.key == K_LEFT and frog.x + px > -10:
                    frog.x -= 60
                elif e.key == K_RIGHT and frog.x + frog.w + px < width - 20:
                    frog. x += 60
                elif e.key == K_DOWN and frog.y + py > 0:
                    frog.y += 65
                elif e.key == K_UP and frog.y + frog.h + py < height - 147:
                    frog.y -= 65
                elif e.key == K_p:
                    pause = True

                    paused()

            elif e.type == KEYUP:
                if e.key == K_LEFT or e.key == K_RIGHT or e.key == K_DOWN or e.key == K_UP:
                    px = 0
                    py = 0

            # removes diagnol movement
            if (py == 3 and px == 3) or (py == -3 and px == -3) or (py == 3 and px == -3) or (py == -3 and px == 3):
                py = 0
                px = 0

        m = mouse.get_pos()
        print(m)



        # TASK 6 - Make a more polished frogger game :)

        # movement
        moveFrog()
        moveCars()

        # game mechanics
        global lives
        for c in carList:
            if c.carRect.colliderect(frog):
                drawPlayer()
                frog.x = x
                frog.y = y
                lives -= 1
                death_sound.play()

        global onlog, count

        # on log

        for l in logList:
            count += 1
            if l.logRect.colliderect(frog) == 1:
                px = l.logSpeed
                count = 0

            if l.logRect.colliderect(frog) == 1 and frog.x > width or frog.x < 0:
                lives = lives - 1
                frog.x = x
                frog.y = y


        #drowning
            if l.logRect.colliderect(frog) == 0 and count == 7:
                px = 0
                count = 0

            if frog.y < 355 and l.logRect.colliderect(frog) == 0 and count == 6:
                lives-= 1
                frog.x = x
                frog.y = y
                count = 0


            print(count)

        if lives <= 0:
            lives = 0
            drawCars()
            lives = 3
            game_over()

        if frog.y > 750:
            frog.x = x
            frog.y = y

        if frog.y < 70:
            win()



        # drawing
        drawBackground()
        drawlogs()
        movelogs()
        drawPlayer()
        drawCars()
        draw_lives()
        # show the newly drawn screen (double buffering)
        display.flip()
        clock.tick(60)
        # short delay to slow down animation.
        time.delay(5)

game_intro()