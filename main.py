import pygame, sys
from asteroid import Asteroid
from asteroidfield import *
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS, PLAYER_RADIUS

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    
    
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    
    asteroid_field = AsteroidField()
        
    while True:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 return
        
        
            
        screen.fill("black")
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.colisionCheck(player) == True:
                 sys.exit()
                 print("Game over!")
        
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        
        #limit the framerate to 60 fps
        dt = clock.tick(60) / 1000 
        
        
if __name__ == "__main__":
    main()
