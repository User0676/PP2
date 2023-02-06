n = int(input())

sum = 0

for x in range(n-1):
    a = int(input())
    sum+=a

sum2=0
    
for x in range(1,n+1):
    sum2+=x

print(sum2-sum)