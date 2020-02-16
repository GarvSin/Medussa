# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class tryingticktock:
    def __init__(self,myList):
        self.myList = myList
        
    #def ticTockToe(self,move)
    def check_result(self,myList):
        if self.myList[0]==self.myList[1]==self.myList[2]:
            print("matched")
            return 1
        elif self.myList[3]==self.myList[4]==self.myList[5]:
            print("matched")
            return 1
        elif self.myList[6]==self.myList[7]==self.myList[8]:
            print("matched")
            return 1
        elif self.myList[0]==self.myList[3]==self.myList[6]:
            print("matched")
            return 1
        elif self.myList[4]==self.myList[1]==self.myList[7]:
            print("matched")
            return 1
        elif self.myList[5]==self.myList[8]==self.myList[2]:
            print("matched")
            return 1
        elif self.myList[0]==self.myList[4]==self.myList[8]:
            print("matched")
            return 1
        elif self.myList[6]==self.myList[4]==self.myList[2]:
            print("matched")
            return 1
        
    def moves(self):
        total_moves = 0
        while total_moves <= 9:
            print("current move {}".format(total_moves))
            
            move = int(input("Enter location to move"))
            print(move)
            
            if self.myList[move] == 'X' or self.myList[move] == 'O' :
                print("Enter some other location. This move is already done.")
                total_moves -= 1
            else:
                if total_moves%2==0:
                    self.myList[(self.myList.index(move))] = 'O'
                else:
                    self.myList[(self.myList.index(move))] = 'X'
            self.display()
            
            if self.check_result(self.myList)==1:
                break
    
            total_moves += 1

    def display(self):
        print(self.myList[0:3])
        print(self.myList[3:6])
        print(self.myList[6:9])
        

test = tryingticktock([0,1,2,3,4,5,6,7,8])
test.moves()
