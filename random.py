import random

print("3-digit code:")
print(
    random.randint(0, 9),
    random.randint(0, 9),
    random.randint(0, 9),
    sep=""
)

print("4-digit code:")
print(
    random.randint(1, 6),
    random.randint(1, 6),
    random.randint(1, 6),
    random.randint(1, 6),
    sep=""
)