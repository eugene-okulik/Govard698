def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


gen = fibonacci()

indexes = [5, 200, 1000, 100000]
results = {}

for i in range(1, max(indexes) + 1):
    num = next(gen)
    if i in indexes:
        results[i] = num

for index in indexes:
    print(f"{index}-е число Фибоначчи: {results[index]}")
