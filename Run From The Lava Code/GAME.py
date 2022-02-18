
import pygame, sys
import json
import time
from pygame.event import event_name
from Sprite import *

#©2021 HARIZ GAMES
print("")
print("Pls Run Game In Main.py")
print("")

def mainGame(CcOpYrIgHt):
    pygame.init()
    pygame.mixer.init()
    skrin = pygame.display.set_mode((600, 500))
    clock = pygame.time.Clock()
    image = pygame.image.load
    pygame.display.set_caption('RUN FROM THE LAVA')
    pygame.display.set_icon(image(IconSprite))
    gameSmolFont = pygame.font.Font(Font, 30)
    gameVerySmolFont = pygame.font.Font(Font, 15)
    gameFont = pygame.font.Font(Font, 50)
    gameBIGFont = pygame.font.Font(Font, 70)
    Saquer = pygame.Surface
    time.sleep(1)
    firstTime = False

    data={
        'death' : 0,
        'HiJumps' : 0
    }

    Green = (20,105, 105)
    Black = (255, 255 , 255)

    try:
        with open('saveFile.json') as SaveFile:
            data = json.load(SaveFile)

    except:
        print("      __________________")
        print("      |                |")
        print("      |                |")
        print("      |No File Detected|")
        print("      |                |")
        print("      |                |")
        print("      ------------------")
        firstTime = True

    grey = (150, 150, 150)
    Dgrey = (170, 170, 170)
    y = 300
    gravity = 0
    Jumps = 0

    y -= gravity

    square = image(PlayerSprite)
    squarect = square.get_rect(center =(300, y))
    square = image(PlayerSprite)
    squarect = square.get_rect(center =(300, y))

    squareHujung = Saquer([600, 100])
    squareHujung.fill((255, 106, 0))
    squarectH = squareHujung.get_rect(center =(300, 540))
    squarectH2 = squareHujung.get_rect(center =(300, -40))


    squarebg = Saquer([600, 500])
    squarebg.fill(grey)
    squarectbg = square.get_rect(center =(50, 50))

    squaremenu = image(ButtonSprite)
    squaremenu = pygame.transform.scale(squaremenu, (400, 200))
    squarectmenu = square.get_rect(center =(115, 275))

    title = image(TitleSprite)
    title = pygame.transform.scale(title, (378, 122))
    title_rect = title.get_rect(center = (300, 70))

    D_text = gameFont.render(f'Death : {data["death"]}', True, Green)
    D_text_rect = D_text.get_rect(center = (300, 20))

    J_text = gameSmolFont.render(f'Jump : {Jumps}', True, Black)
    J_text_rect = J_text.get_rect(center = (100, 40))

    Play_text = gameBIGFont.render('Play', True, Green)
    Play_text_rect = Play_text.get_rect(center = (300, 350))

    Jh_text = gameFont.render(f'Jump Highscore : {data["HiJumps"]}', True, Dgrey)
    Jh_text_rect = Jh_text.get_rect(center = (300, 200))
    Jh2_text = gameVerySmolFont.render(f'Jump Highscore : {data["HiJumps"]}', True, Green)
    Jh2_text_rect = Jh2_text.get_rect(center = (130, 150))

    Tuto1_text = gameVerySmolFont.render('press esc to exit to menu', True, Green)
    Tuto2_text = gameVerySmolFont.render('press space to jump', True, Green)
    Tuto1_text2 = gameFont.render('press esc to exit to menu', True, Green)
    Tuto2_text2 = gameFont.render('press space to jump', True, Green)
    Tuto1_text_rect = Tuto1_text.get_rect(center = (110, 190))
    Tuto2_text_rect = Tuto2_text.get_rect(center = (110, 210)) 
    Tuto1_text_rect2 = Tuto2_text2.get_rect(center = (260, 160))
    Tuto2_text_rect2 = Tuto2_text2.get_rect(center = (300, 330))
    Jh2_text_rect = Jh2_text.get_rect(center = (130, 150))

    Copyright_text = gameVerySmolFont.render(f"{CcOpYrIgHt}", True, Green)
    Copyright_text_rect = Copyright_text.get_rect(center = (60, 480))

    Pauseimage = image(PauseSprite)
    Pauseimage = pygame.transform.scale(Pauseimage, (50, 50))
    Pauseimage2 = image(PauseSprite)
    Pauseimage2 = pygame.transform.scale(Pauseimage2, (100, 100))
    PauseimageRect = Pauseimage.get_rect(center =(550, 30))
    PauseimageRect2 = Pauseimage2.get_rect(center =(300, 250))

    #Sound
    Death = pygame.mixer.Sound(DEath)
    jump = pygame.mixer.Sound(CLick)

    #IDK
    ismenu = True
    ispause = False


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                time.sleep(1)
            
                if Jumps >= data['HiJumps']:
                        data['HiJumps'] = Jumps
                with open('saveFile.json', 'w') as SaveFile:
                    json.dump(data,SaveFile)

                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print("       Program Quited")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                pygame.quit()
                sys.exit()
        
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if ismenu == False:
                #    y -= 100
                #    jump.play()
                #    Jumps += 1
                
                if ismenu != True:
                    if ispause == False:
                        if PauseimageRect.collidepoint(event.pos):
                            ispause = True 
                            y = 300
                            Death.play()
                            ispause = True
                            time.sleep(0.01)
                    if ispause == True:
                        if PauseimageRect2.collidepoint(event.pos):
                            ispause = False
                            Death.play()
                            time.sleep(0.01)
            
                else:
                    if squarectmenu.collidepoint(event.pos) or Play_text_rect.collidepoint(event.pos):
                        ismenu = False
                        y = 300
                        jump.play()
                        time.sleep(1)
            
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if ismenu == False:
                        if ispause == False:
                            y -= 100
                            jump.play()
                            Jumps += 1
                if event.key == pygame.K_ESCAPE:
                    ismenu = True
                    if Jumps >= data['HiJumps']:
                        data['HiJumps'] = Jumps
                    with open('saveFile.json', 'w') as SaveFile:
                       json.dump(data,SaveFile)
                    Jh_text = gameFont.render(f'Jump Highscore : {data["HiJumps"]}', True, Dgrey)
                    Jh_text_rect = Jh_text.get_rect(center = (300, 200))
                    y = 70
                    Jumps = 0
                    gravity = 0
                    ispause == False
    
        skrin.fill(grey)
    
        if ismenu == False:
            if ispause == False:
                gravity -= 5
                y -= gravity
                gravity += 5

    
        square = image(PlayerSprite)
        squarect = square.get_rect(center =(300, y))

        if ismenu == False:
            if ispause == False:
                skrin.blit(square, squarect)
                skrin.blit(squareHujung, squarectH)
                skrin.blit(squareHujung, squarectH2)

    
        D_text = gameFont.render(f'Death : {data["death"]}', True, Green)
        D_text_rect = D_text.get_rect(center = (300, 20))
        J_text = gameFont.render(f'Jump : {Jumps}', True, Black)
        J_text_rect = D_text.get_rect(center = (100, 40))

        if y <= 20 or y >= 480:
            data['death'] += 1
            y = 70
            if Jumps >= data['HiJumps']:
                data['HiJumps'] = Jumps
            with open('saveFile.json', 'w') as SaveFile:
                json.dump(data,SaveFile)
            gravity = 0
            Death.play()
            ismenu = True
            time.sleep(0.3)
            ismenu = False
            Jumps = 0
            with open('saveFile.json', 'w') as SaveFile:
                json.dump(data,SaveFile)
        
        if ismenu == False:
            if ispause == False:
                Jh2_text = gameSmolFont.render(f'Jump Highscore : {data["HiJumps"]}', True, Green)
                Jh2_text_rect = Jh2_text.get_rect(center = (130, 150))
                skrin.blit(D_text, D_text_rect)
                skrin.blit(J_text, J_text_rect)
                skrin.blit(Jh2_text, Jh2_text_rect)
                skrin.blit(Pauseimage, PauseimageRect)
                if(data['death'] <= 5 and firstTime == True):
                    skrin.blit(Tuto1_text, Tuto1_text_rect)
                    skrin.blit(Tuto2_text, Tuto2_text_rect)
            if ispause == True:
                skrin.blit(Pauseimage2, PauseimageRect2)
                skrin.blit(Tuto1_text2, Tuto1_text_rect2)
                skrin.blit(Tuto2_text2, Tuto2_text_rect2)

        #Menu
        if ismenu == True:
            skrin.blit(squaremenu, squarectmenu)
            skrin.blit(Play_text, Play_text_rect)
            skrin.blit(title, title_rect)
            skrin.blit(Jh_text, Jh_text_rect)

        skrin.blit(Copyright_text, Copyright_text_rect)
    
        pygame.display.update()
        clock.tick(60)