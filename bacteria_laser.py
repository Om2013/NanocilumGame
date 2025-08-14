#This class represents a laser shot fired by a bacteria enemy. It:

#Appears at a specific position on screen

#Moves downward each frame

#Automatically removes itself when it goes off-screen

import pygame
WINDOW_HEIGHT=900
class BacteriaLaser(pygame.sprite.Sprite):
    """A class to model a laser fired by the bacteria"""

    def __init__(self, x, y, laser_group):
        #Initialize the laser
        super().__init__()
        self.image = pygame.image.load("red_laser.png") # Load red laser image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.velocity = 10
        laser_group.add(self)

    def update(self):
        self.rect.y += self.velocity

        #If the bullet is off the screen, kill it
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()