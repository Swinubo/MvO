import pygame, pyautogui, pathlib, os, random, divrounder

pygame.init()

pygame.display.set_caption("MvO")

X, Y = pyautogui.size()
scrn = pygame.display.set_mode((X, Y))

current_dir = os.getcwd()
image_path = pathlib.Path(current_dir, 'MvO Images')

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (0, 128,   0)
PURPLE = (134, 19, 144)
YELLOW = (212, 195, 27)
BLUE = (0, 191, 255)

M_IMAGE_SIZE = (100, 100)
O_IMAGE_SIZE = (200, 100)
SMALL_IMAGE_SIZE = (50, 50)
M = pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, "M.png"))).convert_alpha(), M_IMAGE_SIZE) #Loads cf montreal logo
O = pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, "O.png"))).convert_alpha(), O_IMAGE_SIZE) #Loads orlando sc logo
Ball = pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, "Ball.png"))).convert_alpha(), SMALL_IMAGE_SIZE) #Loads ball
ExitDispl = pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, "Exit.png"))).convert(), SMALL_IMAGE_SIZE) #Loads exit
ResetDispl = pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, "Reset.png"))).convert_alpha(), SMALL_IMAGE_SIZE) #Loads exit

def DisplScrn(O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown):
    scrn.fill(GREEN)
    pygame.draw.rect(scrn, BLACK, pygame.Rect(50, 150, 300, 700))
    pygame.draw.rect(scrn, GREEN, pygame.Rect(60, 160, 280, 680))
    pygame.draw.rect(scrn, BLACK, pygame.Rect(1550, 150, 300, 700))
    pygame.draw.rect(scrn, GREEN, pygame.Rect(1560, 160, 280, 680))
    pygame.draw.rect(scrn, BLACK, pygame.Rect(0, 290, 100, 420))
    pygame.draw.rect(scrn, BLACK, pygame.Rect(1820, 290, 120, 420))
    pygame.draw.rect(scrn, WHITE, pygame.Rect(0, 300, 100, 400))
    pygame.draw.rect(scrn, WHITE, pygame.Rect(1820, 300, 100, 400))
    pygame.draw.circle(scrn, BLACK, (960, 500), 150)
    pygame.draw.circle(scrn, GREEN, (960, 500), 140)
    pygame.draw.rect(scrn, BLACK, pygame.Rect(960, 0, 10, 1500))
    scrn.blit(M, (M_X, M_Y))
#    if (OutOLeft == True) or (OutORight == True) or (OutOUp == True) or (OutODown == True):
#        O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown = CheckODirection(O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown)
    scrn.blit(O, (O_X, O_Y))
    scrn.blit(Ball, (BallX, BallY))
    scrn.blit(ExitDispl, (1870, 0))
    scrn.blit(ResetDispl, (1800, 0))
    scrn.blit(font.render(str(MScore), True, BLACK),(800, 0))
    scrn.blit(font.render(str(OScore), True, BLACK),(1100, 0))
    pygame.display.flip()
    return O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown

def CheckInNet(MScore, OScore, BallX, BallY, M_X, M_Y, O_X, O_Y):
    if BallX < 100:
        OScore += 1
        M_X, M_Y, O_X, O_Y, BallX, BallY = 500, 500, 700, 700, 940, 480
    if BallX > 1820:
        MScore += 1
        M_X, M_Y, O_X, O_Y, BallX, BallY = 500, 500, 700, 700, 940, 480
    return MScore, OScore, M_X, M_Y, O_X, O_Y, BallX, BallY

def CheckODirection(O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown):
    if (OutOLeft== True) and (OutORight== True) and (OutOUp== True) and (OutODown== True):
        DirectionsList = ['Left', 'Right', 'Up', 'Down']
        direction = random.choice(DirectionsList)
        if direction == 'Left':
            OutOLeft = False
        elif direction == 'Right':
            OutORight = False
        elif direction == 'Up':
            OutOUp = False
        elif direction == 'Down':
            OutODown = False
    return O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown

            

font = pygame.font.SysFont('Comic Sans M',  150)
M_X, M_Y, O_X, O_Y, BallX, BallY = 500, 500, 700, 700, 940, 480
FPS = 60
MScore, OScore = 0, 0
OutOLeft, OutORight, OutOUp, OutODown = True, True, True, True
clock = pygame.time.Clock()
done = False

