import math
import os
import random
import re
import sys
n, m = map(int, input().rstrip().split())
matrix = [input() for _ in range(n)]
s = ''.join(matrix[j][i] for i in range(m) for j in range(n))
print(__import__('re').sub(r'(?<=\w)[^\w]{1,}(?=\w)', ' ', s))
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
