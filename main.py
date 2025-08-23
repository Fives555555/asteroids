import pygame
from constants import *
from player import Player

def main():
    # Initialise pygame and screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Clock and delta t
    clock = pygame.time.Clock()
    
    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    
    # Initialise player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    dt = 0
    
    while True:
        # Quit condition
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Update player's position from inputs
        updatable.update(dt)
        
        # Draw black background
        screen.fill("black")
        # Draw items to screen (player, asteroids, shots)
        for item in drawable:
            item.draw(screen)
            
        pygame.display.flip()
        
        #Limit framerate to 60 FPS
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()