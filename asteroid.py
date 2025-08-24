from constants import *
from circleshape import *
from asteroidfield import *
import pygame, random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity=None):
        super().__init__(x, y, radius)
        if  velocity is None:
            self.velocity = pygame.math.Vector2(0,0)
        else:
            self.velocity = velocity
            
    def draw(self,screen):
        pygame.draw.circle(screen, (124,124,124),(self.position.x,self.position.y),self.radius,2)
        
    def update(self, dt):
        self.position += (self.velocity * dt)
        
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20,50)
        vector_1 = self.velocity.rotate(angle)
        vector_2 = self.velocity.rotate(-angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius, vector_1 * ASTEROID_SPLIT_SPEED_MULTIPLIER)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius, vector_2 * ASTEROID_SPLIT_SPEED_MULTIPLIER)
        
        AsteroidField.add(asteroid_1)
        AsteroidField.add(asteroid_2)
        
