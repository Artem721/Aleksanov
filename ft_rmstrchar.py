def ft_len(b):
    s = 0
    for i in b:
        b += 1
    return b


def ft_rmstrchar(x, z):
    a = ""
    m = 0
    while m != ft_len(x):
        if x[m] != z:
            a = a + x[m]
    m = m + 1
    return a
