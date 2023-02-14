s = input()

def rev(sentence):
    words = sentence.split()[::-1]
    reverse_sentence = []
    for i in words:
        reverse_sentence.append(i)
    print(" ".join(reverse_sentence))



rev(s)