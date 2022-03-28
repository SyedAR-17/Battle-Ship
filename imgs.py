import pygame
from Colors import white
pygame.init()
#############################PYGAME###################################
Screen=pygame.display.set_mode(size=(900,700))
pygame.display.set_caption("BATTLESHIP")
def draw():
    pygame.draw.rect(Screen, white, (130,430,150,50))
