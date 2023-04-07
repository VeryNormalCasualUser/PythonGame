import pygame
from helper import *
import helper 

class Player(pygame.sprite.Sprite):
    

    SPRITES = helper.Helper().load_sprite_sheets( "MainCharacters" , "PinkMan" , 32 , 32 , True )
    ANIMATION_DELAY = 4
    
    JUMPVARIABLE = 9
    
    GRAVITY = 1
    
    COLOR = (255, 0, 0)

    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0
        self.jump_count = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        
    def handle_vertical_collision(self, objects):
        collided_objects = [] 
        for obj in objects: 
            if pygame.sprite.collide_mask(self, obj): 
                if (self.y_vel > 0):
                    self.rect.bottom = obj.rect.top
                    self.landed()
                elif self.y_vel < 0:
                    self.rect.top = obj.rect.bottom
                    self.hit_head()
                    
            collided_objects.append(obj)
    
        return collided_objects
    
    def jump(self):
        if self.jump_count < 2 : 
            self.y_vel = -self.GRAVITY * self.JUMPVARIABLE
            self.animation_count = 0
            self.jump_count += 1
            if self.jump_count == 1: 
                self.fall_count = 0
        
    
    def landed(self): 
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0
        
    def hit_head(self): 
        self.count = 0
        self.y_vel *= -1
        
    def handle_move(self, velocity, objects): 
        keys = pygame.key.get_pressed()

        self.x_vel = 0

        if keys[pygame.K_a]: 
            self.move_direction(velocity, "left")
        elif keys[pygame.K_d]: 
            self.move_direction(velocity, "right")  # could make more effective my passing the pygame key variable directly to the move function 
        
        self.handle_vertical_collision(objects)
    
    def update_sprite(self): 
        sprite_sheet = "idle"
        if self.y_vel < 0: 
            if self.jump_count == 1: 
                sprite_sheet = "jump"
            elif self.jump_count == 2:
                 sprite_sheet = "double_jump"
        elif self.y_vel > self.GRAVITY: 
            sprite_sheet = "fall"
        elif self.x_vel != 0: 
            sprite_sheet = "run"
            
        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = ( self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.update()
    
    def move_direction(self, vel, directionStr):

        newVel = 0

        if (directionStr == "left"):
            newVel = -vel
        elif (directionStr == "right"):
            newVel = vel
        else:
            raise Exception("no such direction as" + directionStr)

        self.x_vel = newVel        
        if self.direction != directionStr:
            self.direction = directionStr
            self.animation_count = 0
            
    def update(self):
        self.rect = self.sprite.get_rect(topleft = (self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def loop(self, fps):
        self.y_vel += (self.fall_count*2  / fps) * self.GRAVITY
        self.move(self.x_vel, self.y_vel)
        self.fall_count += 1
        self.update_sprite()
    
    def draw(self, win):
        win.blit(self.sprite, (self.rect.x, self.rect.y))