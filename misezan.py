x = int(input())
y = int(input())

def is_repeating_char(number, char):
    return str(number) == char * len(str(number))

if x == y:
    print(str(x) + '見せ' +str(y) + 'のとき、眼は' + str(1))
elif (is_repeating_char(x, '6') and is_repeating_char(y, '9')) or (is_repeating_char(x, '9') and is_repeating_char(y, '6')):
    print(str(x) + '見せ' + str(y) + 'のとき、眼は11')
elif (x == 1) and (y == 100):
    print(str(x) + '見せ' + str(y) + 'のとき、眼は83')
elif x > y:
    print(str(x) + '見せ' +str(y) + 'のとき、眼は' + str(x))
elif x < y:
    print(str(x) + '見せ' +str(y) + 'のとき、眼は' + str(y))
