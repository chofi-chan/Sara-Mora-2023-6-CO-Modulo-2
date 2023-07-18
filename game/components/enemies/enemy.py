import pygame
import random
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_1, ENEMY_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH

LEFT = 'left'
RIGHT = 'right'

class Enemy(Sprite):
    MOVEMENTS = [LEFT, RIGHT]
    X_POS_LIST = [50, 100, 150, 200, 250, 350, 400, 450, 500, 550]
    Y_POS = 20
    VARIANTS = {
        1: {
            'image': ENEMY_1,
            'speed_x': 5,
            'speed_y': 1,
            'move_x': (30, 100)
        },
        # No es necesario agregar el atributo de resistencia de balas a Enemy
        # 2: {
        #     'image': ENEMY_2,
        #     'speed_x': 5,
        #     'speed_y': 2,
        #     'move_x': (50, 120)
        # }
    }
    
    def __init__(self, variant):
        enemy_variant = self.VARIANTS[variant]
        self.image = pygame.transform.scale(enemy_variant['image'], (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.type = ENEMY_TYPE
        
        self.speed_x = enemy_variant['speed_x']
        self.speed_y = enemy_variant['speed_y']
        
        self.movement = random.choice(self.MOVEMENTS)
        lower_limit, upper_limit = enemy_variant['move_x']
        self.move_x = random.randint(lower_limit, upper_limit)
        self.moving_index = 0

    def update(self, ships, game):
        self.rect.y += self.speed_y
        self.shoot(game.bullet_manager, game.enemy_manager)  # Lógica de disparo agregada

        if self.movement == LEFT:
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x
            
        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)
            self.generate_new_enemy(game.enemy_manager)  # Generamos un nuevo enemigo aleatorio
            
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
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
    def shoot(self, bullet_manager, enemy_manager):
        bullet = Bullet(self.type, self.rect.center)
        bullet_manager.add_bullet(bullet)

        
    def generate_new_enemy(self, enemy_manager):
        enemy_variant = random.randint(1, 2)
        new_enemy = Enemy(enemy_variant)
        enemy_manager.enemies.append(new_enemy)
