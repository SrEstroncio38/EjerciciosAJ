import lcm

def randomLasVegas(l, u):
    W = u-l
    r = lcm.randomLCM(lcm.c) // (lcm.c['M'] // W)
    while r >= W:
        r = lcm.randomLCM(lcm.c) // (lcm.c['M'] // W)
    r = r + l
    return r

if __name__ == '__main__':
    low = 0
    high = 3
    for i in range(10):
        print(int(randomLasVegas(low, high)))