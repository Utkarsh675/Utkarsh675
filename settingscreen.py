#''''''''GAME BY UV'''''''                         SNAKE GAME                               UTKARSH RASTOGI


import pygame
from pygame.locals import *

def draw_block():
    surface.fill((110, 110, 5))                                            #setting up screen colour by colour picker on chrom
    surface.blit(block, (block_x, block_y))                                #setting up dimnsions
    pygame.display.flip()

if __name__ == '__main__':
    pygame.init()

    surface = pygame.display.set_mode((500, 500))                          #setting up screen size
    surface.fill((110, 110, 5))                                            #colors

    block = pygame.image.load("resources/block.jpg").convert()             #adding the block

    block_x, block_y = 100, 100

    surface.blit(block, (block_x, block_y))

    pygame.display.flip()                                                  #displays block on screen

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:                                       #setting up keys
                if event.key == K_ESCAPE:
                    running = False                                         #for exiting the game
                if event.key == K_LEFT:
                    block_x -= 10                                           #left key decrese the block by position to 10 on x
                    draw_block()                                            #move the block
                if event.key == K_RIGHT:                                    
                    block_x += 10                                           #right key increse the block by position to 10 on x
                    draw_block()
                if event.key == K_UP:
                    block_y -= 10                                           #up key decrese the block by position to 10 on y
                    draw_block()
                if event.key == K_DOWN:
                    block_y += 10                                           #down key increse the block by position to 10 on y
                    draw_block()

            elif event.type == QUIT:
                running = False