import pygame
import object 
import helper 

class Block(object.Object): 
    

    def __init__(self, x, y, size): 
        super().__init__(x,y,size,size)
        block = helper.Helper().get_block(2, size)
        self.image.blit(block, (0,0))
        self.mask = pygame.mask.from_surface(self.image)
        
    