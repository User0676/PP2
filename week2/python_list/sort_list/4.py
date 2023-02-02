def func(n):
    return abs(n-50)

thislist = [123,57,84]
thislist.sort(key = func)

print(thislist)
