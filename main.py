import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # Initialise pygame and screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen_centre = screen.get_rect().center
    # Clock and delta t
    clock = pygame.time.Clock()
    
    # Text font
    font = pygame.font.Font(pygame.font.get_default_font(), 30)
    
    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Containers
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)    
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)
    
    # Initialise objects
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    dt = 0
    
    state = "INTRO"
    run_game = True
    
    while run_game:
        # Quit condition
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
        
        if state == "INTRO":
            text = font.render("START - Press enter", True, (255,255,255))
            screen.blit(text, (screen_centre[0] - text.get_width()//2, screen_centre[1]))
            pygame.display.update()
            keys = pygame.key.get_pressed()

            if keys[pygame.K_RETURN]:
                state = "GAME"
            
        elif state == "GAME":
            # Update player's position from inputs
            updatable.update(dt)
            
            # Asteroid-player collision
            for asteroid in asteroids:
                if asteroid.collision(player):
                    state = "GAMEOVER"
                    print("Game over!")
                    sys.exit()
                    
                for shot in shots:
                    if asteroid.collision(shot):
                        shot.kill()
                        asteroid.split()
            
            # Draw black background
            screen.fill("black")
            # Draw items to screen (player, asteroids, shots)
            for item in drawable:
                item.draw(screen)
                
            pygame.display.flip()
            
            #Limit framerate to 60 FPS
            dt = clock.tick(60)/1000
            
        elif state == "GAMEOVER":
            pass


if __name__ == "__main__":
    main()