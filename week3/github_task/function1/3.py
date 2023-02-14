
def solve(numheads,numlegs):
   ch = numlegs/2 - numheads
   ra = numheads - ch
   return ch, ra

print("Headnumber : ")
y = int(input())
print("Legnumber : ")
x = int(input())

print(solve(y,x))