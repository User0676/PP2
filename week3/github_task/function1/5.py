from itertools import permutations

def all_permut(string):
    permutations=[''.join(p) for p in permutations(string)]
    print(*permutations)

string = input()
all_permut(string)
