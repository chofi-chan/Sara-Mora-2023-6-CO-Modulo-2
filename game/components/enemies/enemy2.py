import pygame
import random
from pygame.sprite import Sprite
from game.utils.constants import ENEMY_2, ENEMY_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH
from game.components.bullets.bullet import Bullet

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
        self.bullet_counter = 0
        self.shooting_time = random.randint(30, 50)
        self.current_time = pygame.time.get_ticks()
        
    def update(self, ships, game):
        if self.descending:
            self.rect.y += self.speed_y
            if self.rect.y >= self.DESCENDING_HEIGHT:
                self.descending = False
        else:
            self.rect.y -= self.speed_y
            if self.rect.y <= self.Y_POS:
                self.descending = True
        
        self.shoot(game.bullet_manager, game.enemy_manager)  # Lógica de disparo agregada

        if self.movement == LEFT:
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x
        
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
        
    def shoot(self, bullet_manager, enemy_manager):
        current_time = pygame.time.get_ticks()
        if current_time - self.current_time > self.shooting_time:
            bullet = Bullet(ENEMY_TYPE, self.rect.center)
            bullet_manager.add_bullet(bullet)

            self.current_time = current_time
            self.shooting_time = random.randint(30, 50)

    def receive_bullet(self):
        self.bullet_counter += 1
        if self.bullet_counter >= 4:
            self.bullet_counter = 0
            self.kill()  # Eliminamos el enemigo actual de la lista
            self.generate_new_enemy()  # Generamos un nuevo enemigo aleatorio

    def generate_new_enemy(self):
        enemy_classes = [Enemy, Enemy2]
        new_enemy_class = random.choice(enemy_classes)
        new_enemy = new_enemy_class(random.randint(1, 2))
        self.enemy_manager.enemies[self.enemy_manager.enemies.index(self)] = new_enemy
