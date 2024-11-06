import pygame
import multiprocessing
import os
import time
import random

pygame.init()
SIZE = WIDTH, HEIGHT = 400, 300
window_num = 50
xMin = 0
xMax = 1520
yMin = 30
yMax = 720
white = (255, 255, 255)
pink = (255, 182, 193)

def main():
    x = random.uniform(xMin, xMax)
    y = random.uniform(yMin, yMax)
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
    fps = 60
    surface = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Thông báo!!!")
    clock = pygame.time.Clock()
    surface.fill(pink)
    font = pygame.font.Font('NotoSans-VariableFont_wdth,wght.ttf', 50)
    text = font.render('ANH NHỚ EM', True, white)
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT // 2)
    surface.blit(text, textRect)

    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        pygame.display.update()

if __name__ == '__main__':
    for _ in range(window_num):
        multiprocessing.Process(target=main).start()
        time.sleep(0.2)