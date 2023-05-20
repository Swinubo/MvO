import pygame, pyautogui, pathlib, os, random, divrounder, easygui, Pop
from tkinter.filedialog import askopenfilename

pygame.init()

pygame.display.set_caption("MvO")

X, Y = pyautogui.size()
scrn = pygame.display.set_mode((X, Y))

current_dir = os.getcwd()
image_path = pathlib.Path(current_dir, 'MvO Images')

pygame.mixer.music.load(str(pathlib.Path(image_path, "Alexandre Desplat - Courtyard Apocalypse.mp3")))
pygame.mixer.music.play()

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (0, 128,   0)
PURPLE = (134, 19, 144)
YELLOW = (212, 195, 27)
BLUE = (0, 191, 255)
DARKBLUE = (0, 0, 255)

M_IMAGE_SIZE = (100, 100)
O_IMAGE_SIZE = (200, 100)
SMALL_IMAGE_SIZE = (50, 50)
BIG_IMAGE_SIZE = (800, 800)
PLAY_IMAGE_SIZE = (428, 249)

M = pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, "M.png"))).convert_alpha(), M_IMAGE_SIZE) #Loads cf montreal logo
O = pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, "O.png"))).convert_alpha(), O_IMAGE_SIZE) #Loads orlando sc logo
Ball = pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, "Ball.png"))).convert_alpha(), SMALL_IMAGE_SIZE) #Loads ball
ExitDispl = pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, "Exit.png"))).convert(), SMALL_IMAGE_SIZE) #Loads exit
ResetDispl = pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, "Reset.png"))).convert_alpha(), SMALL_IMAGE_SIZE) #Loads reset
ChangeDispl = pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, "Change.png"))).convert_alpha(), SMALL_IMAGE_SIZE) #Loads change
NoMusicDispl = pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, "NoMusic.png"))).convert_alpha(), SMALL_IMAGE_SIZE) #Loads no music
MusicDispl = pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, "Music.png"))).convert_alpha(), SMALL_IMAGE_SIZE) #Loads music
PauseDispl = pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, "Pause.png"))).convert_alpha(), SMALL_IMAGE_SIZE) #Loads pause
PlayPauseDispl = pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, "Play.png"))).convert_alpha(), SMALL_IMAGE_SIZE) #Loads play
BotDispl = pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, "Bot.png"))).convert_alpha(), BIG_IMAGE_SIZE) #Loads bot image
TwoPlayersDispl = pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, "TwoPlayers.png"))).convert_alpha(), BIG_IMAGE_SIZE) #Loads twoplayers image
PlayDispl = pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, "Play.jpg"))).convert(), PLAY_IMAGE_SIZE) #Loads play image
HomeDispl = pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, "Home.png"))).convert(), SMALL_IMAGE_SIZE) #Loads home image

font = pygame.font.SysFont('Comic Sans M',  150)
smallfont = pygame.font.SysFont('lucidasanstypewriter',  50)
Home = smallfont.render('Home', True, BLACK)
Away = smallfont.render('Away', True, BLACK)

M_X, M_Y, O_X, O_Y, BallX, BallY = 500, 480, 1380, 480, 940, 480
FPS = 60
MScore, OScore = 0, 0
OutOLeft, OutORight, OutOUp, OutODown = True, True, True, True
TimePassed = 0
Music, Playing = 'On', True
MultiPlayer = False
M_x_change, M_y_change = 0, 0
clock = pygame.time.Clock()

def DisplMain(NumberOfRecs):
    scrn.fill(DARKBLUE)
    
    TopLeft_X = NumberOfRecs * 20 / 3

    for num in range(NumberOfRecs):
        rect = pygame.Rect(TopLeft_X, 100, X/NumberOfRecs, 700)
        pygame.draw.rect(scrn, PURPLE, rect)

        TopLeft_X += X/NumberOfRecs + NumberOfRecs * 20 / 3
    
    scrn.blit(BotDispl, (100, 250))
    scrn.blit(TwoPlayersDispl, (1100, 250))
    scrn.blit(PlayDispl, (800, 820))
    scrn.blit(ExitDispl, (1870, 0))

    pygame.display.flip()

