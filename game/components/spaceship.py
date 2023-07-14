import pygame
from pygame.locals import *
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT

class Spaceship:
    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (60, 40))
        self.rect = self.image.get_rect()
        self.rect.x = 520
        self.rect.y = 500
        self.is_w_pressed = False
        self.is_a_pressed = False
        self.is_d_pressed = False
        
    def update(self, user_input):
        self.is_w_pressed = user_input[pygame.K_w]
        self.is_a_pressed = user_input[pygame.K_a]
        self.is_d_pressed = user_input[pygame.K_d]
        
        if self.is_a_pressed:
            if self.is_w_pressed:
                self.move_up_left()
            else:
                self.move_left()
        elif self.is_d_pressed:
            if self.is_w_pressed:
                self.move_up_right()
            else:
                self.move_right()
        elif self.is_w_pressed:
            self.move_up()
        elif user_input[pygame.K_s]:
            self.move_down()
            
    def move_left(self):
        print("left")
        if self.rect.left > 50:
            self.rect.x -= 10
        else:
            self.rect.x = SCREEN_WIDTH - self.rect.width
    
    def move_right(self):
        print("right")
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10
        else:
            self.rect.x = 0
            
    def move_up(self):
        print("up")
        if self.rect.top > SCREEN_HEIGHT //  2:
            self.rect.y -= 10
            
    def move_down(self):
        print("down")
        if self.rect.bottom < SCREEN_HEIGHT - 50:
            self.rect.y += 10
    
    def move_up_left(self):
        print("up left")
        if self.rect.top > SCREEN_HEIGHT // 2 and self.rect.left > 50:
            self.rect.y -= 10
            self.rect.x -= 10
    
    def move_up_right(self):
        print("up right")
        if self.rect.top > SCREEN_HEIGHT // 2 and self.rect.right < SCREEN_WIDTH:
            self.rect.y -= 10
            self.rect.x += 10
            
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
  

       