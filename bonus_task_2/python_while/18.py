x = int(input())
thislist = []
while x != 0:
    thislist.append(x)
    x = int(input())
    
avg = sum(thislist)/len(thislist)
sum = 0
for i in thislist:
    sum += (i-avg)**2
sum = ( sum/(len(thislist)-1) )**0.5
print(sum)