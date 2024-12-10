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

    def chop (self):
        if self.wood > 0:
            self.wood -= 1
            return True
        return False

    
class SmallStone:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = constants.SMALL_STONE_SIZE
        self.stone = 1
        small_stone_path = os.path.join('assets','images','objects','small_stone.png')
        self.small_stone = pygame.image.load(small_stone_path).convert_alpha()
        self.small_stone = pygame.transform.scale(self.small_stone, (self.size , self.size))

    def draw(self, screen):
        screen.blit(self.small_stone, (self.x, self.y))

    def mine (self):
        if self.stone > 0:
            self.stone -= 1
            return True
        return False
    
    


    
