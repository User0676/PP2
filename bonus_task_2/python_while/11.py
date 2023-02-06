cnt=-1
pn=-99999
while True:
    a = int(input())
    if a==0:
        break
    if pn<a:
        cnt+=1
    pn=a
print(cnt)