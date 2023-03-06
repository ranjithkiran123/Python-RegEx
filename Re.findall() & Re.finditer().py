import re
text = r'[aeiouAEIOU^]?[aeiouAEIOU]{2,}[^aeiouAEIOU$]'
value = re.findall(text,input())
if value:
    [print(i[:-1]) for i in value]
else:
    print(-1)
