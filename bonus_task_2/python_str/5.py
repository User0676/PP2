s = input()
n=s.count('f')

if n==1:
    print(s.find('f'))
elif n>=2:
    print(s.find('f'))
    print(s.rfind('f'))