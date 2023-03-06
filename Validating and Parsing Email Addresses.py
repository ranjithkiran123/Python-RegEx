import re
for _ in range(int(input())):
    name, email = input().split()
    print(f"{name} {email}") if bool(re.search(r"^[a-zA-Z][a-zA-Z-._0-9]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$",email[1:len(email)-1])) else None
