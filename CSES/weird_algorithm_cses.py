def algo(n):
    s = ""
    while n != 1:
        s += f"{int(n)} "
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3
            n += 1
    return s


print(algo(7329151234))
