def sequence(n,m):
    x = int( n ** 0.5)
    d = int(m ** 0.5)
    while x <= d:
        yield x * x
        x += 1

for i in sequence(1,int(input())):
    print(i,end = " ")