def expA(x, a):
    print('te')
    if a == 0:
        return 1
    if a == 1:
        return x
    if a % 2 == 0:
        total = expA(x, a/2)
        return total*total
    else:
        total = expA(x, (a-1)/2)
        return total*total*x

x = int(input('Introduce la base: '))
a = int(input('Introduce el exponente: '))
res = expA(x,a)
print(x,'^', a,'= ',res)