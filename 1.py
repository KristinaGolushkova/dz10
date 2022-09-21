from decimal import Decimal
num = list(map(Decimal, '2.45 2.69 2.45 3.45 2.00 0.04 7.25'.split()))
print(sum(num))
print(sorted(num))