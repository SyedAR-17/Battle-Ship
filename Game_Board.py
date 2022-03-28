import pygame
import random
pygame.init()
from imgs import Screen
from Write import Display_message
from Colors import white
from Colors import red
from Colors import green
from Colors import blue



###############################BOARD##################################

class Board:
    def __init__(self):
        self.grid =[[1]*8 for _ in range(8)] 
    def setship(self,x,y,o):
        if(o==1):
            self.grid[x][y]=0
            self.grid[x+1][y]=0
        elif(o==0):
            self.grid[x][y]=0
            self.grid[x][y+1]=0
    def setsubmarine(self,x,y,o):
        if(y>4 and x>4):
            o=-1
        if(y>4 and x<4):
            o=1
        if(o==-1):
            self.grid[x][y]=4
            self.grid[x-1][y]=4
            self.grid[x-2][y]=4
            self.grid[x-3][y]=4
        if(o==1):
            self.grid[x][y]=4
            self.grid[x+1][y]=4
            self.grid[x+2][y]=4
            self.grid[x+3][y]=4
        elif(o==0):
            self.grid[x][y]=4
            self.grid[x][y+1]=4
            self.grid[x][y+2]=4
            self.grid[x][y+3]=4
    def printboard(self,com=False):
        print()
        num=-1
        nm=-1
        for i in range(9):
            for j in range(9):
                if(i==0 or j==0):
                        z="0"
                        if(i==0):
                            num=str(num)
                            z=num
                            num=int(num)
                            num=num+1
                        if(j==0):
                            nm=str(nm)
                            z=nm
                            nm=int(nm)
                            nm=nm+1 
                        if(z!='-1'):
                            pygame.draw.rect(Screen, white,((30*i)+20,(30*j)+20,28,28),1)
                            Display_message(z, (30*i)+32, (30*j)+37, 20, 'Calibri')
                            pygame.draw.rect(Screen, white,((30*i)+570,(30*j)+370,28,28),1)
                            Display_message(z, (30*i)+582, (30*j)+387, 20, 'Calibri')
                            pygame.display.update()
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if(com==False):
                    if(self.grid[i][j]==1):
                        '''print("*",end=" ")'''
                        pygame.draw.rect(Screen, white,((30*i)+50,(30*j)+50,28,28,),1)
                        pygame.display.update()
                    elif(self.grid[i][j]==2):
                        pygame.draw.rect(Screen, red,((30*i)+50,(30*j)+50,28,28))
                        pygame.display.update()
                    elif(self.grid[i][j]==0 or self.grid[i][j]==4):
                        '''print("S",end=" ")'''
                        pygame.draw.rect(Screen,green,((30*i)+50,(30*j)+50,28,28))
                        pygame.display.update()
                    elif(self.grid[i][j]==3):
                        pygame.draw.rect(Screen,blue,((30*i)+50,(30*j)+50,28,28))
                        pygame.display.update()
                elif(com==True):
                    if(self.grid[i][j]==1):
                        '''print("*",end=" ")'''
                        pygame.draw.rect(Screen, white,((30*i)+600,(30*j)+400,28,28),1)
                        pygame.display.update()
                    elif(self.grid[i][j]==2):
                        pygame.draw.rect(Screen, red,((30*i)+600,(30*j)+400,28,28))
                        pygame.display.update()
                    elif(self.grid[i][j]==0 or self.grid[i][j]==4):
                        '''print("S",end=" ")'''
                        pygame.draw.rect(Screen, green,((30*i)+600,(30*j)+400,28,28))
                        pygame.display.update()
                    elif(self.grid[i][j]==3):
                        pygame.draw.rect(Screen, blue,((30*i)+600,(30*j)+400,28,28))
                        pygame.display.update()
            print()
            
    def attack(self,x,y,com=False):
        count_ships=0
        if(self.grid[x][y]==3 and com ==True):
            x=random.choice([1,2,3,4,5,6,7,0])
            y=random.choice([1,2,3,4,5,6,7,0])
        if(self.grid[x][y]==0 or self.grid[x][y]==4):
            self.grid[x][y]=2
        elif(self.grid[x][y]==1):
            self.grid[x][y]=3
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if(self.grid[i][j]==0 or self.grid[i][j]==4):
                    count_ships=count_ships+1
        if(count_ships==0 and com==True):
            Display_message("Player WON !", 526, 100, 50, 'Serif')
        if(count_ships==0 and com==False):
            Display_message("Player LOST !", 526, 100, 50, 'Serif')
                
                
                
                
                
                
                
                
                
                    