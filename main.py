import os
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def initialise():
    # os.environ['SDL_VIDEO_CENTERED'] = '1' # try to keep window centred
    # Initialise pygame and screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen_centre = screen.get_rect().center
    # Clock and delta t
    clock = pygame.time.Clock()
    
    # Text font
    font = pygame.font.Font(pygame.font.get_default_font(), 40)
    
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
    
    run_game = True
    state = "INTRO"
    
    return screen, screen_centre, clock, font, updatable, drawable, asteroids, shots, asteroid_field, player, dt, run_game, state

def main():
    
    screen, screen_centre, clock, font, updatable, drawable, asteroids, shots, asteroid_field, player, dt, run_game, state = initialise()

    while run_game:
        # Quit condition
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            run_game = False
        
        if state == "INTRO":
            welcome_text = font.render("Welcome to Asteroids!", False, WHITE)
            screen.blit(welcome_text, (screen_centre[0] - welcome_text.get_width()//2, screen_centre[1] - welcome_text.get_height()//0.2))
            
            start_text = font.render("START - Press enter", False, GREEN)
            screen.blit(start_text, (screen_centre[0] - start_text.get_width()//2, screen_centre[1]))
            
            exit_text = font.render("EXIT - Press escape", False, WHITE)
            screen.blit(exit_text, (screen_centre[0] - exit_text.get_width()//2, screen_centre[1] - exit_text.get_height()*2))
            
            pygame.display.update()
            if keys[pygame.K_RETURN]:
                state = "GAME"
            
        elif state == "GAME":
            # Update player's position from inputs
            updatable.update(dt)
            
            # Asteroid-player collision
            for asteroid in asteroids:
                if asteroid.collision(player):
                    state = "GAMEOVER"
                    
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
            over_text = font.render("GAME OVER!", False, RED)
            screen.blit(over_text, (screen_centre[0] - over_text.get_width()//2, screen_centre[1] - over_text.get_height()//0.2))
            
            start_text = font.render("RESTART - Press enter", False, GREEN)
            screen.blit(start_text, (screen_centre[0] - start_text.get_width()//2, screen_centre[1]))
            
            exit_text = font.render("EXIT - Press escape", False, WHITE)
            screen.blit(exit_text, (screen_centre[0] - exit_text.get_width()//2, screen_centre[1] - exit_text.get_height()*2))
            
            pygame.display.update()
            if keys[pygame.K_RETURN]:
                    screen, screen_centre, clock, font, updatable, drawable, asteroids, shots, asteroid_field, player, dt, run_game, state = initialise()


if __name__ == "__main__":
    main()