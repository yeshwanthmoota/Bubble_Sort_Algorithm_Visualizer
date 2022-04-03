


import pygame
from constants import *
from rectangles import *
import time

pygame.init()

gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sorting Visualization")


SORTING_TYPE = 0
i = 0
j = 0


def draw_display(rectangles):
    gameDisplay.fill(BLACK)
    x_pos = 0
    for rect in rectangles:
        if rect == rectangles[j] and SORTING_TYPE != 0:
            pygame.draw.rect(gameDisplay, RED, pygame.Rect(x_pos, HEIGHT - rect.height, RECTANGLES_WIDTH, rect.height))
        elif j+1 < NO_OF_RECTANGLES and rect == rectangles[j+1] and SORTING_TYPE != 0:
            pygame.draw.rect(gameDisplay, WHITE, pygame.Rect(x_pos, HEIGHT - rect.height, RECTANGLES_WIDTH, rect.height))
        else:
            pygame.draw.rect(gameDisplay, GREEN, pygame.Rect(x_pos, HEIGHT - rect.height, RECTANGLES_WIDTH, rect.height))
        x_pos += RECTANGLES_WIDTH
    pygame.display.update()

def main(rectangles):
    clock = pygame.time.Clock()
    running = True
    global i
    global j
    global SORTING_TYPE
    rectangles_copy = rectangles.copy()
    isTrue = True
    VAR = True

    while isTrue:
        # keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isTrue = False
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    isTrue = False
                    SORTING_TYPE = 1
                if event.key == pygame.K_2:
                    isTrue = False
                    SORTING_TYPE = 2
            draw_display(rectangles=rectangles)
    
    if SORTING_TYPE == 1:
        i = NO_OF_RECTANGLES
        j = 0
    elif SORTING_TYPE == 2:
        i = 1
        j = i



    time1 = time.time()

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    SORTING_TYPE = 0
                    main(rectangles_copy)

        if SORTING_TYPE == 1:
            [i, j] = Rectangle.bubble_sort(i, j, rectangles)
        elif SORTING_TYPE == 2:
            [i, j] = Rectangle.bubble_sort2(i, j, rectangles)
            if j == len(rectangles):
                j = len(rectangles) - 1
        
        if SORTING_TYPE == 1 and i <= 0 and VAR: # Sorting Completed
            VAR = False
            print("time elapsed = ", time.time() - time1)
        elif SORTING_TYPE == 2 and i >= len(rectangles) and VAR: # Sorting Completed
            VAR = False
            print("time elapsed = ", time.time() - time1)
            
        

        draw_display(rectangles=rectangles)

    pygame.quit()


if __name__=='__main__':
    main(rectangles = Rectangle.rectanglesSpawn())