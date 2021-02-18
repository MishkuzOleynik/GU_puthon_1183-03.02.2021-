#  процент 1
#  процента 2, 3, 4,
#  процентов 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
percents = input('Введите число от 0 до 20:  ')
if int(percents) == 1:
    print(percents + ' процент')
elif 1 < int(percents) < 5:
    print(percents + ' процента')
else:
    print(percents + ' процентов')
