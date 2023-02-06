pos=0
max=-99999
num=-1
while True:
    a = int(input())
    if a==0:
        break
    num+=1
    if max<a:
        max=a
        pos=num
print(pos)