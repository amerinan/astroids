from constants import *
from circleshape import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
        
    def draw(self,screen):
        pygame.draw.circle(screen, (124,124,124),(int(self.position.x),int(self.position.y)),self.radius,2)
        
    def update(self, dt):
        self.position += (self.velocity * dt)