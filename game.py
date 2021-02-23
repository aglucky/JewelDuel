import numpy as np
import pandas as pd
import random

#Gem Object, represented as greek letters
class gem:
  def __init__(self):
    self.types = ['\u0394','\u03B8','\u03BB','\u03B2','\u03A9']
    self.type = '0'
    self.owner = 0
    self.matchCol=[]
    self.mathRow=[]

  #Made to avoid gems sharing a reference
  def setType(self,jewel):
    self.type = self.types[jewel]

  #For win condition
  def setOwn(self,player):
    self.owner[player] = True

#Game class, using numpy 2d array   
class game:
  def __init__(self,p1,p2):
    self.board = np.zeros([6,6],dtype = object)
    for ix,iy in np.ndindex(self.board.shape):
      self.board[ix,iy] = gem()
    self.players = [p1,p2]
    self.win = False
  
  #Fills empty slots with random gems
  def fillBlank(self):
    for ix,iy in np.ndindex(self.board.shape):
      if self.board[ix,iy].type == '0':
        self.board[ix,iy].setType(random.randint(0,4))

  #Swaps two pieces on board
  def swap(self,gem1x,gem1y,gem2x,gem2y):
    self.board[gem1x,gem1y],self.board[gem2x,gem2y] = self.board[gem2x,gem2y],self.board[gem1x,gem1y]

  #recursive solution to empty matches
  def floodFillUp(self,x,y,check):
    if self.board[x,y].type == check:  
        self.board[x,y].type = '0' 
        if x > 0:
            self.floodFillUp(x-1,y,check)
        if x < self.board.shape[0] - 1:
            self.floodFillUp(x+1,y,check)
    
  def floodFillSide(self,x,y,check):
    if self.board[x,y].type == check:  
        self.board[x,y].type = '0' 
        if y > 0:
            self.floodFillSide(x,y-1,check)
        if y < self.board.shape[1] - 1:
            self.floodFillSide(x,y+1,check)
       
       
  #Checks for matches and empties rows
  def isMatch(self,num):
    inRow = 1
    for iy in range(self.board.shape[1]):
      for ix in range(self.board.shape[0]-1):
        if self.board[ix,iy].type != '0':
          if self.board[ix,iy].type == self.board[ix+1,iy].type:
            inRow+=1
            if inRow == num:
              check = self.board[ix,iy].type
              self.floodFillUp(ix,iy,check)
              return True
          else:
            inRow = 1

    for ix in range(self.board.shape[0]):
      for iy in range(self.board.shape[1]-1):
        if self.board[ix,iy].type != '0':
          if self.board[ix,iy].type == self.board[ix,iy+1].type:
            inRow+=1
            if inRow == num:
              check = self.board[ix,iy].type
              self.floodFillSide(ix,iy,check)
              return True

    return False

  #Drags gems above empty slots down
  def gravDrag(self):
    for i in range(self.board.shape[0]):
      for iy in range(0,self.board.shape[0]):
        for ix in range(self.board.shape[1]-1,0,-1):
          if self.board[ix,iy].type == '0':
            self.swap(ix,iy,ix-1,iy)
        
  #Shows board as pandas df with coordinates
  def show(self):
    C_Label=['A','B','C','D','E','F']
    R_Label=['1','2','3','4','5','6']

    showBoard = np.zeros([6,6],dtype = str)
    for ix,iy in np.ndindex(showBoard.shape):
      showBoard[ix,iy] = self.board[ix,iy].type

    df = pd.DataFrame(showBoard,columns = C_Label,index = R_Label)
    print(df)
  
  #Add gem with ownership, used when 4 in a row happens
  def addSpecialGem(self,player):
    for ix,iy in np.ndindex(self.board.shape):
      if self.board[ix,iy].type == '0':
        self.board[ix,iy].type = str(self.players.index(player)+1)
        self.board[ix,iy].owner = player
        break

  #Checks for win condition and finds a winner, returns 0 if none
  def winCheck(self):

    inRow = 1
    for iy in range(self.board.shape[1]):
      for ix in range(self.board.shape[0]-1):
        if self.board[ix,iy].owner != 0:
          if self.board[ix,iy].owner == self.board[ix+1,iy].owner:
            inRow+=1
          if inRow == 3:
            return self.board[ix,iy].owner
          else:
            inRow = 1

    for ix in range(self.board.shape[0]):
      for iy in range(self.board.shape[1]-1):
        if self.board[ix,iy].owner != 0:
          if self.board[ix,iy].owner == self.board[ix,iy+1].owner:
            inRow+=1
            if inRow == 3:
              return self.board[ix,iy].owner

    return 0

  #Checks if move is valid
  def moveCheck(self,gem1,gem2):
    #Gem1 and Gem2 formatted as string (ex. A6)
    posLets = ['A','B','C','D','E','F','G']
    posNums = ['1','2','3','4','5','6']

    if len(gem1) == 2 and len(gem2)==2:
      if gem2[0] in posLets and gem2[1] in posNums:
        if gem2[0] in posLets and gem2[1] in posNums:
          if posLets.index(gem1[0]) == posLets.index(gem2[0]) or posNums.index(gem1[1]) == posNums.index(gem2[1]):
            if abs(posLets.index(gem1[0]) - posLets.index(gem2[0]))==1 or abs(posNums.index(gem1[1]) - posNums.index(gem2[1])) ==1:
              return True

    return False