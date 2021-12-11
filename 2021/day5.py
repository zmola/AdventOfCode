
tinput='''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
'''



from pprint import pprint
import io
import math
from typing import DefaultDict

def sign( a):
    if a > 0:
        return 1
    if a < 0:
        return -1
    if a == 0:
        return 0
    return nan


f1= open('input.5.1.txt','r',newline='\n')
f0 = io.StringIO(tinput,newline='\n')

fin = f1

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    




    def path( self, v):
        
        # if (self.x-v.x)*(self.y - v.y) != 0:
        #     return None
        ylength = v.y - self.y
        xlength = v.x - self.x 
        xinc = sign(xlength)
        yinc = sign(ylength)
        rtn = [self]
        for i in range(max(abs(xlength),abs(ylength))):
            rtn.append(Point(self.x+ (xinc * (i+1)), self.y + yinc *( i+1)))

        return rtn
        # return None
        if self.x == v.x:
            length = v.y - self.y
            inc = sign(length)
            rtn = [self]
            a = self.y
            for i in range(abs(length)):
                rtn.append(Point(self.x, a + inc *( i+ 1)))
            return rtn
        if self.y == v.y:
            length = v.x - self.x 
            inc = sign(length)
            rtn = [self]
            a = self.x
            for i in range(abs(length)):
                rtn.append(Point(a+ (inc * (i+1)) ,self.y))
            return rtn
        return None
        

    classmethod 
    def parse(s):
        s1 = s.split(',')
        x = int(s1[0])
        y = int(s1[1])
        return Point(x,y)

    def __str__(self):
        return f"({self.x},{self.y})"    
    def __repr__(self):
        return f"Point({self.x},{self.y})"    

lines= fin.readlines()

# lines = f1.readlines()
from collections import defaultdict
ventmap = defaultdict(int)

sum = 0
for line in lines:
   s1 = line.split('->')
   a=  Point.parse(s1[0])
   b=  Point.parse(s1[1])
   # print("l ", a, b)
   p = a.path(b)
   if p:
    sum += len(p)
    # print(p)
    for pnt in p :
        ventmap[repr(pnt)] += 1

#print("part1 sum:",sum )    

finalsum=0
for k,v in ventmap.items():
    finalsum += v
print("part1 finalsum:", finalsum )    
danger=[ v for k,v in ventmap.items() if v > 1]
warn=[ v for k,v in ventmap.items() if v == 1]
    
print(len(danger), len(warn),len(danger)+ len(warn),len(ventmap))
print(len(danger))
#guess1=6249  too low

#{k:v for k,v in ventmap.items() if v > 1}    
