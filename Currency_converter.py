import requests

# По курсу ЦБ РФ
# data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
# USD_rate = round(data['Valute']['USD']['Value'], 2)
# По курсу сайта openexchangerates.org
data = requests.get('https://openexchangerates.org/api/latest.json?app_id=f02103aa3e3a4f58ba88e926982a32d0').json()
USD_RUB_rate = data['rates']['RUB']

print('Курс доллара на сегодняшний день:', round(USD_RUB_rate, 2))
print('Сколько у вас есть долларов?')

USD_count = None
while True:
    try:
        USD_count = float(input())
    except ValueError:
        print("Извините, я вас не понял. Пожалуйста, введите число и повторите попытку")
        continue
    else:
        break
if USD_count <= 1000:
    print('Не так уж и много, но тоже неплохо.')
else:
    print('Неплохо, на iphone может и хватит.')

RUB_count_int = int(USD_RUB_rate * USD_count)
RUB_count_round = round(USD_RUB_rate * USD_count, 2)
kop_count = int(round((RUB_count_round - RUB_count_int) * 100),)

one_last_digit_ruble = int(str(RUB_count_int)[-1])
try:
    two_last_digits_ruble = int(str(RUB_count_int)[-2:])
except IndexError:
    two_last_digits_ruble = int(0 + one_last_digit_ruble)

one_last_digit_kop = int(str(kop_count)[-1])
try:
    two_last_digits_kop = int(str(kop_count)[-2:])
except IndexError:
    two_last_digits_kop = int(0 + one_last_digit_kop)

list1 = [0, 5, 6, 7, 8, 9]
list2 = [1]
list3 = [11]
list4 = [2, 3, 4]
list5 = [12, 13, 14]


def ruble_name():
    if one_last_digit_ruble in list1:
        return 'рублей'
    if one_last_digit_ruble in list2:
        if one_last_digit_ruble in list3:
            return 'рублей'
        return 'рубль'
    if one_last_digit_ruble in list4:
        if two_last_digits_ruble in list5:
            return 'рублей'
        return 'рубля'


def kop_name():
    if one_last_digit_kop in list1:
        return 'копеек'
    if one_last_digit_kop in list2:
        if two_last_digits_kop in list3:
            return 'копеек'
        return 'копейку'
    if one_last_digit_kop in list4:
        if two_last_digits_kop in list5:
            return 'копеек'
        return 'копейки'


print('За ваши доллары вы получите', '{0:,}'.format(RUB_count_int).replace(',', ' '), ruble_name(), kop_count,
      kop_name())
print('hello')
