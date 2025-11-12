import random

digits = list("0123456789")
random.shuffle(digits)
rand = ""
for i in range(4):
    rand = rand + digits[i]

print('*** Загадано число', rand, '***') # Узнаём загаданное число для тестирования программы

count = 1
number = input('Введите 4-значное число: ')

while number != rand:
    bulls = 0
    cows = 0

    for i in range(4):
        if number[i] == rand[i]:
            bulls += 1
        elif number[i] in rand:
            cows += 1

    print(f'Быков: {bulls}, Коров: {cows}')
    count += 1
    number = input('Попробуйте ещё раз: ')

print('Вы угадали число!')
print('Количество потраченных попыток:', count)



