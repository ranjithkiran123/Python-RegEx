import re
regex = r"^[+-]?[0-9]*[.][0-9]+$";

T = int(input())
matchs = [False]*T
for i in range(T):
    string = input()
    if re.match(regex, string):
        matchs[i] = True
print(*matchs, sep="\n")
