import pygame
from imgs import Screen
from Colors import black
from Colors import blue



'''###########################TEXT OBJECT##############################'''
def T_obj(text,font):
        t_surface= font.render(text,True,black)
        return t_surface, t_surface.get_rect()

def T_obj_Button(text,font):
        t_surface= font.render(text,True,blue)
        return t_surface, t_surface.get_rect()
    
def Display_message(text,x,y,size,Font):
        T_text=pygame.font.SysFont(Font, size, True, True)
        T_Surface,T_rect=T_obj(text,T_text)
        T_rect.center=(x,y)
        Screen.blit(T_Surface,T_rect)
        
        pygame.display.update()
