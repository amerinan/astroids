from constants import *
from circleshape import *
import pygame, random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity=None, asteroid_field_instance=None):
        super().__init__(x, y, radius)
        self.AsteroidField = asteroid_field_instance
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
             
        self.AsteroidField.spawn(new_radius, self.position, vector_1 * ASTEROID_SPLIT_SPEED_MULTIPLIER)
        self.AsteroidField.spawn(new_radius, self.position, vector_2 * ASTEROID_SPLIT_SPEED_MULTIPLIER)        
