#!/bin/python

tinput = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
'''

from pprint import pprint
import io
from typing import AwaitableGenerator
f1= open('input.4.1.txt','r',newline='\n')
f0 = io.StringIO(tinput,newline='\n')


lines = tinput.splitlines()
fin = io.StringIO(tinput)

guesses=[int(x) for x in lines[0].split(',')]
print(guesses)

def parselines(input):
    # yield the guesses
    line=input.readline()
    yield([int(x) for x in line.split(',')])
    while True:
        line = input.readline()
        if not line:
            break
        if line!= '\n':
            print("ouch: ",line)
        assert line =='\n' 
        boardlines=[]
        for i in range(5):
            line = input.readline()
            if not line:
                break
            
            boardlines.append(line) 


        ba=[]
        for  l in boardlines:
            ba.append([int(x) for x in l.strip().split()])
        yield ba



class BBoard:
    def __init__(self, guesses, board):
        self.guesses = guesses
        self.board = board
        self.board_lookup={}
        for i in range(5):
           for j in range(5):
                self.board_lookup[self.board[i][j]] = (i,j)     
            
f0.seek(0)
fi = parselines(f0)
guesses= next(fi)
boards=[]
for f in fi:
    boards.append(BBoard(guesses,f))

b=boards[0]

row = 2
boardlines=lines[2:6]


#  def loadiput(input):

x = '''a

b

c'''