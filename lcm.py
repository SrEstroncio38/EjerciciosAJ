
seed = 1234
c = {
    'M': 2**10-3,
    'A': 35,
    'C': 8,
    'X': seed   # Ultimo aleatorio que se ha generado
}



def moduloSum(x, y, m):
    if x <= m-1-y:
        return x+y
    else:
        return x - (m-y)


def randomLCM(c):
    r = (c['A'] * c['X']) % c['M']
    r = moduloSum(r, c['C'], c['M'])
    c['X'] = r
    return c['X']


if __name__ == '__main__':
    w = 100
    for i in range(10):
        n = randomLCM(c)
        print(str(n%w))