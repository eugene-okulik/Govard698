number = 1

while True:
    user_input = int(input('Введи свое число : '))
    if user_input == number:
        print('Ты угадал число, молодец')
        break
    else:
        print('Попробуй снова')
