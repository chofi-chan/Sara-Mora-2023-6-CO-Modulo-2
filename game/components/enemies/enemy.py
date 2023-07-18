import pygame
import random
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_1, ENEMY_2, ENEMY_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH
LEFT ='left'
RIGHT ='right'
IMAGE = 'image'
SPEED_X = 'speed_x'
SPEED_Y = 'speed_y'
MOVE_X = 'move_x'
class Enemy(Sprite):
    MOVEMENTS = [LEFT, RIGHT]
    X_POS_LIST = [50, 100, 150, 200, 250, 350, 400, 450, 500, 550]
    Y_POS = 20
    VARIANTS = {
        1:{
            IMAGE: ENEMY_1,
            SPEED_X: 5,
            SPEED_Y: 1,
            MOVE_X: (30, 100)
        },
        2: {
            IMAGE: ENEMY_2,
            SPEED_X: 5,
            SPEED_Y: 2,
            MOVE_X: (50, 120)
        }
    }
    
    def __init__(self, variant):
        enemy_variant = self.VARIANTS[variant]
        self.image = pygame.transform.scale(enemy_variant[IMAGE], (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.type = ENEMY_TYPE
        
        self.speed_x = enemy_variant[SPEED_X]
        self.speed_y = enemy_variant[SPEED_Y]
        
        self.movement = random.choice(self.MOVEMENTS)
        lower_limit, upper_limit = enemy_variant[MOVE_X]
        self.move_x = random.randint(lower_limit, upper_limit)
        self.moving_index = 0
        self.shooting_time = random.randint(30, 50)
    
    def update(self, ships, game):
        self.rect.y += self.speed_y
        self.shoot(game.bullet_manager)
        if self.movement == LEFT:
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x
            
        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)
            
        self.update_movement()
            
            
    def update_movement(self):
        self.moving_index += 1
        if  self.rect.x >= SCREEN_WIDTH - 50:
            self.movement = LEFT
        elif self.rect.x <= 0:
            self.movement = RIGHT
            
        if self.moving_index >= self.move_x:
            self.moving_index = 0
            self.movement = LEFT if self.movement == RIGHT else RIGHT
        
        
    def draw(self, screen):
        screen.blit (self.image,(self.rect.x, self.rect.y))
        
    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(30, 50)