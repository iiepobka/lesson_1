# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

'''user_number = int(input('Введите любое число цифрами: '))
max = 1

while user_number > 1:
    user_number = user_number / 10
    number = (user_number - int(user_number)) * 10
    if number > 8.9:
        max = 9
    elif max < number:
        max = int(number)

print(f'Cамая большая цифра в числе: {max}')'''

# Если делать нормально и чтобы от длинны не зависило вообще, а не как выше, то

get_number = int(input('Число: '))
get_number = list(str(get_number))
max_number = max(get_number)
print('Cамая большая цифра в числе:', max_number)
