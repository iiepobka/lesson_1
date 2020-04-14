# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк.

user_seconds = int(input('Введите время в секундах: '))
hours = int(user_seconds / 3600)
minutes = int((user_seconds - hours * 3600) / 60)
seconds = int((user_seconds - hours * 3600) - (minutes * 60))

if hours < 10 and minutes < 10 and seconds < 10:
    time = 'Выше время: 0{}:0{}:0{}'.format(hours, minutes, seconds)
elif hours < 10 and minutes < 10 and seconds >= 10:
    time = 'Выше время: 0{}:0{}:{}'.format(hours, minutes, seconds)
elif hours < 10 and minutes >= 10 and seconds < 10:
    time = 'Выше время: 0{}:{}:0{}'.format(hours, minutes, seconds)
elif hours < 10 and minutes >= 10 and seconds >= 10:
    time = 'Выше время: 0{}:{}:{}'.format(hours, minutes, seconds)
elif hours >= 10 and minutes < 10 and seconds < 10:
    time = 'Выше время: {}:0{}:0{}'.format(hours, minutes, seconds)
elif hours >= 10 and minutes < 10 and seconds >= 10:
    time = 'Выше время: {}:0{}:{}'.format(hours, minutes, seconds)
elif hours >= 10 and minutes >= 10 and seconds < 10:
    time = 'Выше время: {}:{}:0{}'.format(hours, minutes, seconds)
else:
    time = 'Выше время: {}:{}:{}'.format(hours, minutes, seconds)

print(time)
