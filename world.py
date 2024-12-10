import pygame
import constants
from elements import Tree, SmallStone
import random
import os

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # Crear arboles aleatorios  
        self.trees = [Tree(random.randint(0, width-constants.TREE_SIZE), 
                           random.randint(0, height-constants.TREE_SIZE)) for _ in range(10)]

        # Crear piedras aleatorias
        self.small_stones = [SmallStone(random.randint(0, width-constants.SMALL_STONE_SIZE), 
                           random.randint(0, height-constants.SMALL_STONE_SIZE)) for _ in range(15)]


        grass_path = os.path.join('assets','images','objects','grass.png')
        self.grass_image = pygame.image.load(grass_path).convert()
        self.grass_image = pygame.transform.scale(self.grass_image, (constants.GRASS_SIZE, constants.GRASS_SIZE))



    def draw(self, screen):
        
        for y in range(0, self.height, constants.GRASS_SIZE):
            for x in range(0, self.width, constants.GRASS_SIZE):
                screen.blit(self.grass_image, (x, y))

        for small_stone in self.small_stones:
            small_stone.draw(screen)
            
        for tree in self.trees:
            tree.draw(screen)

    def draw_inventory(self,screen,character):
        font = pygame.font.Font(None, 36)
        wood_text = font.render(f"Wood: " + str(character.inventory["wood"]), True, constants.WHITE)
        stone_text = font.render(f"Stone: " + str(character.inventory["stone"]), True, constants.WHITE)
        
        screen.blit(wood_text, (10, 10))
        screen.blit(stone_text, (10, 50))