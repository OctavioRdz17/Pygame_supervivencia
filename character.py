import pygame
import constants
import os
from elements import Tree, SmallStone
from world import World

class Character:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.inventory = {"wood":0,"stone":0,"food":0}
        image_path = os.path.join('assets','images','character','character.png')
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image,(constants.CHARACTER_SIZE,constants.CHARACTER_SIZE))
        self.size = self.image.get_width()

    def draw(self,screen):
        screen.blit(self.image,(self.x,self.y))

    def move(self,dx,dy,world):
        # nuevas coordenadas
        new_x = self.x + dx
        new_y = self.y + dy

        for tree in world.trees:
            if self.check_collision(new_x,new_y,tree):
                return
            
        self.x = new_x
        self.y = new_y
        self.x = max(0, min(self.x, constants.WIDTH - self.size))
        self.y = max(0, min(self.y, constants.HEIGHT - self.size))

    
    def check_collision(self,x,y,obj):
        
        return (x < obj.x + obj.size and x + self.size > obj.x and
                y < obj.y + obj.size and y + self.size > obj.y)
    
    def is_near(self,obj):
        return (abs(self.x - obj.x) <= max(self.size , obj.size) and
                abs(self.y - obj.y) <= max(self.size , obj.size))
    
    def interact (self,world):
        for tree  in world.trees:
            if self.is_near(tree):
                print("Estoy cerca de un arbol")

        for stone in world.small_stones:
            if self.is_near(stone):
                print("Estoy cerca de una piedra")
     