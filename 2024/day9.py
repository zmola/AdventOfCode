import copy
import itertools
import collections
from pprint import pprint
from fractions import Fraction
import operator
from functools import reduce

day = 9
part = 1


def read_input(day=day,part=part):
   f = open(f"input/{day}.{part}.txt")
   return f.read()



def parse_intlist_line(l):
    return [int(x) for x in l.split()]

def parse_intlist(lines):
    for l in lines:
        yield parse_intlist_line(l)

def psub(p,q):
    return (p[0]-q[0],p[1]-q[1])

def padd(p,q):
    return (p[0]+q[0],p[1]+q[1])


samp='''2333133121414131402'''
s = samp

def build_file(i,b,f):
    return([i]*b+[-1]*f)

def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return zip(a, a)

def build_disk(input):
    disk = []
    i = 0 
    pos = 0
    inp = [int(x) for x in list(input)]
    lastb=inp[-1]
    for b,f in pairwise(inp):
       # print(i,b,f)
       disk = disk + build_file(i,b,f)
       i = i +1 
    disk = disk + build_file(i,lastb,0)
    return disk

# s = read_input()

dm = build_disk(s)
dm0 = copy.deepcopy(dm)

print('crc dm0 ',crc(dm0))
# print(dm)

def mov(dm):
    front=0
    back = len(dm)-1
    while back >= front:
        while dm[back] == -1:
            back -= 1
        while dm[front] != -1:
            front += 1

        dm[front] = dm[back]
        dm[back] = -1

mov(dm)
dm1= copy.deepcopy(dm)
print('dm1 =',dm1)    

def crc(dm):
    # d = [x for x in copy.deepcopy(dm) if x >= 0]
    crcv=0
    for i,x in zip(range(len(dm)),dm):
        if x != -1:
           crcv = crcv + i * x 
    return crcv

print('crc dm1 ',crc(dm))

def build_freemap(input):
    i = 0
    freemap= collections.defaultdict(list)
    freespace_list = []
    diskmap = dict()
    inp = [int(x) for x in list(input)]
    inp.append(0) 
    blk=0
    for b,f in pairwise(inp):
       diskmap[i]=(i,b,blk)
       i=i+b
       if f>0:
         freemap[f].append(i)
         freespace_list.append((i,f))
       i = i + f
       blk += 1
    freespace_list.sort()
    return(freemap,diskmap, i, freespace_list)



freemap,diskmap,l, fsl = build_freemap(s)
print(freemap)
print(diskmap)
print(l)   
print(fsl)

def expand_dm(cdm,l):
   dm = [-1] * l
   for k,v in cdm.items():
       for i in range( v[0],v[0]+v[1]):
           dm[i]=v[2]

   return dm

dm2 = expand_dm(diskmap,l)
print(dm2)

def findfirstblock(fsl,l,maxl):
    for i in range(len(fsl)):
       if fsl[i][1] >= l:
           return i
       if i > maxl:
           return maxl
    return maxl + 100

def findBlocksAround(fsl,pos,maxl):
    keys=fsl.keys()
    keys.sort()
    old_lower = None
    for k in keys:
        if k < pos: 
            old_lower = k
        else:
            return(old_lower,k)
    return(old_lower,None)

def wow(cdm,fsl,l):
    keys = list(cdm.keys())
    keys.sort(reverse=True)
    cdm2=copy.deepcopy(cdm)
    for k in keys:
        L = cdm2[k][1]
        b = cdm2[k][2]
        start = cdm2[k][0]
        freeBlk= findfirstblock(fsl,L,start)
        #print('ffb', freeBlk, L, start,b,fsl )
        if  freeBlk < start:
            ffb = fsl[freeBlk]
            #print('swp', freeBlk,L,b,ffb,k)
            ffb = fsl[freeBlk]
            cdm2[ffb[0]]=(ffb[0],L,b)
            cdm2.pop(k)
            fsl[freeBlk]=(ffb[0]+L,ffb[1]-L)
            
    return cdm2,fsl

cdm2,fsl2 = wow(diskmap,fsl,l)

dm3=expand_dm(cdm2,l)
crc2=crc(dm3)
dm3 = [max(0,x) for x in dm3]
print(dm3)
print("crc dm3", crc2)