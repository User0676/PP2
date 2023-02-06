max = -999999

while True:
    a = int(input())
    if a==0:
        break
    if max<a:
        max=a
print(max)