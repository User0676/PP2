n = int(input())

x = 1
cnt=0
if(x>n):
    cnt+=1
    x=2
    

while n>=x*2:
    x=x*2
    cnt+=1
else: print(cnt,x)