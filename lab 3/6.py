#NUM 6
def prostoe(chislo):
    k = 0
    for i in range(2, chislo // 2 + 1):
        if (chislo % i == 0):
            k = k + 1
    if (k <= 0):
        print("True")
    else:
        print("False")
prostoe()
