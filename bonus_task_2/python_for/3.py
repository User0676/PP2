a = int(input())
b = int(input())

if a%2==0:
    a-=1

for x in range(a,b-1,-2):
    print(x)
    