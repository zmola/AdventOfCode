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

# def findstart(s):
#     for i in range(len(s)):
#         for j in range(len(s[i])):
#             if s[i][j] == '^':
#                 return (i,j,'^')
#     return False
            
# (y,x,dirchar) = findstart(s)
# pos=[y,x]
# dir=[-1,0]


class Point:
    def __init__(self,x=0,y=0):
       self.x=x
       self.y=y
    
    def __repr__(self):
        return(f"Point({self.x},{self.y})")
    
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

class Guard(Point):
    def __init__(self, pos: Point, dir: Point):
        self.pos=pos
        self.dir=dir

    def __eq__(self,g):
        return (self.pos == g.pos) and (self.dir == g.dir)
    
    def nextStep(self):
        return self.pos + self.dir


class Map:
    def mark(self,p):
        self.m[p.y][p.x] = 'X'

    def __init__(self,m):
        self.m=m
        (y,x,dirchar) = self.findstart(m)
        self.guard=Point(x,y)
        self.dir=Point(0,-1)
        self.mark(self.guard)
        self.maxx = len(m[0])-1
        self.maxy = len(m)-1

    def findstart(self,s):
        for i in range(len(s)):
            for j in range(len(s[i])):
                if s[i][j] == '^':
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
        
    def turnright(self):
        if self.dir.x == 0:
            self.dir.x = -self.dir.y
            self.dir.y = 0
        else:
            self.dir.y = self.dir.x
            self.dir.x = 0

    def move(self):
        newp = self.guard + self.dir
        if self.pointoutside(newp):
            return False 
        if self.charAt(newp)  == '#':
            self.turnright()
            self.move()
        else:
            self.guard = newp
            self.mark(self.guard)
        return True
    
    def wouldbeloop(self):
        self.tguard=Point(self.guard.x,self.guard.y)
        self.startpos = Point(self.guard.x,self.guard.y)
        self.startdir = Point(self.dir.x,self.dir.y)

    def testmove(self):
        newp = self.guard + self.dir
        if self.pointoutside(newp):
            return False 
        if self.charAt(newp)  == '#':
            self.turnright()
            self.move()
        else:
            self.guard = newp
            self.mark(self.guard)
        return True
    
  #  def s

    def countDistinct(self):
        cnt=0
        for r in self.m:
            for c in r:
                if c == 'X':
                    cnt = cnt + 1
        return cnt
    
    def causes_cycle(self):
        # if right turn here puts me into a cycle, add position to cycle list
        pass

from collections import defaultdict

class ObsticalMap():
    def __init__(self,m):
        self.obsticles=[]
        self.yobsticles = defaultdict(list)
        self.xobsticles = defaultdict(list)
        for y in range(len(m)):
            for x in range(len(m[y])):
                self.obsticles.append(Point(x,y))
                self.yobsticles[y].append(x)
                self.xobsticles[x].append(y)
        # sorting probably not necessary
        for k,v in self.yobsticles:
            v.sort()
        for k,v in self.xobsticles:
            v.sort()
        self.m=m
        self.maxx = len(m[0])-1
        self.maxy = len(m)-1
    
        # build y sparse obsticle map
        # build x sparse obsticle map



def range_around(i,sl,mini,maxi):
    # find range
    # input of a sorted list of int. and a number.
    # find the number below and above that number.
    if len(sl)==0:
        return (None,None)
    assert(i>=mini )
    assert(i <= maxi )
    #TODO
    l=None
    h=None
    for a in sl:
        assert (i != a)
        if a < i:
            l = i
        if not(h):
            if a > i:
                h = a
                return l,h
    return l,h        
    
mm=Map(s)
    
while mm.move():
    pass
print(mm.countDistinct())



s = [list(x) for x in read_input()]
mm=Map(s)
    
while mm.move():
    pass
print(mm.countDistinct())


tst= [  ''' ''',
        ''' ''']

#
#  def 