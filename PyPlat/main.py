import os 
import random  
import math 
import pygame
from os import listdir 
from os.path import isfile ,join
import player as player1
import helper 
import block as block1
pygame.init()

pygame.display.set_caption("Platformer")


WIDTH = 1000
HEIGHT = 800
FPS = 120
PLAYER_VEL = 4
TERRAINDICT = {
        1:  (0,     0),
        2:  (96,    0),
        3:  (192,   0), 
        4:  (0,    64),
        5:  (96,   64),
        6:  (192,  64), 
        7:  (288,  64), 
        8:  (0,   128),
        9:  (96,  128),
        10: (192, 128), 
        12: (288, 128), 
    }


window = pygame.display.set_mode((WIDTH, HEIGHT))






def main(window): 

    clock = pygame.time.Clock() 
    background, bg_image = helper.Helper().get_background("Blue.png")
    
    block_size = 96 
    
    player = player1.Player(100,100,50,50)
    floor = [block1.Block(i * block_size, HEIGHT - block_size, block_size) for i in range(-WIDTH // block_size, WIDTH*2//block_size)]

    run = True
    while run: 
        clock.tick(FPS)
        
        for event in pygame.event.get(): 
            if (event.type == pygame.QUIT): 
                run = False
                break
        
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE: 
                    player.jump()
            
        player.loop(FPS)
        player.handle_move(PLAYER_VEL, floor)   
        helper.Helper().draw(window, background, bg_image, player, floor)
    
    pygame.quit()
    quit()
    

if __name__ == "__main__": 
    main(window)