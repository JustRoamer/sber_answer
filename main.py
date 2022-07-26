# 1. Написать функцию, которая возвращает максимальную прибыль от одной сделки
# с одной акцией (сначала покупка, потом продажа). Исходные данные — массив
#  вчерашних котировок stock_prices_yesterday с ценами акций.
# Информация о массиве:
#     Индекс равен количеству минут с начала торговой сессии (9:30 утра).
#     Значение в массиве равно стоимости акции в это время.
# Например: если акция в 10:00 утра стоила 20 долларов, то
# stock_prices_yesterday[30] = 20.
# Допустим, имеем некоторые условия:
# stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
# profit = get_max_profit(stock_prices_yesterday)
# #вернет 6 (купили за 5, продали за 11)
# Массив может быть любым, хоть за весь день. Нужно написать функцию
# get_max_profit как можно эффективнее — с наименьшими затратами времени
# выполнения и памяти.
# Дополнительная цель - объяснить решение.


def get_max_profit(data):
    if all([isinstance(item, int) or isinstance(item, float) for item in data]):
        max_value = max(data)
        min_value = min(data)
        return max_value - min_value
    else:
        return 'Тип данных в массиве должен быть числовым (int or float)'


stock_prices_yesterday = [10, 20, 35, 40]
profit = get_max_profit(stock_prices_yesterday)
print(profit)

# Почему решение именно такое? (специально нагуглил аргументы в пользу именно этого решения)
# min и max реализованы в машинном коде, поэтому они, безусловно, быстрее, чем при самостоятельной реализации в коде Python.
# сделал простенькую проверку на тип данных в массиве
