import pygame, sys
from asteroid import Asteroid
from player import Player
from shot import Shot
from constants import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable)
    
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
                 print("Game over!")
                 sys.exit()
        
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        
        #limit the framerate to 60 fps
        dt = clock.tick(60) / 1000 
        
        
if __name__ == "__main__":
    main()
