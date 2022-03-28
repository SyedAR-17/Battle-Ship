from Game_Board import Board
import random
################################COM##################################

class computer:
    CB=Board()
    def setboard(self):
        o=random.choice([0,1])
        x=random.choice([0,1,2,3,4,5,6,7])
        y=random.choice([0,1,2,3,4,5,6,7])
        if(x==7):
            o=0
        elif(y==7):
            o=1
        self.CB.setship(x,y,o)
        #print("computer Board")
        self.CB.printboard(com=True)
        o=random.choice([0,1])
        x=random.choice([0,1,2,3,4,5,6,7])
        y=random.choice([0,1,2,3,4,5,6,7])
        if(x==7):
            o=0
        elif(y==7):
            o=1
        self.CB.setsubmarine(x,y,o)
        #print("computer Board")
        self.CB.printboard(com=True)
    def Cattack(self):
        x=int(input("ENTER x coordinate: "))
        y=int(input("ENTER y coordinate: "))
        self.CB.attack(x, y, com=True)
        #print("computer Board")
        self.CB.printboard(com=True)
