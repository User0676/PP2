import re

with open('row.txt', 'r', encoding='utf-8') as file:
    result = re.findall(r'[A-Z][^A-Z]*', file.read() )
    print(result)