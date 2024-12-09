import constants
import pygame
import os


class Tree:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = constants.TREE_SIZE
        self.wood = 5
        tree_path = os.path.join('assets','images','objects','tree.png')
        self.tree = pygame.image.load(tree_path).convert_alpha()
        self.tree = pygame.transform.scale(self.tree, (self.size, self.size))

    def draw(self, screen):
        screen.blit(self.tree, (self.x, self.y))

    
class SmallStone:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = constants.SMALL_STONE_SIZE
        self.stone = 1
        small_stone_path = os.path.join('assets','images','objects','small_stone.png')
        self.stone = pygame.image.load(small_stone_path).convert_alpha()
        self.stone = pygame.transform.scale(self.stone, (self.size , self.size))

    def draw(self, screen):
        screen.blit(self.stone, (self.x, self.y))
    


    
