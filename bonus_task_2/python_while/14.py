max=-99999
cnt=1
while True:
    a = int(input())
    if a==0:
        break
    if max<a:
        max=a
        cnt=1
    elif a==max:
        cnt+=1
    
print(cnt)