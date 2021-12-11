
from pprint import pprint
tstinput='''2199943210
3987894921
9856789892
8767896789
9899965678
'''

tstmap=[]
lines=tstinput.splitlines()
for l in lines:
    line=[]
    for c in l:
        line.append(int(c))
    tstmap.append(line)

pprint(tstmap)

tstnrows=len(tstmap)
tstncols=len(tstmap[0])

pprint(f"({tstnrows}, {tstncols})")


import numpy as np
map=[]

realinput= open('input.09.1.txt','r',newline='\n')  
lines=[x.strip() for x in realinput.readlines()]
for l in lines:
    line=[]
    for c in l:
        line.extend([int(c)])
    map.append(line)

#pprint(map)
npmap=np.array(map)

nrows=len(map)
ncols=len(map[0])

#pprint(f"({nrows}, {ncols})")


# def ismin(r,c,map,nrows,ncols):
#     result=True
#     for rr in range(max(0,r-1),min(nrows,r+2)):
#         for cc in range(max(0,c-1),min(ncols,c+2)):
#             #print(r,c,rr,cc)
#             if (rr != r) or (cc != c):
#                 #print("loop: ",r,c,rr,cc)
#                 if map[rr][cc] <= map[r][c]:
#                     #print('     notmin',rr,cc,r,c,map[rr][cc],map[r][c])
#                     return False

#     return(True)


def ismin(r,c,map,nrows,ncols):
    result=True
    if r > 0: 
       if map[r-1][c] <= map[r][c]: 
           return False
    if c > 0:
       if map[r][c-1] <= map[r][c]: 
           return False
    if r < nrows -1: 
       if map[r+1][c] <= map[r][c]: 
           return False
    if c < ncols -1 :
       if map[r][c+1] <= map[r][c]: 
           return False


    return(True)

#results=[0]*ncols *nrows 


# measure=0
# for r in range(nrows):
#     for c in range(ncols):
#         if ismin(r,c):
#             print("ismin",r,c,map[r][c])
#             results.append((r,c,map[r][c]))
#             measure += map[r][c] +1



def getMeasure(tstmap, tstnrows, tstncols):
    measure=0
    results=[]
    for r in range(tstnrows):
        for c in range(tstncols):
            if ismin(r,c,tstmap,tstnrows,tstncols):
#                print("ismin",r,c,tstmap[r][c])
                measure += tstmap[r][c] +1
                results.append((r,c,tstmap[r][c],measure))
    return results

tstmeasure = getMeasure(tstmap, tstnrows, tstncols )
#print(measure)
measure = getMeasure(npmap, nrows, ncols )
#print(measure)

#pprint(results)
from collections import defaultdict
def fill(map,r,c,nrows,ncols,fval=100):

    myval = map[r][c]
    map[r][c]=fval
    result = [(r,c)]

    if r > 0: 
        v = map[r-1][c] 
        #print('a',(r,c))
        if v < 9 and map[r-1][c] >= myval : 
           result = result+ fill(map,r-1,c,nrows,ncols,fval)

    if c > 0:
        #print('b',(r,c))
        v = map[r][c-1]         
        if v < 9 and v >=  myval: 
           result = result + fill(map,r,c-1,nrows,ncols,fval)
    if r < nrows -1: 
        #print('c',(r,c))
        if map[r+1][c] < 9 and map[r+1][c] >= myval: 
           result = result + fill(map,r+1,c,nrows,ncols,fval)
    if c < ncols -1:
       #print('d',r,c)
       if map[r][c+1] < 9 and map[r][c+1] >= myval: 
           result = result + fill(map,r,c+1,nrows,ncols,fval)
    return result


# k = np.array(tstmap)
# print(k)
# fill(k, 0,1,5,10,99)

# tstmeasure
# fill(k,0,9,5,10,98)
# fill(k,2,2,5,10,97)

def part2(tstmap, tstnrows, tstncols, tstmeasure):
    results = {}
    color=100
    for result in tstmeasure:
        r = result[0]
        c = result[1]
        basinsize=fill(tstmap,r,c,tstnrows,tstncols,color)
        results[color]= basinsize
    #print(basinsize)
        color +=1

    print(len(results))

    basins = results.values()
    basin_sizes= [len(x) for x in basins]


    x=sorted(basin_sizes,reverse = True)
    print(x[0:3])
    print(x[0]* x[1] * x[2])
# tmap=np.array(tstmap)
    # pprint (tmap)

part2(npmap, nrows,ncols, measure)