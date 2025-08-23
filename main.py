# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    # Initialise pygame and screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Clock and delta t
    clock = pygame.time.Clock()
    dt = 0
    
    while True:
        # Quit condition
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Draw black background
        screen.fill("black")
        pygame.display.flip()
        
        #Limit framerate to 60 FPS
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()