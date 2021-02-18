prices = [57.85, 46.54, 97, 43.23, 17.07, 23.8, 45.06, 54.35, 17.23, 100.45]
print('исходный не сортированный список', prices, id(prices))
prices.sort()
print('Сортированный список in_line', prices, id(prices))
print('Id не изменился')
descending_prices = sorted(prices, key=None, reverse=True)
for each_price in range(len(prices)):
    if int(prices[each_price] % 1 * 100) < 10:
        prices[each_price] = str(int(prices[each_price] // 1)) + " руб 0" +\
                             str(int(prices[each_price] - abs(int(prices[each_price])))) + " коп"
        # prices[each_price] = str(int(prices[each_price] // 1)) + " руб 0" + \
                        #    str(int(prices[each_price] % 1 * 100)) + " коп"

    else:
        prices[each_price] = str(int(prices[each_price] // 1)) + " руб " +\
                             str(int(prices[each_price] % 1 * 100)) + " коп"

for each_price in range(len(descending_prices)):
    if int(descending_prices[each_price] % 1 * 100) < 10:
        descending_prices[each_price] = str(int(descending_prices[each_price] // 1)) + " руб 0" +\
                             str(int(descending_prices[each_price] % 1 * 100)) + " коп"
    else:
        descending_prices[each_price] = str(int(descending_prices[each_price] // 1)) + " руб " +\
                             str(int(descending_prices[each_price] % 1 * 100)) + " коп"


print('Возрастающий список', prices)
print('Убывающий список', descending_prices)
print('Список пяти самых дорогих товаров по возрастанию', prices[len(prices)-5:len(prices)])
