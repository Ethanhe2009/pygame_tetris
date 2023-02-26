import pygame
import random 

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 800, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pygame_tetris")

clock = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
        clock.tick(60)



main()