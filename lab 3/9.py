#NUM 9
def proverka():
    import re
    n = input('Enter password: ')
    pat = '[A-Z]'
    low = '[a-z]'
    if any(map(str.isdigit, n)) and re.search(pat, n) and re.search(low, n):
        print('True')
    else:
        print('False')
proverka()
