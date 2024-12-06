

samp="xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

import re
def parsemul(s):
    x = re.findall('[0-9][0-9]?[0-9]?',s)
    return(int(x[0]) * int(x[1]))
x = re.findall("mul\\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\\)",samp)
print(x)

y= [ parsemul(i) for i in x]
print(y)
print(sum(y))

with open('input/3.1.txt', 'r') as file:
    data = file.read()

x = re.findall("mul\\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\\)",data)
y= [ parsemul(i) for i in x]
print(sum(y))

samp2 = r"xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
s = samp2.split("don't")
print(s)
s = data.split("don't")
newstr=s[0]
for sss in s:
    tmp = sss.split('do',1)
    if len(tmp)> 1:
        newstr = newstr +  tmp[1]

x = re.findall("mul\\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\\)",newstr)
# print(x)

y= [ parsemul(i) for i in x]
# print(y)
print(sum(y))


