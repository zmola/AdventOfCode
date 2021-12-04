

tstinput='''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''.splitlines()


lines = tstinput
input = open('input.3.1.txt','r').readlines()
lines = [x.strip for x in input ]
digits = len(lines[0])

def calcfreq(lines):
    freq=[]
    for i in lines[0]:
        freq.append(0)

    cnt=0
    for r in lines:
        cnt +=1
        for i in range(len(r)):
          if r[i] == '1':
              freq[i] +=1
    return freq,cnt

freq, cnt = calcfreq(lines)

gamma=0
mask=0
for i in range(len(lines[0])):
    if (((freq[i]*1.0/cnt) -.5) > 0): 
        gamma +=1
    mask += 1 
    mask *= 2
    gamma = gamma * 2 
gamma = int(gamma / 2)
mask = int(mask/2)

epsilon = mask & ~ gamma  

epsilon * gamma



def calcfreqchar(freq, cnt):
    freqi = [round(1 + x/cnt)-1 for x in freq]

    j = 0
    for x in freqi:
        j *= 2
        j +=x 
    freqj=j
    freqchr= [ str(x) for x in freqi]
    return freqj,freqchr

freq, cnt = calcfreq(lines)
freqj, freqchr = calcfreqchar(freq, cnt)


linesi= [int(x,2) for x in lines]
measure = [ (x  &  freqj) for x in linesi]
v =max(measure)
for ll in zip(linesi,measure):
    
    if ll[1] == v:
        rtn = ll
        print(ll)

o2=rtn[0]

lines=tstinput
lines = [x.strip() for x in input ]
digits = len(lines[0])


for i in range(digits):
    freq, cnt = calcfreq(lines)
    freqj, freqchr = calcfreqchar(freq, cnt)

    newlines=[]
    for l in lines:
       if l[i]==freqchr[i]:
           rtn=l
           print(l,freqchr[i],i)
           newlines.append(l)
    lines=newlines
print(newlines)
o2=int(rtn,2)



lines=tstinput
lines=input
lines = [x.strip() for x in input ]
digits = len(lines[0])

for i in range(digits):
    freq, cnt = calcfreq(lines)
    freqj, freqchr = calcfreqchar(freq, cnt)

    newlines=[]
    for l in lines:
       if l[i]!=freqchr[i]:
            rtn=l
            print(l,freqchr[i],i)
            newlines.append(l)
    lines=newlines
print(newlines)
co2=int(rtn,2)

print(o2*co2)
