duration = int(input('Введите целое число: '))
hours = duration // 3600  # деление на цело на час в секундах
minutes = (duration % 3600) // 60  # деление нацело остатка от деления на 3600 секунд. получение количества минут.
seconds = duration % 60  # остаток от деления на количество секунд в минуте - получение остатка секунд
time = str(hours) + ' час ' + str(minutes) + ' мин ' + str(seconds) + ' сек'
print('Вы ввели: ', duration)
print(time)
print(3600 * hours, 60 * minutes, seconds, '  ----   для проверки правильности ')
