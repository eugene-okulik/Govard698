import random

salary = int(input('Напиши свою зарплату: '))
bonus = random.choice([True, False])
if bonus:
    bonus_random = random.randint(1, 5000)
    print(f'К вашей зарплате зачислен случайный бонус :{bonus_random}$ в итоге\
           вы получаете ${salary + bonus_random} ')
else:
    print('Зарплата без изменения')
