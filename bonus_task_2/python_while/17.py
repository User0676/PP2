a=int(input())
b=int(input())
n=1
m=0
while a!=0 and b!=0:
    if a==b:
      a=b
      b=int(input())
      n+=1
    if a!=b!=0:
      m=max(n,m)
      n=1
      a=b
      b=int(input())
      
print(max(n,m))