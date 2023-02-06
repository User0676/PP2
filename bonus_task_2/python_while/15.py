n = int(input())

x = 0
y = 0
z = 1

if n==0:
    z=0
else:
    for i in range(n-1):
        x = y
        y = z
        z = x + y
print(z)