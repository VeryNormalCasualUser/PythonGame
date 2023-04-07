import os
import random
import math
import pathlib
from main import pygame
from os import listdir
from os.path import isfile, join
from main import WIDTH, HEIGHT , FPS, PLAYER_VEL, TERRAINDICT

class Helper():
    
    
    @staticmethod
    def load_sprite_sheets(dir1, dir2, width, height, direction=False):

        path = join("PyPlat", "assets", dir1, dir2)
        images = [f for f in listdir(path) if isfile(join(path, f))]
        all_sprites = {}
        for image in images:
            sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()
            sprites = []
            for i in range(sprite_sheet.get_width() // width):
                surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
                rect = pygame.Rect(i * width, 0, width, height)
                surface.blit(sprite_sheet, (0, 0), rect)
                sprites.append(pygame.transform.scale2x(surface))
            if direction:
                all_sprites[image.replace(".png", "") + "_right"] = sprites
                all_sprites[image.replace(".png", "") + "_left"] = Helper().flip(sprites)
            else:
                all_sprites[image.replace(".png", "") + ""] = sprites
        return all_sprites

    @staticmethod
    def get_block(imageIndex, size): 
        img_position = TERRAINDICT[imageIndex]
        path = join("PyPlat", "assets","Terrain", "Terrain.png")
        image = pygame.image.load(path).convert_alpha()
        surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        rect = pygame.Rect(img_position[0],img_position[1],size,size)
        surface.blit(image, (0,0), rect)
        return pygame.transform.scale2x(surface)

    @staticmethod
    def flip(sprites):
        return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

    @staticmethod
    def get_background(name):
        image = pygame.image.load(join("PyPlat", "assets", "Background", name))
        _, _, width, height = image.get_rect()
        tiles = []
        for i in range( WIDTH // width + 1):
            for j in range(HEIGHT//height + 1):
                pos = [i*width, j*height]
                tiles.append(pos)
        return tiles, image

    @staticmethod
    def draw(window, background, bg_image, player, objects):
        for tile in background:
            window.blit(bg_image, tile)

        for obj in objects: 
            obj.draw(window)

        player.draw(window)
        pygame.display.update()
