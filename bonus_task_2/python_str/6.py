s = input()
n = s.count('f')

if n==1:
    print("-1")
elif n>=2:
    print(s[s.find('f')+1:].find('f') +s.find('f')+1 )
else: print("-2")