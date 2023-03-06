for _ in range(int(input())):
    print('YES' if bool(__import__('re').match('^[789]{1}\d{9}$', input())) else 'NO')
