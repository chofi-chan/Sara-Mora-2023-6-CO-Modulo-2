import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT

class Spaceship:
    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (60, 40))
        self.rect = self.image.get_rect()
        self.rect.x = 520
        self.rect.y = 500
        
    def update(self, user_imput):
        if user_imput[pygame.K_a]:
            self.move_left()
            print(user_imput)
        elif user_imput[pygame.K_d]:
            self.move_right()
        elif user_imput[pygame.K_w]:
            self.move_up()
        elif user_imput[pygame.K_s]:
            self.move_down()
            
    def move_left(self):
        print("lef")
        if self.rect.left > 50:
            self.rect.x -= 10
    
    def move_right(self):
        print("rig")
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10
            
    def move_up(self):
        print("above")
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= 10
    def move_down(self):
        print("below")
        if self.rect.y < SCREEN_HEIGHT - 50: 
            self.rect.y += 10             
        
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        

       