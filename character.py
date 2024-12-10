import pygame
import constants
import os
from elements import Tree, SmallStone
from world import World

class Character:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.inventory = {"wood":0,"stone":0}
        image_path = os.path.join('assets','images','character','character.png')
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image,(constants.CHARACTER_SIZE,constants.CHARACTER_SIZE))
        self.size = self.image.get_width()

        self.inventory_images = {"stone": self.load_items_images("stone.png"), 
                                 "wood": self.load_items_images("wood.png")}

    def load_items_images(self,filename):
        image_path = os.path.join('assets','images','objects',filename)
        image = pygame.image.load(image_path).convert_alpha()
        image = pygame.transform.scale(image,(40,40))
        return image

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
        
        return (x < obj.x + obj.size//2 and x + self.size//2 > obj.x and
                y < obj.y + obj.size//2 and y + self.size//2 > obj.y)
    
    def is_near(self,obj):
        return (abs(self.x - obj.x) <= max(self.size , obj.size) and
                abs(self.y - obj.y) <= max(self.size , obj.size))
    
    def interact (self,world):
        for tree  in world.trees:
            if self.is_near(tree):
                if tree.chop():
                    self.inventory["wood"] += 1
                    if tree.wood <= 0:
                        world.trees.remove(tree)
                return
            
        for stone in world.small_stones:
            if self.is_near(stone):
                if stone.mine():
                    self.inventory["stone"] += 1
                    if stone.stone <= 0:
                        world.small_stones.remove(stone)
                return
                
    def draw_inventory(self,screen):
        background = pygame.Surface((300,400),pygame.SRCALPHA)
        background.fill((0,0,0,128))
        # centra la ventana de inventario en la pantalla
        screen.blit(background,(constants.WIDTH//2 - 150,constants.HEIGHT//2 - 200))

        font = pygame.font.Font(None, 36)
        title = font.render("Inventory", True, constants.WHITE)

        # dibuja el titulo en la parte superior de la venta de inventario
        screen.blit(title,(constants.WIDTH//2 - title.get_width()//2,constants.HEIGHT//2 - 180))

        item_font = pygame.font.Font(None, 24)
        y_offset = 80
        for item,quantity in self.inventory.items():
            if quantity > 0:
                screen.blit(self.inventory_images[item],(constants.WIDTH//2 - 150 + 20,constants.HEIGHT//2 - 200 + y_offset))
                text = item_font.render(f"{item.capitalize()}: {quantity}", True, constants.WHITE)
                screen.blit(text,(constants.WIDTH//2 - 150 + 70,constants.HEIGHT//2 - 200 + y_offset))
                y_offset += 60

        close_text = item_font.render("Press 'i' to close", True, constants.WHITE)
        screen.blit(close_text,(constants.WIDTH//2 - close_text.get_width()//2,constants.HEIGHT//2 + 160))
        
        