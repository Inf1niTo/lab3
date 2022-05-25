#NUM 10
def password():
    import random
    psw = ''
    for x in range(1):
        psw = random.sample(list('12345679'), 2) + random.sample(list('qwertyuiopasdfghjkzxcvbnmQWERTYUPASDFGHJKLZXCVNM'), 8) + random.sample(list('*_+=?%#@'), 2)
        random.shuffle(psw)
        print(''.join(psw))
        return psw
def proverka(n):
    import re
    pat = '[A-Z]'
    low = '[a-z]'
    if any(map(str.isdigit, n)) and re.search(pat, n) and re.search(low, n):
        print('True')
    else:
        print('False')

k = 0
if k <= 1:
    a = password()
    a = ''.join(a)
    proverka(a)
    k += 1
print("Пароль подобрался за", k, "попыток")
