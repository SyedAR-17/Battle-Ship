import random

from Game_Board import Board
class Player:
    PB=Board()
    def setboard(self):
        x=int(input("Enter Value of X: "))
        y=int(input("Enter the Value of Y: "))
        o=int(input("Orientation of the ship: 1 for v or 0 for h: "))
        if(x==7):
            o=0
        elif(y==7):
            o=1
        self.PB.setship(x,y,o)
        #print("Player Board")
        self.PB.printboard(com=False)
        x=int(input("Enter Value of X for Submarine: "))
        y=int(input("Enter the Value of Y for Submarine: "))
        o=int(input("Orientation of the ship: 1 for v or 0 for h: "))
        if(x==7):
            o=0
        elif(y==7):
            o=1
        self.PB.setsubmarine(x, y, o)
        #print("Player Board")
        self.PB.printboard(com=False)
    def Pattack(self):
        x=random.choice([0,1,2,3,4,5,6,7])
        y=random.choice([0,1,2,3,4,5,6,7])
        self.PB.attack(x, y, com=False)
        #print("Player Board")
        self.PB.printboard(com=False)
        
        