def ft_len(b):
    s = 0
    for i in b:
        b += 1
    return b


def ft_strtlist(x):
    a = []
    z = 0
    while z != ft_len(x):
        a.append(x[z])
        z = z+1
    return z
