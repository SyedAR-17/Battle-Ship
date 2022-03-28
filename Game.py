###############################LIBRARIES##############################
import pygame
clock=pygame.time.Clock()
pygame.init()
from Write import Display_message
from Buttons import button_func
pygame.init()
from Com import computer
from Playerr import Player
from imgs import Screen
from GlobalV import exi

        
'''##############################MAIN##############################'''

def main():
    from GlobalV import counter
    P=Player()
    C=computer()
    #mouse=pygame.mouse.get_pos()
    image=pygame.image.load("Ocean.jpg")
    game=True
    Screen.blit(image,(0,0))
    while(game):
        for event in pygame.event.get():
            if(event.type)==pygame.QUIT:
                game=False
        if(counter == 0):
            button_func("START", 130, 430, 150, 50,P.setboard,C.setboard,None)
            if(event.type==pygame.MOUSEBUTTONDOWN):
                    counter=counter + 1
        if(counter == 1):
            button_func("ATTACK", 105, 500, 200, 50, C.Cattack, None,None)
            button_func("END TURN", 90, 570, 250, 50, P.Pattack, None,None)
        Display_message("PLAYER BOARD", 170, 330,50,'Calibri')
        Display_message("COM BOARD", 700, 330,50,'Calibri')
        button_func("QUIT", 105, 640, 200, 50, exi, None)
        #print(mouse)
        pygame.display.update()
        clock.tick(10)
                       
    
if __name__ == "__main__":
    main()
