add = lambda x, y: x + y

print(add(5, 7))

# --------------------------------

def double(x):
    return x * 2

sequence = [1, 3, 5, 9]
doubled = [double(x) for x in sequence] # são funções mais performáticas
print(doubled)
doubled = map(double, sequence)
print(doubled)
doubled = list(map(lambda x: x * 2, sequence))
print(doubled)
