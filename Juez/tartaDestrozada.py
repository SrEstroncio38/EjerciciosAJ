w = int(input(''))
n = int(input(''))
a = 0

for i in range(n):
    str = input('')
    x = str.split(' ')
    a = a + int(x[0]) * int(x[1])

print(int(a / w))
