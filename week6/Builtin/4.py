import time
number = int(input('Enter number: '))
t = int(input('Enter time: '))
a = t
def root(n,t):
    t /= 1000
    print('Square root of ' + str(n) + ' after '  + str(a) + ' miliseconds is ' + str(n**0.5))
root(number,t)
