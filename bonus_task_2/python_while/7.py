sum=0
cnt=0

while True:
    a = int(input())
    if a==0:
        break;
    sum+=a
    cnt+=1
print(sum/cnt)