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
    
    def __str__(self):
        return(f"({self.x},{self.y})")
    
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

    def __init__(self,m):
        self.m=copy.deepcopy(m)
        (y,x,dirchar) = self.findstart()
        self.startpoint=Point(x,y)
        self.guard=Guard(Point(x,y),Point(0,-1))
        self.mark(self.guard.pos)
        self.maxx = len(m[0])-1
        self.maxy = len(m)-1
        self.cycleCount = 0
        self.cycle = []
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
        if self.pointoutside(newp):
            return False 
        if self.charAt(newp)  == '#':
            self.guard.turnright()
            self.move()
        else:
            self.guard.move()
            self.mark(self.guard.pos)
            self.stepcnt +=1
            # self.causes_cycle()
        return True
    
    def testmove(self,guard):
        newp = guard.nextStep()
        if self.pointoutside(newp):
            return False 
        if self.charAt(newp)  == '#' or newp == self.baricade:
            # print(guard.dir)
            guard.turnright()
            # print(guard.dir) 
        guard.move()
        return True
    
    def causes_cycle_old(self):
        # if right turn here puts me into a cycle, add position to cycle list
        newGuard = copy.deepcopy(self.guard)
        newGuard.name='newGuard'
        originalGuard = copy.deepcopy(self.guard)
        originalGuard.name='originalGuard'
        firstTime=True
        self.baricade = newGuard.nextStep()
        newGuard.turnright()
        guardset=set()
        guardset.add(originalGuard.__repr__())

        while True:
            # if self.stepcnt == 532:
            #     print(newGuard.pos,newGuard.dir,len(guardset))
            if self.pointoutside(newGuard.nextStep()):
                return False
            firstTime = False
            x = self.testmove(newGuard)
            if not(x):
                print('ouch', newGuard, originalGuard)
            if newGuard.__repr__() in guardset: 
                self.cycleCount += 1
                self.cycle.append(self.guard.nextStep())
                return True
            guardset.add(newGuard.__repr__())
             

    def run(self):
        while self.move():
            pass
        x=set([(p.x,p.y) for p in self.cycle])
        x.discard((self.startpoint.x,self.startpoint.y))
    
        print(self.countDistinct(),self.cycleCount, len(x), self.stepcnt)
        #old_p = self.blocklist[0] 



Map(s).run()
    
s = [list(x) for x in read_input()]
ss = Map(s)
ss.run()
    
olist = list()
def buildList(m):
    global olist
    for j in range(len(m)):
        for i in range(len(m[j])):
            if m[j][i]=='X':
               olist.append((i,j))

#TODO: make run capture the cycles
# TODO: store guard locations for where you have been, to capture cycles.
# TODO: dedup cycle list, remove startpoint


# TODO: for every obsticle location, run the map.
#       if obsticle causes cycle, add 1 to cycle count
        
buildList(ss.m)
olist.sort()
olist.remove((ss.startpoint.x,ss.startpoint.y))
print('olsit.len:',len(olist))
i=0
# for x,y in olist:
#   print(i)
#   t=copy.deepcopy(s)
#   t[y][x]='#'
#   tt=Map(t)
#   i=i+1