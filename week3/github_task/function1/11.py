def palindrome(word):
    word2 = word[::-1]
    if word2 == word:
        print("palindrome")
    else:print("not palindrome")

s = input()
palindrome(s)