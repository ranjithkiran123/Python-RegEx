for _ in range(int(input())): 
    print('Valid' if __import__('re').match(r'^(?!.*(\d)(-?\1){3})[456]\d{3}(?:-?\d{4}){3}$', input()) else 'Invalid')
