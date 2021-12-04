testinput='''forward 5
down 5
forward 8
up 3
down 8
forward 2'''
x=testinput.splitlines()
print(x)    

start=[0,0]
def move(pos, cmd):
    direction, distance = cmd.split()
    if direction == 'forward':
       pos[0]=pos[0]+ int(distance)
    elif direction == 'up':        
       pos[1] = pos[1] - int(distance)
       #pos[1] = max(pos[1],0)
    elif direction == 'down':
       pos[1]=pos[1] + int(distance)
    else:
        print("ouch ", direction)
    return pos

cursor=[0,0,0]
for cmd in x:
    move(cursor,cmd)

print (cursor[0]*cursor[1])
input = open('input2.1.txt','r').readlines()
cursor=[0,0]
cursor=[0,0,0]
for cmd in x:
    move(cursor,cmd)
print (cursor[0]*cursor[1])


cursor=[0,0,0]
def move(pos, cmd):
    direction, distance = cmd.split()
    if direction == 'forward':
       pos[0]=pos[0]+ int(distance)
       pos[1]=pos[1] + pos[2] * int(distance)
    elif direction == 'up':        
       pos[2] = pos[2] - int(distance)
       #pos[1] = max(pos[1],0)
    elif direction == 'down':
       pos[2]=pos[2] + int(distance)
    else:
        print("ouch ", direction)
    return(pos)


cursor=[0,0,0]
for cmd in input:
    move(cursor,cmd)
print (cursor[0]*cursor[1])
