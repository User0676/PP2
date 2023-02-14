import random

def rand_game():
    c = random.randint(0,20)
    n = 21
    cnt = 0
    print("Guess the number :")
    while n!=c:
        n = int(input())
        print("You are wrong! Try again : ")
    if n==c:
        print("Nice! You win!")
        return

rand_game()
        


