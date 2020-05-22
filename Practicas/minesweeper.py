import pygame
import sys
import lcm


SCREEN_W = 20
SCREEN_H = 20
SIZE = 40
MAX_T_SIZE = 12
MAX_T_NUM = 40
D = 0.02
D2 = 0.01
DT = 0.2
DG = 0.2



def initMap(W, H):
    fila = [0] * W
    map = []
    for i in range(H):
        map.append(fila[:])
    return map



def printMap(map, xPj, yPj):
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W * SIZE, SCREEN_H * SIZE))
    screen.fill((0, 0, 255))
    pygame.display.set_caption("Minesweeper")

    resources = dict()
    resources['tree'] = pygame.image.load("resources/minesweeper/tree.png").convert()
    resources['tree'] = pygame.transform.scale(resources['tree'], (SIZE, SIZE))
    resources['tree2'] = pygame.image.load("resources/minesweeper/tree2.png").convert()
    resources['tree2'] = pygame.transform.scale(resources['tree2'], (SIZE, SIZE))
    resources['grass'] = pygame.image.load("resources/minesweeper/grass.png").convert()
    resources['grass'] = pygame.transform.scale(resources['grass'], (SIZE, SIZE))
    resources['grass2'] = pygame.image.load("resources/minesweeper/grass2.png").convert()
    resources['grass2'] = pygame.transform.scale(resources['grass2'], (SIZE, SIZE))
    resources['pj'] = pygame.image.load("resources/minesweeper/pj.png").convert()
    resources['pj'] = pygame.transform.scale(resources['pj'], (SIZE, SIZE))
    resources['e1'] = pygame.image.load("resources/minesweeper/suicune.png").convert()
    resources['e1'] = pygame.transform.scale(resources['e1'], (SIZE, SIZE))
    resources['e2'] = pygame.image.load("resources/minesweeper/entei.png").convert()
    resources['e2'] = pygame.transform.scale(resources['e2'], (SIZE, SIZE))
    resources['e3'] = pygame.image.load("resources/minesweeper/raikou.png").convert()
    resources['e3'] = pygame.transform.scale(resources['e3'], (SIZE, SIZE))
    resources['poke'] = pygame.image.load("resources/minesweeper/poke.png").convert()
    resources['poke'] = pygame.transform.scale(resources['poke'], (SIZE, SIZE))
    for i in range(len(map)):
        for j in range(len(map[0])):
            if(map[i][j] == 1):
                if lcm.randomLCM(lcm.c) / lcm.c['M'] < D:
                    r = int(lcm.randomLCM(lcm.c) / lcm.c['M'] * 2)
                    if(r == 0):
                        screen.blit(resources['e1'], (i * SIZE, j * SIZE))
                    elif(r == 1):
                        screen.blit(resources['e2'], (i * SIZE, j * SIZE))
                    else:
                        screen.blit(resources['e3'], (i * SIZE, j * SIZE))
                elif lcm.randomLCM(lcm.c) / lcm.c['M'] < D2:
                    screen.blit(resources['poke'], (i * SIZE, j * SIZE))
                else:
                    if lcm.randomLCM(lcm.c) / lcm.c['M'] < DG:
                        screen.blit(resources['grass2'], (i * SIZE, j * SIZE))
                    else:
                        screen.blit(resources['grass'], (i * SIZE, j * SIZE))
            else:
                if lcm.randomLCM(lcm.c) / lcm.c['M'] < DT:
                    screen.blit(resources['tree2'], (i * SIZE, j * SIZE))
                else:
                    screen.blit(resources['tree'], (i * SIZE, j * SIZE))
    screen.blit(resources['pj'], (xPj * SIZE, yPj * SIZE))


def randomWalk(W, H, T, L, map):


    # Elijo posicion inicial
    x = int(lcm.randomLCM(lcm.c) / lcm.c['M'] * W)
    y = int(lcm.randomLCM(lcm.c) / lcm.c['M'] * H)
    xPj = x
    yPj = y
    #print(x)
    #print(y)

    last = [-1, -1]
    for i in range(T):
        check = True
        l = int(lcm.randomLCM(lcm.c) / lcm.c['M'] * L + 1)
        g = int(lcm.randomLCM(lcm.c) / lcm.c['M'] * 4)
        if last[0] == 0:
            while (g == 1 or g == last[1]):
                g = int(lcm.randomLCM(lcm.c) / lcm.c['M'] * 4)
        elif last[0] == 1:
            while (g == 0 or g == last[1]):
                g = int(lcm.randomLCM(lcm.c) / lcm.c['M'] * 4)
        elif last[0] == 2:
            while (g == 3 or g == last[1]):
                g = int(lcm.randomLCM(lcm.c) / lcm.c['M'] * 4)
        elif last[0] == 3:
            while (g == 2 or g == last[1]):
                g = int(lcm.randomLCM(lcm.c) / lcm.c['M'] * 4)
        #print("giro ",g)
        #print("tamaño ", l)
        # Derecha
        if (g == 0):
            if (x + l < W):
                for j in range(0, l):
                    map[x+1+j][y] = 1
                x += l
                last[0] = g
            else:
                for j in range(0, W - x - 1):
                    map[x+1+j][y] = 1
                x = W - 1
                last[1] = g
        # Izq
        elif (g == 1):
            if (x - l >= 0):
                for j in range(0, l):
                    map[x - 1 - j][y] = 1
                x -= l
                last[0] = g
            else:
                for j in range(0, x):
                    map[x - 1 - j][y] = 1
                x = 0
                last[1] = g

        # Arriba
        elif (g == 2):
            if (y - l >= 0):
                for j in range(0, l):
                    map[x][y - 1 - j] = 1
                y -= l
                last[0] = g
            else:
                for j in range(0, y):
                    map[x][y - 1 - j] = 1
                y = 0
                last[1] = g
        # Abajo
        elif (g == 3):
            if (y + l < H):
                for j in range(0, l):
                    map[x][y + 1 + j] = 1
                y += l
                last[0] = g
            else:
                for j in range(0, H - y - 1):
                    map[x][y + 1 + j] = 1
                y = H - 1
                last[1] = g
        #print(x)
        #print(y)
    return [map, xPj, yPj]

def main():
    map = initMap(SCREEN_W, SCREEN_H)
    map, xPj, yPj = randomWalk(SCREEN_W, SCREEN_H, MAX_T_NUM, MAX_T_SIZE, map)

    printMap(map, xPj, yPj)

    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == '__main__':
    main()