while not done:
    O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown = CheckODirection(O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown)
    if OutOLeft == False:
        O_X -= 20
        if O_X < 0:
            O_X = 0
            OutOLeft = True
    elif OutORight == False:
        O_X += 20
        if O_X > 1720:
            O_X = 1720
            OutORight = True
    elif OutOUp == False:
        O_Y -= 20
        if O_Y < 0:
            O_Y = 0
            OutOUp = True
    elif OutODown == False:
        O_Y += 20
        if O_Y > 920:
            O_Y = 920
            OutODown = True
    O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown = DisplScrn(O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x, y = event.pos
            if ((x < 1920) and (x > 1870) and (y < 50) and (y > 0)):
                pygame.quit()
                quit()
            if ((x < 1850) and (x > 1800) and (y < 50) and (y > 0)):
                M_X, M_Y, O_X, O_Y, BallX, BallY = 500, 500, 700, 700, 940, 480
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if event.key == pygame.K_LEFT:
                OutLeft = False
                while OutLeft == False:
                    M_X -= 20
                    if M_X < 0:
                        M_X = 0
                    if (M_X == BallX) and ((M_Y + 100 > BallY) and (M_Y - 50 < BallY)):
                        BallX -= 20
                        MScore, OScore, M_X, M_Y, O_X, O_Y, BallX, BallY = CheckInNet(MScore, OScore, BallX, BallY, M_X, M_Y, O_X, O_Y)
                    O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown = DisplScrn(O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown)
                    for event in pygame.event.get():
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_LEFT:
                                OutLeft = True
                    clock.tick(FPS)
            elif event.key == pygame.K_RIGHT:
                OutRight = False
                while OutRight == False:
                    M_X += 20
                    if M_X > 1820:
                        M_X = 1820
                    if (M_X == BallX) and ((M_Y + 100 > BallY) and (M_Y - 50 < BallY)):
                        BallX += 20
                        MScore, OScore, M_X, M_Y, O_X, O_Y, BallX, BallY = CheckInNet(MScore, OScore, BallX, BallY, M_X, M_Y, O_X, O_Y)
                    O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown = DisplScrn(O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown)
                    for event in pygame.event.get():
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_RIGHT:
                                OutRight = True
                    clock.tick(FPS)
            elif event.key == pygame.K_UP:
                OutUp = False
                while OutUp == False:
                    M_Y -= 20
                    if M_Y < 0:
                        M_Y = 0
                    if (M_Y == BallY) and ((M_X + 100 > BallX) and (M_X - 50 < BallX)):
                        BallY -= 20
                    O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown = DisplScrn(O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown)
                    for event in pygame.event.get():
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_UP:
                                OutUp = True
                    clock.tick(FPS)
            elif event.key == pygame.K_DOWN:
                OutDown = False
                while OutDown == False:
                    M_Y += 20
                    if M_Y > 980:
                        M_Y = 980
                    if (M_Y == BallY) and ((M_X + 100 > BallX) and (M_X - 50 < BallX)):
                        BallY += 20
                    O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown = DisplScrn(O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown)
                    for event in pygame.event.get():
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_DOWN:
                                OutDown = True
                    clock.tick(FPS)
            elif event.key == pygame.K_SPACE:
                if (M_X + 20 == BallX) and ((M_Y + 100 > BallY) and (M_Y - 50 < BallY)):
                    Powering = True
                    SecondsPassed = 0
                    while Powering == True:
                        SecondsPassed += 1/FPS
                        for event in pygame.event.get():
                            if event.type == pygame.KEYUP:
                                if event.key == pygame.K_SPACE:
                                    Powering = False
                        clock.tick(FPS)
                    OutShot = False
                    try:
                        RandomLimit = random.randint(M_X, 1920)
                    except ValueError:
                        OutShot = True
                    while OutShot == False:
                        BallX += 27 * SecondsPassed
                        O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown = DisplScrn(O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown)     
                        clock.tick(FPS)
                        if BallX > RandomLimit:
                            OutShot = True
                            BallX = divrounder.divround(BallX, 20)
                            MScore, OScore, M_X, M_Y, O_X, O_Y, BallX, BallY = CheckInNet(MScore, OScore, BallX, BallY, M_X, M_Y, O_X, O_Y)
            elif keys[pygame.K_SPACE] and keys[pygame.K_LSHIFT]:
                if (M_X + 20 == BallX) and ((M_Y + 100 > BallY) and (M_Y - 50 < BallY)):
                    Powering = True
                    SecondsPassed = 0
                    while Powering == True:
                        SecondsPassed += 1/FPS
                        for event in pygame.event.get():
                            if event.type == pygame.KEYUP:
                                if event.key == pygame.K_SPACE:
                                    Powering = False
                        clock.tick(FPS)
                    
                    try:
                        RandomLimit = random.randint(M_X, 1920)
                    except ValueError:
                        OutShot = True
                    
                    K = BallX * BallY
                    OutShot = False

                    while OutShot == False:
                        BallX += 27 * SecondsPassed
                        BallY = K/BallX
                        O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown = DisplScrn(O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown)     
                        clock.tick(FPS)
                        if BallX > RandomLimit:
                            OutShot = True
                            BallX = divrounder.divround(BallX, 20)
                            BallY = divrounder.divround(BallY, 20)
                            MScore, OScore, M_X, M_Y, O_X, O_Y, BallX, BallY = CheckInNet(MScore, OScore, BallX, BallY, M_X, M_Y, O_X, O_Y)
    clock.tick(FPS)