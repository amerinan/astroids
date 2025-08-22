from constants import *
from circleshape import *

class Astroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self,screen):
        pygame.draw.circle(screen, (0,0,0),(self.x,self.y),self.radius,2)
        
    def update(self, dt):
        (self.velocity * dt) + self.velocity