
from collections import defaultdict
samp='''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''
#
# sample
input=samp.split('\n\n')
print(input)
# from file 
day=5
part=1

def read_input(day=day,part=part):
   f = open(f"input/{day}.{part}.txt")
   return f.read()

input = read_input().split('\n\n')


rules=input[0].split('\n')
rulelist=defaultdict(set)  # items that have to be after key
for l in rules:
    f,s=l.split('|')
    rulelist[f].add(s)
updates=input[1].split('\n')
updatelist = [ u.split(',') for u in updates ]

def updateok(update,rulelist):
    #print()
    for i in range(1,len(update)) :
        a = rulelist[update[i]]
        #print('a, u,p, i=',a,update[i],update[0:i],i)
        v=a.intersection(set(update[0:i]))
        if v:
            return False
    return True

#print([updateok(u,rulelist) for u in updatelist])
ok = [ u for u in updatelist if updateok(u,rulelist) ]
for u in ok:
    if (len(u)%2)==0 :
        print('u doesnt have a middle element',u)

me= [int(u[len(u)//2]) for u in ok ]
print(sum(me))   

nok = [ u for u in updatelist if not updateok(u,rulelist) ]
a = nok[1]
rulelistbefore=defaultdict(set)  # items that have to be before key
for l in rules:
    f,s=l.split('|')
    rulelistbefore[s].add(f)

def cmp(a,b):
    ra = rulelist[a]
    rb = rulelist[b]
    agtb = a in rb 
    bgta = b in ra
    if agtb and bgta :
        print("oops,ab",a,b)
        return(0)
    if agtb:
        return -1
    if bgta:
        return 1
    return 0

from functools import cmp_to_key
keyfun =cmp_to_key(cmp)
for l in nok:
    l.sort(key=keyfun,reverse=True)
    # print(l)

me= [int(u[len(u)//2]) for u in nok ]
print(sum(me))   


