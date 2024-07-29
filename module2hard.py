def result(n):
    cod = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                cod += str(i) + str(j)
    return cod


print('Введите число: ')

print(result(int(input())))
