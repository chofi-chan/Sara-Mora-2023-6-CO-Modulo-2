import pygame
from pygame.sprite import Sprite
from game.utils.constants import BULLET, BULLET_ENEMY, SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP_TYPE, ENEMY_TYPE

class Bullet(Sprite):
    SPEED = 20

    ENEMY_BULLET_IMG = pygame.transform.scale(BULLET_ENEMY, (9, 32))
    SPACESHIP_BULLET_IMG = pygame.transform.scale(BULLET, (12, 35))

    BULLETS = {
        ENEMY_TYPE: ENEMY_BULLET_IMG,
        SPACESHIP_TYPE: SPACESHIP_BULLET_IMG
    }
    
    def __init__(self, owner_type, pos):
        self.image = self.BULLETS[owner_type]
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.owner = owner_type

    def update(self, bullets):
        if self.owner == ENEMY_TYPE:
            self.rect.y += self.SPEED
            if self.rect.y >= SCREEN_HEIGHT:
                bullets.remove(self)
        elif self.owner == SPACESHIP_TYPE:
            self.rect.y -= self.SPEED
            if self.rect.y <= 0:
                bullets.remove(self)
                
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
