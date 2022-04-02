


import pygame
from constants import *
from rectangles import *

pygame.init()

gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))

i = NO_OF_RECTANGLES # This keeps decrementing
j = 0 # cycles 

def draw_display(rectangles):
    gameDisplay.fill(BLACK)
    x_pos = 0
    for rect in rectangles:
        if rect == rectangles[j]:
            pygame.draw.rect(gameDisplay, RED, pygame.Rect(x_pos, HEIGHT - rect.height, RECTANGLES_WIDTH, rect.height))
        elif j+1 < NO_OF_RECTANGLES and rect == rectangles[j+1]:
            pygame.draw.rect(gameDisplay, WHITE, pygame.Rect(x_pos, HEIGHT - rect.height, RECTANGLES_WIDTH, rect.height))
        else:
            pygame.draw.rect(gameDisplay, GREEN, pygame.Rect(x_pos, HEIGHT - rect.height, RECTANGLES_WIDTH, rect.height))
        x_pos += RECTANGLES_WIDTH
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    running = True
    global i
    global j
    rectangles = Rectangle.rectanglesSpawn()
    

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if i > 0: # Bubble sorting algorithm
            if j + 1 < i:
                    if rectangles[j].height > rectangles[j+1].height:
                        temp = rectangles[j+1]
                        rectangles[j+1] = rectangles[j]
                        rectangles[j] = temp
            else: # AT_RECTANGLE has reached NO_OF_RECTANGLES's value => sorting completed
                i -= 1
                j = -1 # putting it as -1 because the next statement "j += 1" increments it immediately
            j += 1


        draw_display(rectangles=rectangles)

    pygame.quit()


if __name__=='__main__':
    main()