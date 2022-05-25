#NUM 3
def summa(tovari):
    a = 10.95
    b = 2.95
    if tovari == 0:
        return print("Вы ввели неверное колличество товаров")
    if tovari == 1:
        return print("Доставка товаров на сумму: ", a, "$")
    s = a + tovari * b
    print("Доставка товаров на сумму: ", s,"$")
summa()
