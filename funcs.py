def binary(n, zf=8):
    return bin(n).zfill(zf).replace('b', '')


def binary_digit(n, zf=8, i=1):
    return int(binary(n, zf)[-i])


def list_format(l: list):
    return list_format_str(str(l))


def list_format_str(l: str):
    return l.replace('[', '').replace(']', '').replace("'", '').replace(',', '')


def combine_lists(tab, *lists: list):
    return tab.join([str(i).replace('[', '').replace(']', '').replace(',', '') for i in lists])


def list_add_list(l1, l2):
    assert len(l1) == len(l2)
    return [l1[i] + l2[i] for i in range(0, len(l1))]


def list_sub_list(l1, l2):
    assert len(l1) == len(l2)
    return [l1[i] - l2[i] for i in range(0, len(l1))]


def list_sub_list_bitwise(l1, l2):
    assert len(l1) == len(l2)
    return [0 if l1[i] == 0 or l2[i] == 1 else 1 for i in range(0, len(l1))]


def list_sub_list_bitwise_rev(l1, l2):
    assert len(l1) == len(l2)
    return [max(l1[i] - l2[i], 0) for i in range(0, len(l1))]


def binary_digit_value(n, zf=8, i=1):
    return binary_digit(n, zf, i) * (2 ** (i - 1))


def multiply_list(l: list, multiplier):
    return [multiplier * i for i in l]
