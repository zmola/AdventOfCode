import copy
import operator
from functools import reduce

from pprint import pprint
import collections
import itertools

day=6
part=1

def read_input(day=day,part=part):
   f = open(f"input/{day}.{part}.txt")
   return [l.strip() for l in f.readlines()]


def parse_intlist_line(l):
    return [int(x) for x in l.split()]

def parse_intlist(lines):
    for l in lines:
        yield parse_intlist_line(l)



samp ='''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''.split('\n')

s = [list(x) for x in samp]

class Point:
    def __init__(self,x=0,y=0):
       self.x=x
       self.y=y
    
    def __repr__(self):
        return(f"Point({self.x},{self.y})")
    
    def __str__(self):
        x = self.x
        y = self.y
        return(f"({x},{y})")
    
    def addToMe(self,point):
        self.x=point.x
        self.y = point.y

    def __add__(self,point):
        return Point(self.x+point.x, self.y + point.y)

    def __copy__(self):
        p=Point(self.x,self.y)
        return p
    
    def __eq__(self,p):
        return (self.x==p.x) and (self.y == p.y)
    
    def toTuple(self):
       return (self.x,self.y)

class Guard(Point):
    def __init__(self, pos: Point, dir: Point):
        self.pos=Point(pos.x,pos.y)
        self.dir=Point(dir.x,dir.y)
        self.name = 'x'

    def __eq__(self,g):
        return (self.pos == g.pos) and (self.dir == g.dir)


    def __repr__(self):
        return(f"Pos({self.pos.x},{self.pos.y}),dir({self.dir.x},{self.dir.y})")

    def __copy__(self):
        return(Guard(Point(self.pos),Point(self.dir)))

    def nextStep(self):
        return self.pos + self.dir
    
    def move(self):
        self.pos = self.pos + self.dir

    def turnright(self):
        # print('turn',self.name, self.dir)
        if self.dir.x == 0:
            self.dir.x = -self.dir.y
            self.dir.y = 0
        else:
            self.dir.y = self.dir.x
            self.dir.x = 0
        # print('turn',self.dir)

    def toTuple(self):
        return (self.pos.toTuple(), self.dir.toTuple())


class Map:

    def __init__(self,m):
        self.m=copy.deepcopy(m)
        (y,x,dirchar) = self.findstart()
        self.startpoint=Point(x,y)
        self.guard=Guard(Point(x,y),Point(0,-1))
        self.startdir = Point(0,-1)
        self.mark(self.guard.pos)
        #
        self.maxx = len(m[0])-1
        self.maxy = len(m)-1
        self.cycleCount = 0
        self.cycle = []
        self.steps = set()
        self.stepcnt=0
        self.blocklist = list()

    def mark(self,p):
        self.m[p.y][p.x] = 'X'
        # self.blocklist.append(p)


    def findstart(self):
        for i in range(len(self.m)):
            for j in range(len(self.m[i])):
                if self.m[i][j] == '^':
                    return (i,j,'^')
        return False

    def charAt(self,p):
        return self.m[p.y][p.x]
    
    def pointoutside(self,p):
        if p.x < 0 or p.y < 0:
            return True
        if p.x > self.maxx or p.y > self.maxy:
            return True
        else: 
            return False


    def countDistinct(self):
        cnt=0
        for r in self.m:
            for c in r:
                if c == 'X':
                    cnt = cnt + 1
        return cnt
    
    def move(self):
        # if self.stepcnt % 1 == 0:
        #     print(self.stepcnt)

        newp = self.guard.nextStep()
        # print(self.guard.__repr__())
        if self.pointoutside(newp):
            #print('outofbounds')
            return False        
        if self.guard.toTuple() in self.steps:
            #print("alreadyVisitied")
            self.cycleCount = self.cycleCount +1
            return False
        if self.charAt(newp)  == '#':
            #print("turnRight")
            self.steps.add(self.guard.toTuple())
            self.guard.turnright()
            self.move()
            return True
        #else:
        self.steps.add(self.guard.toTuple())
        self.guard.move()
        self.mark(self.guard.pos)
        self.stepcnt +=1
        # self.causes_cycle()
        return True
    
    def run(self):
        while self.move():
            pass
        # x=set([(p.x,p.y) for p in self.cycle])
        # x.discard((self.startpoint.x,self.startpoint.y))
    
        return self.cycleCount > 0 
    


ss = Map(s)
    
s = [list(x) for x in read_input()]
ss = Map(s)
ss.run()
print( ss.countDistinct(),
               ss.cycleCount, 
               len(ss.cycle), 
               ss.stepcnt)



m = copy.deepcopy (ss.m)
ss.m[ss.startpoint.y][ss.startpoint.x] = '^'
# for l in m:
#     print(''.join(l))

    

def buildList(m):
    olist = []
    for j in range(len(m)):
        for i in range(len(m[j])):
            if m[j][i]=='X':
               olist.append((i,j))
    oo = set(olist)
    oo.discard((ss.startpoint.x,ss.startpoint.y))
    olist=list(oo)
    return olist           

olist = buildList(m)
cycles=[]
i = 0
for obsticle in olist:
    if not i % 200: 
        print(f"i = {i}, cnt= {len(cycles)}")
    news=copy.deepcopy(s)
    news[obsticle[1]][obsticle[0]] = '#'
    ss = Map(news)
    if ss.run():
        cycles.append(object)
    i = i+1
print(f"num_cycles = {len(cycles)}")

#TODO: make run capture the cycles
# TODO: store guard locations for where you have been, to capture cycles.
# TODO: dedup cycle list, remove startpoint


# TODO: for every obsticle location, run the map.
#       if obsticle causes cycle, add 1 to cycle count
        
# buildList(ss.m)
# olist.sort()
# olist.remove((ss.startpoint.x,ss.startpoint.y))
# print('olsit.len:',len(olist))
# i=0


# for x,y in olist:
#   print(i)
#   t=copy.deepcopy(s)
#   t[y][x]='#'
#   tt=Map(t)
#   i=i+1