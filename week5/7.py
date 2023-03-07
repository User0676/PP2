import re
with open ('row.txt', 'r', encoding='utf-8') as file:
    result = re.sub(r'_([a-z])', lambda match : match.group(1).upper(), file.read())
    print(result)
