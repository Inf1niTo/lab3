# NUM 8
def password():
    import random
    psw = ''
    for x in range(1):
        psw = random.sample(list('2345679'), 2) + random.sample(list('qwertyuiopasdfghjkzxcvbnmQWERTYUPASDFGHJKLZXCVNM'), 8) + random.sample(list('*_+=?%#@'), 2)
        random.shuffle(psw)
        print(''.join(psw))
        return psw
password()