thistlist = [5,234,1,0,3,4,51]

def is_prime(n):
    
    for i in range(2, (n//2)+1):
        if n%i == 0:
            return False
    return True

result = filter(is_prime, thistlist)
print(*result)


