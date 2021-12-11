
tstinput='''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
'''

realinput = '''1443668646
7686735716
4261576231
3361258654
4852532611
5587113732
1224426757
5155565133
6488377862
8267833811
'''
import numpy as np
import pprint



def getarray(txt):
    lines=txt.splitlines()
    x=[]
    for line in lines:
        r = [int(i) for i in line]
        #print(r)
        x.append(r)
    return(np.array(x))

def inMap(map,r,c):
    r1,c1 = map.shape
    return r>=0 and c >=0 and r < r1 and c < c1



def flash(map, r,c ,flashlist):
    global flashcnt
    if (map[r][c] > 9 ) and ( (r,c) not in flashlist):
        flashlist.append((r,c))
        flashcnt += 1
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if (abs(i) +abs(j)) > 0:
                    if inMap(map,r+i,c+j):
                        #print(r,c,i,j)
                        map[r+i][c+j]+=1
                        flash(map,r+i,c+j,flashlist)
    return map
            

                
fc=0

def step(m):
    m = m+1
    global fc
    flashlist=[]
    for r in range(10):
       for c in range(10):
           flash(m,r,c,flashlist)
    
    for pt in flashlist:
        r,c = pt
        m[r][c]= 0 
    fc= len(flashlist)
    return m

flashcnt = 0

m = getarray(realinput)
# m = getarray(tstinput)

rtn =0 
while fc < 100:

#for k in range(100):
    m = step(m)
    rtn += 1
    #print(fc)


print(m)
print()

print(flashcnt)        
print(rtn)