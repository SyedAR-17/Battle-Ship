import pygame
pygame.init()
from imgs import Screen
from Colors import blue
from Write import T_obj
from Write import T_obj_Button

'''##########################BUTTON FUNC##############################'''
def button_func(typ,x,y,w,h,action=None,action2=None,action3=None):
    pygame.draw.rect(Screen, blue,(x,y,w,h),1)
    mouse=pygame.mouse.get_pos() 
    click=pygame.mouse.get_pressed()
    T_text=pygame.font.SysFont('Calibri', 50, True, True)
    if(x+w > mouse[0] > x and y+h > mouse[1]>y):
        T_Surface,T_rect=T_obj_Button(typ,T_text)
        if(click[0] == 1 and action != None ):
            action()
            if(action2 != None):
                action2()
                if(action3 != None):
                    action3()
    else:
        T_Surface,T_rect=T_obj(typ,T_text)
    T_rect.center=(x+(w/2)),(y+(h/2))
    Screen.blit(T_Surface,T_rect)
    
    