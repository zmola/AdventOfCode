

from collections import deque
from pprint import pprint

realinput= open('input.10.txt','r',newline='\n')  
lines=[x.strip() for x in realinput.readlines()]

tstinput = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
'''
#lines=[x.strip() for x in tstinput.splitlines()]
#pprint(lines)

openchars=('(', '{', '[', '<')
closechars=(')', '}', ']', '>')
lookup=dict(zip(closechars,openchars))
score={')':3, 
       ']':57,
       '}': 1197,
       '>':25137 }

def isNotValid(line):
    stk = deque()
    stk2 = deque()
    for c in line:
       if c in openchars:
          stk.append(c)
       elif c in closechars:
          d = stk.pop()
          # print(c,d)
          if lookup[c] != d : 
              return c
       else:
           print("really bad")
    return False


def fix(line):
    stk = deque()
    for c in line:
       if c in openchars:
          stk.append(c)
       elif c in closechars:
          d = stk.pop()
       else:
           print("really bad")
    return stk
# isValid(lines[0])
fscore=0
for line in lines:
    c=isNotValid(line)
    if c:
        print(c)
        fscore = fscore + score[c]

print('part1: ',fscore)
lines = [l for l in lines if not isNotValid(l)]

score2 = {
    '(': 1 ,   
    '[': 2 ,
    '{': 3 ,
    '<': 4 }

result=[]
for line in lines:
    fscore=0
    f =fix(line)
    #rint (line, '    ', f)
    while len(f):
        fscore= 5*fscore + score2[f.pop()]
    result.append(fscore)

r = sorted(result)
print(r[int(len(r)/2)])
