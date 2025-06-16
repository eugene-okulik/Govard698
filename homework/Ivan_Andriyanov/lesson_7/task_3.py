results = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]


def sum_result(num):
    for line in results:
        line_index = line.index(':')
        result_numb = int(line[line_index + 2:])
        print(f'{result_numb + num}')


sum_result(10)
