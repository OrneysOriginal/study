"""
I couldn't find an encoder from the decimal system in uleb128 on python, so I just made it.
Use it if someone finds it.
"""
def encode_dec_to_ULEB128(num: int):
    num = bin(num)[2:]
    g = 0

    if len(num)%7!=0:
        num = '0'*(7-len(num)%7)+num

    lst_bin = []

    for i in range(0,len(num),7):
        lst_bin.append(num[i:i+7])

    for i in range(len(lst_bin)):
        if g == 0:
            lst_bin[i] = '0'+lst_bin[i]
            g += 1
        else:
            lst_bin[i] = '1'+lst_bin[i]

    lst_hex = [hex(int(x,2)) for x in lst_bin]

    return lst_hex[::-1]