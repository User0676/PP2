n = int(input())

sum = 0
fact = 1
for x in range(1,n+1):
    fact*=x
    sum+=fact
print(sum)