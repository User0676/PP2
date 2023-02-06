s = input()

a=s.find('h')
b=s.rfind('h')

str=s[a+1:b].replace("h","H")
print(s[:a+1]+str+s[b:])