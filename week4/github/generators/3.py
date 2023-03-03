def even(n):
    for i in range(n):
        if i % 12 == 0:
            yield i
n = int(input())

for i in even(n):
    if i != n - 1:
        print(i,end = " " )