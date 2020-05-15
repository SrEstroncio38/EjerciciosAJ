import pygame
import sys
import lcm


SCREEN_WIDTH = 25 * 25
SCREEN_HEIGHT = 25 * 25


def fillBoard(screen, xMax, yMax, d, resources):
    for x in range(xMax):
        for y in range(yMax):
            if lcm.randomLCM(lcm.c) / lcm.c['M'] < d:
                screen.blit(resources['mine'], (x * 25, y * 25))
            else:
                screen.blit(resources['cell'], (x * 25, y * 25))


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((0, 0, 255))
    pygame.display.set_caption("Minesweeper")


    resources = dict()
    resources['cell'] = pygame.image.load("resources/minesweeper/cell.png").convert()
    resources['cell'] = pygame.transform.scale(resources['cell'], (25, 25))
    resources['mine'] = pygame.image.load("resources/minesweeper/mine.png").convert()
    resources['mine'] = pygame.transform.scale(resources['mine'], (25, 25))

    fillBoard(screen, 25, 25, 0.9, resources)

    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == '__main__':
    main()