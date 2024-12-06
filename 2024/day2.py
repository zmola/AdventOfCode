
day=2

part=1

def read_input(day=day,part=part):
   f = open(f"input/{day}.{part}.txt")
   return [l.strip() for l in f.readlines()]


def parse_intlist_line(l):
    return [int(x) for x in l.split()]

def parse_intlist(lines):
    for l in lines:
        yield parse_intlist_line(l)


sample='''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''

s= sample.split('\n')
print(s)

ss= list(parse_intlist(s))
print(list(ss))
def sgn(x):
    return -1 if x < 0 else 1;

def report_ok(r):
    ok=len(r)>1
    s = sgn(r[1]-r[0])
    t1 = True
    t2 = True
    for i in range(1,len(r)):
        t1 = t1 and (s == sgn(r[i]-r[i-1]))
        t2 = t2 and abs(r[i]- r[i-1]) in [1,2,3]
    return t1 and t2

print ( [report_ok(r) for r in ss])
        
input1= list(parse_intlist(read_input()))
xx = [r for r in ss if report_ok(r)]
xx = [r for r in input1  if report_ok(r)]
print ('p1', len(xx))


def report_ok_drop(r,x):
    print("rod: ",r,x)
    ok=len(r)>1
    s = sgn(r[1]-r[0])
    t1 = True
    t2 = True
    oldi=0 
    if x == 0:
        s = sgn(r[2]-r[1])
        oldi = 1
        return( report_ok (r[1:]))
    if x == 1: 
        s = sgn(r[2]-r[0])
        
        
    for i in range(1,len(r)):
        if x == i:
            pass
        else: 
            t1 = t1 and (s == sgn(r[i]-r[oldi]))
            t2 = t2 and abs(r[i]- r[oldi]) in [1,2,3]
            print(i,r[i],t1,t2, r[i],r)
            oldi = i
    if t1 and t2:
        return True
    else:
        return False
    
    
def report_ok_2(r):
    t = report_ok(r)
    j = 0
    while not(t) and (j <= len(r)):
        t = report_ok_drop(r,j)
        j = j+1
        
    return t

xx = [r for r in ss if report_ok_2(r)]
print(xx)
xxx = [r for r in input1  if report_ok_2(r)]
print(len(xxx))


tst1 = [0, 1,2,3 ]
tst2 = [ 0, -1, 2, 3]
tst3 = [ 3, 1, 2, 3 ]