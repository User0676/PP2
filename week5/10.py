import re

with open('row.txt', 'r', encoding='utf-8') as file:
    result = re.sub(r'(?<!^)(?=[A-Z])', '_', file.read()).lower()
    print(result)