def DisplScrn():
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
    scrn.blit(O, (O_X, O_Y))
    scrn.blit(Ball, (BallX, BallY))
    scrn.blit(HomeDispl, (1870, 0))
    scrn.blit(ResetDispl, (1800, 0))
    scrn.blit(font.render(str(MScore), True, BLACK),(800, 0))
    scrn.blit(font.render(str(OScore), True, BLACK),(1100, 0))
    scrn.blit(Home, (600, 100))
    scrn.blit(Away, (1250, 100))
    scrn.blit(ChangeDispl, (500, 100))
    scrn.blit(ChangeDispl, (1400, 100))
    scrn.blit(M, (600, 0))
    scrn.blit(O, (1200, 0))
    scrn.blit(font.render(str(round(TimePassed, 2)), True, WHITE), (840, 100))
    if Music == 'On':
        scrn.blit(NoMusicDispl, (1730, 0))
    else:
        scrn.blit(MusicDispl, (1730, 0))
    scrn.blit(PauseDispl, (1660, 0))
    pygame.display.flip()

def CheckInNet(MScore, OScore, BallX, BallY, M_X, M_Y, O_X, O_Y):
    if BallX < 100:
        OScore += 1
        M_X, M_Y, O_X, O_Y, BallX, BallY = 500, 480, 1380, 480, 940, 480
    if BallX > 1820:
        MScore += 1
        M_X, M_Y, O_X, O_Y, BallX, BallY = 500, 480, 1380, 480, 940, 480
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

def RandListGenerator(AmountOfNumbers, Min, Max):
    randomlist = []
    for i in range(0, AmountOfNumbers):
        num = random.randint(Min, Max)
        num = divrounder.divround(num, 20)
        randomlist.append(num)
    return randomlist

def PosOGenrater(M_X, M_Y, O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown, BallX, BallY, MScore, OScore):
    O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown = CheckODirection(O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown)
    RandLimitLeft = randomlistleft[random.randint(0, 99)]
    RandLimitRight = randomlistright[random.randint(0, 99)]
    RandLimitUp = randomlistup[random.randint(0, 99)]
    RandLimitDown = randomlistdown[random.randint(0, 99)]

    if OutOLeft == False:
        O_X -= 20
        if (O_X == BallX) and ((O_Y + 100 > BallY) and (O_Y - 50 < BallY)):
            BallX -= 20
            MScore, OScore, M_X, M_Y, O_X, O_Y, BallX, BallY = CheckInNet(MScore, OScore, BallX, BallY, M_X, M_Y, O_X, O_Y)
        if O_X < 0:
            O_X = 0
            OutOLeft = True
        if O_X < RandLimitLeft:
            O_X = divrounder.divround(O_X, 20)
            OutOLeft = True
    elif OutORight == False:
        O_X += 20
        if (O_X == BallX) and ((O_Y + 100 > BallY) and (O_Y - 50 < BallY)):
            BallX += 20
            MScore, OScore, M_X, M_Y, O_X, O_Y, BallX, BallY = CheckInNet(MScore, OScore, BallX, BallY, M_X, M_Y, O_X, O_Y)
        if O_X > 1820:
            O_X = 1820
            OutORight = True
        if O_X > RandLimitRight:
            O_X = divrounder.divround(O_X, 20)
            OutORight = True
    elif OutOUp == False:
        O_Y -= 20
        if (O_Y == BallY) and ((O_X + 100 > BallX) and (O_X - 50 < BallX)):
            BallY -= 20
        if O_Y < 0:
            O_Y = 0
            OutOUp = True
        if O_Y < RandLimitUp:
            O_Y = divrounder.divround(O_Y, 20)
            OutOUp = True
    elif OutODown == False:
        O_Y += 20
        if (O_Y == BallY) and ((O_X + 100 > BallX) and (O_X - 50 < BallX)):
            BallY += 20
        if O_Y > 920:
            O_Y = 920
            OutODown = True
        if O_Y > RandLimitDown:
            O_Y = divrounder.divround(O_Y, 20)
            OutODown = True
    return M_X, M_Y, O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown, BallX, BallY, MScore, OScore

randomlistleft = RandListGenerator(100, -1000, 1000)
randomlistright = RandListGenerator(100, 1000, 1820)
randomlistup = RandListGenerator(100, 0, 500)
randomlistdown = RandListGenerator(100, 500, 1020)

