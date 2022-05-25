#NUM 1
# def trio(akatet, bkatet):
#     import math
#     c = math.sqrt(akatet**2 + bkatet**2)
#     print("Длина гипотенузы: ",c)
# trio()

#NUM 2
# def taxi(metr):
#     b = 4
#     p = 0.25
#     t = b + (metr/140 * p)
#     t = float('{:.2f}'.format(t))
#     print("Сумма поездки равна: ", t,"$")
# taxi()

#NUM 3
# def summa(tovari):
#     a = 10.95
#     b = 2.95
#     if tovari == 0:
#         return print("Вы ввели неверное колличество товаров")
#     if tovari == 1:
#         return print("Доставка товаров на сумму: ", a, "$")
#     s = a + tovari * b
#     print("Доставка товаров на сумму: ", s,"$")
# summa()

#NUM 4
# def mediana(a, b, c):
#     m = max(a, b, c) - min(a, b, c)
#     print("Медиана трех чисел равна:", m)
# mediana()

#NUM 5
# def chisla(num):
#     s = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
#     print(s.pop(num-1))
# chisla(2)

#NUM 6
# def prostoe(chislo):
#     k = 0
#     for i in range(2, chislo // 2 + 1):
#         if (chislo % i == 0):
#             k = k + 1
#     if (k <= 0):
#         print("True")
#     else:
#         print("False")
# prostoe()

# NUM 8
# def password():
#     import random
#     psw = ''
#     for x in range(1):
#         psw = random.sample(list('2345679'), 2) + random.sample(list('qwertyuiopasdfghjkzxcvbnmQWERTYUPASDFGHJKLZXCVNM'), 8) + random.sample(list('*_+=?%#@'), 2)
#         random.shuffle(psw)
#         print(''.join(psw))
#         return psw
# password()

#NUM 9
# def proverka():
#     import re
#     n = input('Enter password: ')
#     pat = '[A-Z]'
#     low = '[a-z]'
#     if any(map(str.isdigit, n)) and re.search(pat, n) and re.search(low, n):
#         print('True')
#     else:
#         print('False')
# proverka()

#NUM 10
# def password():
#     import random
#     psw = ''
#     for x in range(1):
#         psw = random.sample(list('12345679'), 2) + random.sample(list('qwertyuiopasdfghjkzxcvbnmQWERTYUPASDFGHJKLZXCVNM'), 8) + random.sample(list('*_+=?%#@'), 2)
#         random.shuffle(psw)
#         print(''.join(psw))
#         return psw
# def proverka(n):
#     import re
#     pat = '[A-Z]'
#     low = '[a-z]'
#     if any(map(str.isdigit, n)) and re.search(pat, n) and re.search(low, n):
#         print('True')
#     else:
#         print('False')
#
# k = 0
# if k <= 1:
#     a = password()
#     a = ''.join(a)
#     proverka(a)
#     k += 1
# print("Пароль подобрался за", k, "попыток")
