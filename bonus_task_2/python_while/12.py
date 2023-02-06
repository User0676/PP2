max1=-99999

max2=-100000

while True:
    a = int(input())
    if a==0:
        break
    if max1<a:
        max2=max1
        max1=a
    elif max2<a:
        max2=a
print(max2)
