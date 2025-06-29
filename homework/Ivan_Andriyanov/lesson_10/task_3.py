def operation_control(func):
    def wrapper(first, second, operation):
        if first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'

        return func(first, second, operation)
    return wrapper


@operation_control
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        if second == 0:
            return "Ошибка: деление на 0"
        return first / second
    else:
        return "Неизвестная операция"


first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))

result = calc(first, second, '?')
print("Результат:", result)
