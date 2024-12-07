import copy
import operator
import itertools

day=7
part=1

def read_input(day=day,part=part):
   f = open(f"input/{day}.{part}.txt")
   return [l.strip() for l in f.readlines()]


def parse_intlist_line(l):
    return [int(x) for x in l.split()]

def parse_intlist(lines):
    for l in lines:
        yield parse_intlist_line(l)



samp = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''.split('\n') 

s = [ x.split(':') for x in samp]
s = [ x.split(':') for x in read_input()]
ss = [ (int(x[0]),x[1].strip()) for x in s]
sss= [(x[0],x[1].split()) for x in ss]
s4= [(x[0],[int(y) for y in x[1]]) for x in sss]

def add(x,y):
    return x+y

def sevencat(a,b):
    return int(str(a)+str(b))

def test_perm(oplist,operands):
    rtn=operands.pop(0)
    #print(oplist, rtn, operands)
    for op in oplist:
        # print(op, operands)
        rtn = op(rtn,operands.pop(0))
    return rtn

def testrow(r,operands):
    op_cnt= len(operands)-1
    oplist=[operator.add, operator.mul, sevencat]
    opperm = [ x for x in itertools.product(*([oplist]*op_cnt))]
    for mull in opperm:
        ops = copy.deepcopy(operands)
        x=test_perm(mull,ops)
        if x == r:
            return True
    return False

s5=[]
i=0
for row in s4:
    print (i)
    if testrow(row[0],row[1]):
        s5.append(row[0])
    i+=1
# s5 = [ row[0] for row in s4 if testrow(row[0],row[1])]
print(sum(s5))