numbers = []

# Создание списка из нечетных чисел
odd = 1
while odd <= 1000:
    numbers.append(odd ** 3)
    odd += 2
print(numbers)
# Проверка деления на 7 нацело и подсчет колличества таких чисел в списке
amount_of_specific_numbers = 0
for each_number in numbers:
    amount_of_digits = 0
    _each_number = each_number
    while _each_number > 0:
        amount_of_digits += _each_number % 10
        _each_number //= 10

    print(amount_of_digits, each_number)
    if (amount_of_digits % 7) == 0:
        amount_of_specific_numbers += each_number
        print('Есть одно')
print('сумма особых чисел равна:  ', amount_of_specific_numbers)

# Увеличение каждого элемента списка на 17
for idx in range(len(numbers)):
    numbers[idx] += 17
print(numbers)
print('Каждый элемент списка увеличен на 17')

for each_number in numbers:
    amount_of_digits = 0
    _each_number = each_number
    while _each_number > 0:
        amount_of_digits += _each_number % 10
        _each_number //= 10

    print(amount_of_digits, each_number)
    if (amount_of_digits % 7) == 0:
        amount_of_specific_numbers += each_number
        print('Есть одно')
print('сумма особых чисел равна:  ', amount_of_specific_numbers)
