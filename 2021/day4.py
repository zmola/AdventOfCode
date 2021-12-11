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

f1= open('input.4.1.txt','r',newline='\n')
f0 = io.StringIO(tinput,newline='\n')


#lines = tinput.splitlines()
#fin = io.StringIO(tinputA)

fin = f0

#guesses=[int(x) for x in lines[0].split(',')]
#print(guesses)

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
        self.guess=guesses[0]
        self.board = board
        self.turn = 0
        self.hits = [[-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1]]
        self.board_lookup={}
        for i in range(5):
            for j in range(5):
                self.board_lookup[self.board[j][i]] = (i,j)

    def win(self,x,y):
        h = [ h for h in self.hits[y] if h >= 0]
        v = [ r[x] for r in self.hits if r[x] >= 0]
        d1 = []
        d2 = []

        if len(h)==5 or len(v)==5 or len(d1) ==5 or len(d2)==5:
            print("h,y",h,v)
            return self.hits[y][x] 
        else:
            return 0

    def score(self,num):
        s = 0
        for y in range(5):
            for x in range(5):
                if  self.hits[y][x] < 0:
                    #print('score: ', self.board[y][x] )
                    s += self.board[y][x]      
        print(s)    
        return s * num        

    def play(self):
        guess = self.guesses[self.turn]
        self.guess = guess
        self.turn += 1
        result = self.board_lookup.get(guess,False)
        if result:
            self.hits[result[1]][result[0]] = guess
            if self.win(result[0],result[1]):
                print('xxxxx  board')
                pprint(self.board)
                print('yyyyy -- hits')
                pprint(self.hits)
                return self.score(guess)
        return 0
        
fin.seek(0)
fi = parselines(fin)
guesses= next(fi)
boards=[]
for f in fi:
    boards.append(BBoard(guesses,f))

keepPlaying = True


def turn():
    for i in range(len(boards)):
        b = boards[i]
        rtn = b.play()
        if rtn:
            keepPlaying= False
            print(i,rtn)
            print(b.turn,i,rtn)
            return(b)
    return 0



while len(boards) > 01:
     a = turn()
     if a:
         boards.remove(a)
print(a.score(a.guess))


# turn()
# turn()
# turn()
# turn()
# turn()
# turn()
# turn()
# turn()
# turn()
# turn()
# turn()
# wa = turn(); wa
# boards[2].hits
# bb=boards[2]
# bb.turn
# g=guesses[bb.turn -1]
# bb.score(g)
# t=turn()
# g=guesses[boards[0].turn -1]
# i=boards[0].score(g)
# j=boards[1].score(g)
# k=boards[2].score(g)
# bb=boards[2]
# print((i,j,k))
# print(t,g)


# h = [ h for h in self.hits[y] if h >= 0]
# v = [ r[x] for r in self.hits if r[x] >= 0]
 
