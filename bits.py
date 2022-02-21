def binary(n, zf=8):
    return bin(n).zfill(zf).replace('b', '')


def binary_digit(n, zf=8, i=-1):
    return binary(n, zf)[i]


def listformat(l: list):
    return listformatstr(str(l))


def listformatstr(l: str):
    return l.replace('[', '').replace(']', '').replace("'", '').replace(',', '')
