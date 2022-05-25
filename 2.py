#NUM 2
def taxi(metr):
    b = 4
    p = 0.25
    t = b + (metr/140 * p)
    t = float('{:.2f}'.format(t))
    print("Сумма поездки равна: ", t,"$")
taxi()
