from itertools import product
from string import digits

for password in product(digits, repeat=4):
    print(password)