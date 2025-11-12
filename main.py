import random

digits = list("0123456789")
random.shuffle(digits)
rand = ""
for i in range(4):
    rand = rand + digits[i]

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

    count += 1
    number = input('Попробуйте ещё раз: ')



