line = "результат операции: 42"

colon_index = line.index(':')
number_str = line[colon_index + 2:]
number = int(number_str)
result = number + 10
print(result)
