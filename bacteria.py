import pygame
import random
from bacteria_laser import BacteriaLaser 

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
class Bacteria(pygame.sprite.Sprite):    
    def __init__(self, x, y, velocity, laser_group,bacteria_group):
        """Initialize the alien"""
        super().__init__()
        self.image = pygame.image.load("bacteria_image.png")
        new_size = (40, 40) 
        self.image = pygame.transform.scale(self.image, new_size)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.direction = 1
        self.velocity = velocity
        self.laser_group = laser_group
        self.bacteria_group=bacteria_group

        
    def update(self):
        self.rect.x += self.direction*self.velocity
        if self.rect.right >= WINDOW_WIDTH or self.rect.left <= 0:
            for bacteria in self.bacteria_group:  # Directly reference the global bacteria group
                bacteria.direction *= -1
                bacteria.rect.y += 20  # Move all bacteria down

        #Randomly fires a laser
        if random.randint(0, 1000) > 999 and len(self.laser_group) < 3:
            self.fire()

    def fire(self):
        # Fire a laser
        BacteriaLaser(self.rect.centerx, self.rect.bottom, self.laser_group)
