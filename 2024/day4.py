

samp='''..X...
.SAMX.
.A..A.
XMAS.S
.X....'''

samp2='''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''

day=4
part=1
def read_input(day=day,part=part):
   f = open(f"input/{day}.{part}.txt")
   return [l.strip() for l in f.readlines()]


def searchit( aListOfStrings):
    cnt=0
    input= aListOfStrings
    X = len(input)
    Y = len(input[0])

    def check(i,j):
        nonlocal cnt
        #print("pos: i,j,cnt",i,j,cnt)      
        for dx in [-1,0,1]:
            if i+3*dx <0 or i+3*dx >= X:
                continue
            for dy in [-1,0,1]:      
                if j+3*dy <0 or j+3*dy >= Y:
                    continue
                #print(dx,dy)
                try:
                    if input[i+1*dx][j+1*dy]=='M':
                        if input[i+2*dx][j+2*dy] == 'A':
                            if input[i+3*dx][j+3*dy] == 'S':
                                # print(i,j)
                                cnt = cnt+1
                except e:
                    # print(e)
                    continue


    for i in range(X):
        for j in range(Y):
            if input[i][j] == 'X':
                check(i,j)

    print(cnt)

searchit([ list(l.strip()) for l in samp.split('\n')])
searchit([ list(l.strip()) for l in samp2.split('\n')])
searchit(read_input())

def searchit2( aListOfStrings):
    cnt=0
    input= aListOfStrings
    X = len(input)
    Y = len(input[0])

    def check(i,j):
        nonlocal cnt
        # print("pos: i,j,cnt",i,j,cnt)      
        for dx in [1,-1]:
            for dy in [-1,1]:      
                # print(dx,dy)
                if input[i+dx][j+dy]=='M':
                    if input[i-dx][j-dy] == 'S':
                        if input[i-dx][j+dy]=='M':
                            if input[i+dx][j-dy] == 'S':
                                cnt = cnt+1 
                                #print("xmas: ",i,j)
                if input[i+dx][j+dy]=='S':
                    if input[i-dx][j-dy] == 'M':
                        if input[i-dx][j+dy]=='M':
                            if input[i+dx][j-dy] == 'S':
                                cnt = cnt+1 
                                #print("xmas: ",i,j)


    for i in range(1,X-1):
        for j in range(1,Y-1):
            if input[i][j] == 'A':
                check(i,j)

    print(cnt/2.0)

samp='''M.S
.A.
M.S'''

samp2='''.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........'''

samp3='''S.S
.A.
M.M'''

samp4='''M.M
.A.
S.S'''

samp5='''S.M
.A.
S.M'''


searchit2([ list(l.strip()) for l in samp.split('\n')])
searchit2([ list(l.strip()) for l in samp2.split('\n')])
searchit2([ list(l.strip()) for l in samp3.split('\n')])
searchit2([ list(l.strip()) for l in samp4.split('\n')])
searchit2([ list(l.strip()) for l in samp5.split('\n')])
searchit2(read_input())
