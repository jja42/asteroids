# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import Player

def main():
    #Print Text
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    #Instantiate General Game Vars
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time  = pygame.time.Clock()
    dt = 0

    #Create Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    #Initialize Player
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)

    #Game Loop
    while(True):
        #Exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #Background
        screen.fill("Black")

        updatable.update(dt)
        for entity in drawable:
            entity.draw(screen)

        #Render
        pygame.display.flip()

        #Time Tick
        dt = time.tick(60) / 1000


if __name__ == "__main__":
    main()
