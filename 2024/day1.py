
day=1

part=1

def read_input(day=day,part=part):
   f = open(f"input/{day}.{part}.txt")
   return [l.strip() for l in f.readlines()]


def parse_intlist_line(l):
    return [int(x) for x in l.split()]

def parse_intlist(lines):
    for l in lines:
        yield parse_intlist_line(l)

a = []
b = [] 

a,b = list(zip(*parse_intlist(read_input())))
a=list(a)
b=list(b)

a.sort()
b.sort()
d=[]
for i in range(len(a)):
    d.append( abs(a[i]-b[i]))


print(sum(d))

dd={}
for i in b:
    x = dd.get(i,0)
    dd[i] = x+1

a2=[]   
for i in a:
    a2.append(dd.get(i,0)*i)

print(sum(a2))