done = False
while not done:

    DisplMain(2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x, y = event.pos
            if ((x < 1920) and (x > 1870) and (y < 50) and (y > 0)):
                Pop.popper(900, 0.025)
                pygame.quit()
                quit()
            if ((x < 1230) and (x > 800) and (y < 1070) and (y > 820)):
                Pop.popper(900, 0.025)
                OutOfGame = False
                while OutOfGame == False:
                    TimePassed += 1/FPS
                    if TimePassed > 90:
                        if MScore > OScore:
                            Pop.popper(900, 0.025)
                            easygui.msgbox('The home team wins!', 'Woohoo!', 'Woohoo!', str(pathlib.Path(image_path, "Party Face Emoji.png")))
                            M_X, M_Y, O_X, O_Y, BallX, BallY = 500, 480, 1380, 480, 940, 480
                            TimePassed, MScore, OScore = 0, 0, 0
                        elif MScore < OScore:
                            Pop.popper(900, 0.025)
                            easygui.msgbox('The away team wins!', 'Boohoo!', 'Boohoo!', str(pathlib.Path(image_path, "Disappointed Face Emoji.png")))
                            M_X, M_Y, O_X, O_Y, BallX, BallY = 500, 480, 1380, 480, 940, 480
                            TimePassed, MScore, OScore = 0, 0, 0
                        elif MScore == OScore:
                            Pop.popper(900, 0.025)
                            easygui.msgbox("It's a draw!", ':/', ':/', str(pathlib.Path(image_path, "Neutral Face Emoji.png")))
                            M_X, M_Y, O_X, O_Y, BallX, BallY = 500, 480, 1380, 480, 940, 480
                            TimePassed, MScore, OScore = 0, 0, 0
                    if MultiPlayer == False:
                        M_X, M_Y, O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown, BallX, BallY, MScore, OScore = PosOGenrater(M_X, M_Y, O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown, BallX, BallY, 
                                                                                                                        MScore, OScore)

                    DisplScrn()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            done = True
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            # Set the x, y postions of the mouse click
                            x, y = event.pos
                            if ((x < 1920) and (x > 1870) and (y < 50) and (y > 0)):
                                Pop.popper(900, 0.025)
                                OutOfGame = True
                                M_X, M_Y, O_X, O_Y, BallX, BallY, Time, MScore, OScore = 500, 480, 1380, 480, 940, 480, 0, 0, 0
                            elif ((x < 1850) and (x > 1800) and (y < 50) and (y > 0)):
                                Pop.popper(900, 0.025)
                                M_X, M_Y, O_X, O_Y, BallX, BallY = 500, 480, 1380, 480, 940, 480
                                TimePassed, MScore, OScore = 0, 0, 0
                            elif ((x < 550) and (x > 500) and (y < 150) and (y > 100)):
                                Pop.popper(900, 0.025)
                                try:
                                    ImagePath = askopenfilename()
                                    if ImagePath != '':
                                        M = pygame.transform.scale((pygame.image.load(ImagePath)).convert_alpha(), M_IMAGE_SIZE) #Loads new logo
                                except pygame.error:
                                    easygui.msgbox("Unsupported image format!", "Alert")
                            elif ((x < 1450) and (x > 1400) and (y < 150) and (y > 100)):
                                Pop.popper(900, 0.025)
                                try:
                                    ImagePath = askopenfilename()
                                    if ImagePath != '':
                                        O = pygame.transform.scale((pygame.image.load(ImagePath)).convert_alpha(), M_IMAGE_SIZE) #Loads new logo
                                except pygame.error:
                                    easygui.msgbox("Unsupported image format!", "Alert")
                            elif ((x < 1780) and (x > 1730) and (y < 50) and (y > 0)):
                                Pop.popper(900, 0.025)
                                if Music == 'On':
                                    Music = 'Off'
                                    pygame.mixer.music.pause()
                                elif Music == 'Off':
                                    Music = 'On'
                                    pygame.mixer.music.unpause()
                            elif ((x < 1710) and (x > 1660) and (y < 50) and (y > 0)):
                                Pop.popper(900, 0.025)
                                if Playing == True:
                                    scrn.blit(PlayPauseDispl, (1660, 0))   
                                    pygame.display.flip()
                                    pygame.mixer.music.pause()
                                    UnPaused = False
                                    while UnPaused == False:
                                        for event in pygame.event.get():
                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                x, y = event.pos
                                                if ((x < 1710) and (x > 1660) and (y < 50) and (y > 0)):
                                                    UnPaused = True
                                                    pygame.mixer.music.unpause()
                                                elif ((x < 1920) and (x > 1870) and (y < 50) and (y > 0)):
                                                    Pop.popper(900, 0.025)
                                                    pygame.quit()
                                                    quit()
                                            elif event.type == pygame.QUIT:
                                                Pop.popper(900, 0.025)
                                                pygame.quit()
                                                quit()
                        elif event.type == pygame.KEYDOWN:
                            keys = pygame.key.get_pressed()
                            if event.key == pygame.K_LEFT:
                                M_x_change = -20
                                if (M_X == BallX) and ((M_Y + 100 > BallY) and (M_Y - 50 < BallY)):
                                    BallX -= 20
                                    MScore, OScore, M_X, M_Y, O_X, O_Y, BallX, BallY = CheckInNet(MScore, OScore, BallX, BallY, M_X, M_Y, O_X, O_Y)
                                TimePassed += 1/FPS
                                if MultiPlayer == False:
                                    M_X, M_Y, O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown, BallX, BallY, MScore, OScore = PosOGenrater(M_X, M_Y, O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown, BallX, BallY, 
                                                                                                                    MScore, OScore)
                            elif event.key == pygame.K_RIGHT:
                                M_x_change = 20
                                if (M_X == BallX) and ((M_Y + 100 > BallY) and (M_Y - 50 < BallY)):
                                    BallX += 20
                                    MScore, OScore, M_X, M_Y, O_X, O_Y, BallX, BallY = CheckInNet(MScore, OScore, BallX, BallY, M_X, M_Y, O_X, O_Y)
                                TimePassed += 1/FPS
                                if MultiPlayer == False:
                                    M_X, M_Y, O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown, BallX, BallY, MScore, OScore = PosOGenrater(M_X, M_Y, O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown, BallX, BallY, 
                                                                                                                    MScore, OScore)
                            elif event.key == pygame.K_UP:
                                M_y_change = -20
                                if M_Y < 0:
                                    M_Y = 0
                                if (M_Y == BallY) and ((M_X + 100 > BallX) and (M_X - 50 < BallX)):
                                    BallY -= 20
                                TimePassed += 1/FPS
                                if MultiPlayer == False:
                                    M_X, M_Y, O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown, BallX, BallY, MScore, OScore = PosOGenrater(M_X, M_Y, O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown, BallX, BallY, 
                                                                                                                    MScore, OScore)
                            elif event.key == pygame.K_DOWN:
                                M_y_change = 20
                                if M_Y > 980:
                                    M_Y = 980
                                if (M_Y == BallY) and ((M_X + 100 > BallX) and (M_X - 50 < BallX)):
                                    BallY += 20
                                TimePassed += 1/FPS
                                if MultiPlayer == False:
                                    M_X, M_Y, O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown, BallX, BallY, MScore, OScore = PosOGenrater(M_X, M_Y, O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown, BallX, BallY, 
                                                                                                                    MScore, OScore)
                            elif event.key == pygame.K_SPACE:
                                if (M_X + 20 == BallX) and ((M_Y + 100 > BallY) and (M_Y - 50 < BallY)):
                                    Powering = True
                                    SecondsPassed = 0
                                    while Powering == True:
                                        SecondsPassed += 1/FPS
                                        TimePassed += 1/FPS
                                        if MultiPlayer == False:
                                            M_X, M_Y, O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown, BallX, BallY, MScore, OScore = PosOGenrater(M_X, M_Y, O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown, BallX, BallY, 
                                                                                                                        MScore, OScore)
                                        DisplScrn()
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
                                        TimePassed += 1/FPS
                                        if MultiPlayer == False:
                                            M_X, M_Y, O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown, BallX, BallY, MScore, OScore = PosOGenrater(M_X, M_Y, O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown, BallX, BallY, 
                                                                                                                        MScore, OScore)
                                        DisplScrn()
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
                                        TimePassed += 1/FPS
                                        if MultiPlayer == False:
                                            M_X, M_Y, O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown, BallX, BallY, MScore, OScore = PosOGenrater(M_X, M_Y, O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown, BallX, BallY, 
                                                                                                                        MScore, OScore)
                                        DisplScrn()
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
                                        TimePassed += 1/FPS
                                        if MultiPlayer == False:
                                            M_X, M_Y, O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown, BallX, BallY, MScore, OScore = PosOGenrater(M_X, M_Y, O_X, O_Y, OutOLeft, OutORight, OutOUp, OutODown, BallX, BallY, 
                                                                                                                        MScore, OScore)
                                        DisplScrn()
                                        clock.tick(FPS)
                                        if BallX > RandomLimit:
                                            OutShot = True
                                            BallX = divrounder.divround(BallX, 20)
                                            BallY = divrounder.divround(BallY, 20)
                                            MScore, OScore, M_X, M_Y, O_X, O_Y, BallX, BallY = CheckInNet(MScore, OScore, BallX, BallY, M_X, M_Y, O_X, O_Y)
                            if MultiPlayer == True:
                                if event.key == pygame.K_w:
                                    OutUp = False
                                    while OutUp == False:
                                        O_Y -= 20
                                        if O_Y < 0:
                                            O_Y = 0
                                        if (O_Y == BallY) and ((O_X + 100 > BallX) and (O_X - 50 < BallX)):
                                            BallY -= 20
                                        TimePassed += 1/FPS
                                        DisplScrn()
                                        for event in pygame.event.get():
                                            if event.type == pygame.KEYUP:
                                                if event.key == pygame.K_w:
                                                    OutUp = True
                                        clock.tick(FPS)
                                elif event.key == pygame.K_s:
                                    OutDown = False
                                    while OutDown == False:
                                        O_Y += 20
                                        if O_Y > 980:
                                            O_Y = 980
                                        if (O_Y == BallY) and ((O_X + 100 > BallX) and (O_X - 50 < BallX)):
                                            BallY += 20
                                        TimePassed += 1/FPS
                                        DisplScrn()
                                        for event in pygame.event.get():
                                            if event.type == pygame.KEYUP:
                                                if event.key == pygame.K_s:
                                                    OutDown = True
                                        clock.tick(60)
                                elif event.key == pygame.K_a:
                                    OutLeft = False
                                    while OutLeft == False:
                                        O_X -= 20
                                        if O_X < 0:
                                            M_X = 0
                                        if (O_X == BallX) and ((O_Y + 100 > BallY) and (O_Y - 50 < BallY)):
                                            BallX -= 20
                                            MScore, OScore, M_X, M_Y, O_X, O_Y, BallX, BallY = CheckInNet(MScore, OScore, BallX, BallY, M_X, M_Y, O_X, O_Y)
                                        TimePassed += 1/FPS
                                        DisplScrn()
                                        for event in pygame.event.get():
                                            if event.type == pygame.KEYUP:
                                                if event.key == pygame.K_a:
                                                    OutLeft = True
                                        clock.tick(FPS)
                                elif event.key == pygame.K_d:
                                    OutRight = False
                                    while OutRight == False:
                                        O_X += 20
                                        if O_X > 1820:
                                            O_X = 1820
                                        if (O_X == BallX) and ((O_Y + 100 > BallY) and (O_Y - 50 < BallY)):
                                            BallX += 20
                                            MScore, OScore, M_X, M_Y, O_X, O_Y, BallX, BallY = CheckInNet(MScore, OScore, BallX, BallY, M_X, M_Y, O_X, O_Y)
                                        TimePassed += 1/FPS
                                        DisplScrn()
                                        for event in pygame.event.get():
                                            if event.type == pygame.KEYUP:
                                                if event.key == pygame.K_d:
                                                    OutRight = True
                                        clock.tick(FPS)
                        elif event.type == pygame.KEYUP:
                            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                                M_x_change = 0
                                M_y_change = 0
                    M_X += M_x_change
                    M_Y += M_y_change
                    clock.tick(FPS)
            elif ((x < 970) and (x > 10) and (y < 800) and (y > 100)):
                Pop.popper(900, 0.025)
                MultiPlayer = False
                easygui.msgbox('Bot mode selected', 'Selected', 'OK', str(pathlib.Path(image_path, "Thumbs Up Emoji.png")))
            elif ((x < 1920) and (x > 990) and (y < 800) and (y > 100)):
                Pop.popper(900, 0.025)
                MultiPlayer = True
                easygui.msgbox('Muliplayer mode selected', 'Selected', 'OK', str(pathlib.Path(image_path, "Thumbs Up Emoji.png")))
        clock.tick(60)