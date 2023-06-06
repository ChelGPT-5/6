def convert_num(n):
    result = ""
    while n > 0:
        result = str(n % 2) + result
        n = n // 2
    return result


n = int (input("введите число "))
binary = convert_num(n)
print(f"{n} в двоичной системе счисления: {binary}")