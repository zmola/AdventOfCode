import copy
import itertools
import collections
from pprint import pprint
from fractions import Fraction

day = 8
part = 1


def read_input(day=day,part=part):
   f = open(f"input/{day}.{part}.txt")
   return [l.strip() for l in f.readlines()]


def parse_intlist_line(l):
    return [int(x) for x in l.split()]

def parse_intlist(lines):
    for l in lines:
        yield parse_intlist_line(l)

def psub(p,q):
    return (p[0]-q[0],p[1]-q[1])

def padd(p,q):
    return (p[0]+q[0],p[1]+q[1])

def findAnti_1(p,q,m):
    diff=psub(p,q)
    rtn=[]
    rtn.append(psub(q,diff))
    rtn.append(padd(p, diff))
    return rtn


samp ='''............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............'''.split('\n')

s = [list(x) for x in samp]
#s = [list(x) for x in read_input()]
# pprint(s)

ants = collections.defaultdict(list)
for j in range(len(s)):
    for i in range(len(s[0])):
        if s[j][i] != '.':
            ants[s[j][i]].append((i,j))
#pprint(ants)
#pprint(s)

# def 
antcombos = dict()
for k,v in ants.items():
    print(k,v)
    antcombos[k]= list(itertools.combinations(v,2))

pprint(antcombos)
#print(ants[0])

antAnti = collections.defaultdict(set)


import operator
from functools import reduce

def insideMap(m,p):
    # m is a list of lists (array)
    # p is tupple (point)
    rtn = p[0] >= 0 and p[1] >= 0
    rtn = rtn and p[0] < len(m[0])  and p[1] < len(m) 
    return rtn
    

for k,v in antcombos.items():
    print(k,v)
    x=  [findAnti_1(*x,s) for x in v]
    x = reduce(operator.add,x)
    print(k,":  ", x)
    antAnti[k] = [xx for xx in x if insideMap(s,xx)]

pprint(antAnti)
nodes = list()
for k,v in antAnti.items():
    nodes = nodes + v
n=list(nodes)
print(len(n),n)
nn=set(n)
print(len(nn),nn)

