n = int(input())

x=y=0
z=1
num=1

while z<=n:
    if z==n:
        print(num)
        break
        
    num+=1
    x=y
    y=z
    z=x+y
else:print("-1")