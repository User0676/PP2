x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if abs(x1-x2)==2:
    if abs(y2-y1)==1:
        print("YES")
    else:print("NO")
elif abs(x1-x2)==1:
    if abs(y2-y1)==2:
        print("YES")
    else:print("NO")
else:print("NO")