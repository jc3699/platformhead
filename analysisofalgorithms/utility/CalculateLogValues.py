import math

values = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]

for n in values:
    result = n * math.log2(n)
    print(f"{n} * log base 2 of {n} is: {result}")