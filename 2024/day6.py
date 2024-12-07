import copy

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


class Map:
    def mark(self,p):
        self.m[p.y][p.x] = 'X'

    def __init__(self,m):
        self.m=copy.deepcopy(m)
        (y,x,dirchar) = self.findstart()
        self.guard=Guard(Point(x,y),Point(0,-1))
        self.mark(self.guard.pos)
        self.maxx = len(m[0])-1
        self.maxy = len(m)-1
        self.cycleCount = 0
        self.cycle = []
        self.stepcnt=0

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
        if self.stepcnt % 300 == 0:
            print(self.stepcnt)
        newp = self.guard.nextStep()
        if self.pointoutside(newp):
            return False 
        if self.charAt(newp)  == '#':
            self.guard.turnright()
            self.move()
        else:
            self.guard.move()
            self.mark(self.guard.pos)
            self.stepcnt +=1
            # if False and self.causes_cycle():
            if self.causes_cycle():
               self.cycleCount += 1
               self.cycle.append(self.guard.nextStep()) 
        return True
    
    def testmove(self,guard):
        newp = guard.nextStep()
        if self.pointoutside(newp):
            return False 
        if self.charAt(newp)  == '#':
            # print(guard.dir)
            guard.turnright()
            # print(guard.dir) 
        guard.move()
        return True
    
    def causes_cycle(self):
        # if right turn here puts me into a cycle, add position to cycle list
        newGuard = copy.deepcopy(self.guard)
        newGuard.name='newGuard'
        originalGuard = copy.deepcopy(self.guard)
        originalGuard.name='originalGuard'
        firstTime=True
        newGuard.turnright()
        guardset=set()
        

        while True:
    
        #for i in range(100:
            # print(newGuard.pos, self.guard.pos)
            if newGuard.__repr__() in guardset: 
                return(True)
            guardset.add(newGuard.__repr__())
            if self.pointoutside(newGuard.nextStep()):
                return False
            if newGuard == originalGuard and not firstTime:
                return True
            firstTime = False
            x = self.testmove(newGuard)
            if not(x):
                print('ouch', newGuard, originalGuard)


    def run(self):
        while self.move():
            pass
        print(self.countDistinct(),self.cycleCount, self.stepcnt)



Map(s).run()
    
s = [list(x) for x in read_input()]
ss = Map(s)
ss.run()
    

        
# from collections import defaultdict

# class ObsticalMap():
#     def __init__(self,m):
#         self.obsticles=[]
#         self.yobsticles = defaultdict(list)
#         self.xobsticles = defaultdict(list)
#         for y in range(len(m)):
#             for x in range(len(m[y])):
#                 self.obsticles.append(Point(x,y))
#                 self.yobsticles[y].append(x)
#                 self.xobsticles[x].append(y)
#         # sorting probably not necessary
#         for k,v in self.yobsticles:
#             v.sort()
#         for k,v in self.xobsticles:
#             v.sort()
#         self.m=m
#         self.maxx = len(m[0])-1
#         self.maxy = len(m)-1
    
#         # build y sparse obsticle map
#         # build x sparse obsticle map



# def range_around(i,sl,mini,maxi):
#     # find range
#     # input of a sorted list of int. and a number.
#     # find the number below and above that number.
#     if len(sl)==0:
#         return (None,None)
#     assert(i>=mini )
#     assert(i <= maxi )
#     #TODO
#     l=None
#     h=None
#     for a in sl:
#         assert (i != a)
#         if a < i:
#             l = i
#         if not(h):
#             if a > i:
#                 h = a
#                 return l,h
#     return l,h        
    