import pygame
import sys
import constants
from  character import Character
from world import World

# inicializar pygame
pygame.init()


# Configurar la ventana
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption("Fichicraft")


def main():
    clock = pygame.time.Clock()
    world = World(constants.WIDTH, constants.HEIGHT)

    # posicion del character en la mitad de la pantalla
    character = Character(constants.WIDTH // 2,constants.HEIGHT // 2)
    show_inventory = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    character.interact(world)
                if event.key == pygame.K_i:
                    show_inventory = not show_inventory

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            character.move(-5,0,world)
        if keys[pygame.K_d]:
            character.move(5,0,world)
        if keys[pygame.K_w]:
            character.move(0,-5,world)
        if keys[pygame.K_s]:
            character.move(0,5,world)
        
        

        world.draw(screen)
        character.draw(screen)
        if show_inventory:
            character.draw_inventory(screen)
        else:
            world.draw_inventory(screen,character)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()

    