# 0,6  a,b,c,e,f,g
# 1,2
# 2,5
# 3,5
# 4,4
# 5,5
# 6,6
# 7,3
# 8,7
# 9,6

# 1   c, f
# 4   b,c,d,f
# 7   a,c,f
# 8   a,b,c,d,e,f,g


# check that we have digits 1,7
#  we have 1,7,4,8  *len 2,3,4,7
#  length 6  Iis either 0, 6 or 9, but 
#             6 doess not contain c (1 is not a subset of 6, 1 is  a subsest of 0 and 9)
#             4 union 7 = 9 
#             0 is left
# length 5: 2,3,5
#           1 is a subset of 3 and not a subset of 2,5
#           4-1 is a subset of 5 (and not 2)

# four union seven = nine

tstinput = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |fgae cfgab fg bagce
'''

input=tstinput
realinput= open('input.8.1.txt','r',newline='\n')

linest= [x.strip().split('|')[1].strip().split() for x in  input.splitlines()]
linesr= [x.strip().split('|')[1].strip().split() for x in  realinput.readlines()]




def part1(lines):
    lengths=[]
    for l in lines:
        for d in l:
            ld=len(d)
            if ld in (2,4, 3,7):
               lengths.append(ld)
    return(len(lengths))    
    #print(lengths)        
    #len(lengths)

print(part1(linest))
print(part1(linesr))
# -------------------
# part2

class Digit:

    def __init__(self,s):
        self.inputstring=s
        

# def finda(): 
  
realinput= open('input.8.1.txt','r',newline='\n')  
data = [[x.strip().split('|')[0].strip().split() for x in  input.splitlines()],[x.strip().split('|')[1].strip().split() for x in  input.splitlines()]]
data3a= [ [x.strip().split('|')[0].strip().split(),x.strip().split('|')[1].strip().split() ] for x in  realinput.readlines()]

data2=[]
for l,v in zip(*data):
    #print(l,v)
    data2.append((l,v))
    for i in range(len(l)):
        l[i]=set(l[i])
    for i in range(len(v)):
        v[i]=set(v[i])

data3=[]
for l,v in data3a:
    #print(l,v)
    
        data3.append((l,v))
    for i in range(len(l)):
        l[i]=set(l[i])
    for i in range(len(v)):
        v[i]=set(v[i])


sum_results=0
for l,v in data3:

    digitmap={}
    LENFIVE=[]
    LENSIX=[]
    ONE=5.4
    SEVEN=5.4
    FOUR=5.4
    NINE=5.4

    digitsource= l+v
    answersource= v
    for digit in digitsource:
        if len(digit)==2:
           digitmap[repr(sorted(digit))]=1
           ONE= digit
        elif len(digit)==3:
           digitmap[repr(sorted(digit))]=7
           SEVEN=digit
        elif len(digit)==4:
           digitmap[repr(sorted(digit))]=4
           FOUR=digit
        elif len(digit)==7:
           digitmap[repr(sorted(digit))]=8
        elif len(digit)==5:
           LENFIVE.append(digit)
        elif len(digit)==6:
            LENSIX.append(digit)
        else:
            print("ERROR, ",digit)
    for digit in LENSIX:
        if len(ONE.intersection(digit)) == 1:
            digitmap[repr(sorted(digit))]=6
            SIX=digit
        elif len(FOUR.intersection(digit)) == 4:
            digitmap[repr(sorted(digit))]=9
            NINE=digit
        else:
            digitmap[repr(sorted(digit))]=0
    for digit in LENFIVE:
        if FOUR.difference(ONE).issubset(digit):
            digitmap[repr(sorted(digit))]=5
        elif len(ONE.intersection(digit))==2:
            digitmap[repr(sorted(digit))]=3
        else: 
            digitmap[repr(sorted(digit))]=2
    value=0
    for d in v:
      vv=digitmap[repr(sorted(d))]
      value=value*10+vv
    print(value,answersource)
    sum_results+=value

print(sum_results)
              



    #print(digitmap)
        
    # check that we have digits 1,7
#  we have 1,7,4,8  *len 2,3,4,7
#  length 6  Iis either 0, 6 or 9, but 
#             6: len (6.union(1))==1 doess not contain c (1 is not a subset of 6, 1 is  a subsest of 0 and 9)
#             9: len(9.union(4) = 4 
#             0: len(0.union(4)) == 3
# length 5: 2,3,5
#           1 is a subset of 3 and not a subset of 2,5
#           4-1 is a subset of 5 (and not 2)

# four union seven = nine

    


