import pygame
import random
from pygame.sprite import Sprite
from game.utils.constants import ENEMY_2, ENEMY_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH

LEFT = 'left'
RIGHT = 'right'

class Enemy2(Sprite):
    MOVEMENTS = [LEFT, RIGHT]
    X_POS_LIST = [50, 100, 150, 200, 250, 350, 400, 450, 500, 550]
    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 2
    DESCENDING_HEIGHT = SCREEN_HEIGHT // 2
    
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(ENEMY_2, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.type = ENEMY_TYPE
        
        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y
        
        self.movement = random.choice(self.MOVEMENTS)
        self.move_x = random.randint(30, 100)
        self.moving_index = 0
        self.descending = True
        
    def update(self, ships):
        if self.descending:
            self.rect.y += self.speed_y
            if self.rect.y >= self.DESCENDING_HEIGHT:
                self.descending = False
        else:
            self.rect.y -= self.speed_y
            if self.rect.y <= self.Y_POS:
                self.descending = True
        
        if self.movement == LEFT:
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x
        
        # Wrap the enemy around the screen horizontally
        if self.rect.x > SCREEN_WIDTH:
            self.rect.x = -50
        elif self.rect.x < -50:
            self.rect.x = SCREEN_WIDTH
            
        self.update_movement()
        
    def update_movement(self):
        self.moving_index += 1
        if self.moving_index >= self.move_x:
            self.moving_index = 0
            self.movement = LEFT if self.movement == RIGHT else RIGHT
        
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

