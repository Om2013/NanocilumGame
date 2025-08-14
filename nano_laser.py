import pygame

# Player Bullet Class
class Nanobot_Laser(pygame.sprite.Sprite):
    """A class to model a bullet fired by the player"""
    
    def __init__(self, x, y, laser_group):
        """Initialize the bullet"""
        super().__init__()
        self.image = pygame.image.load("green_laser.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.velocity = 10
        laser_group.add(self)

    def update(self):
        """Update the bullet"""
        self.rect.y -= self.velocity
        if self.rect.bottom < 0:
            self.kill()  # Remove the bullet if it moves off-screen