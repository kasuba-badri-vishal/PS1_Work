import string
alpha = string.ascii_lowercase
n = int(input())
L = []
for i in range(n):
    s = "-".join(alpha[i:n])
    L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
print('\n'.join(L[:0:-1]+L))


# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# # Complete the solve function below.
# def solve(s):
#     full_name = s.split(' ')
#     return ' '.join((word.capitalize() for word in full_name))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = solve(s)

#     fptr.write(result + '\n')

#     fptr.close()
