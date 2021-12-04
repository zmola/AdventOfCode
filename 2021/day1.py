


input=[199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263]

input = open('input.1.1.txt','r').readlines()
input2 = [ int(x) for x in input]
print (len(input))
prev=input[0]
output=0
for i in range(1,len(input)):
   if input[i-1] < input[i]:
       output += 1


print(output)


data=input
output=0
oldwindow= data[0]+data[1]+data[2]
for i in  range(3,len(data)):
   newwindow= oldwindow - data[i-3] + data [i]
   if oldwindow < newwindow:
       output += 1
   oldwindow=newwindow

print(output)