import random
from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy2 import Enemy2

class EnemyManager:
    def __init__(self):
        self.enemies = []
    
    def update(self, game):
        if not self.enemies:
            enemy_variant = random.randint(1, 2)
            if enemy_variant == 1:
                self.enemies.append(Enemy(enemy_variant))
            elif enemy_variant == 2:
                self.enemies.append(Enemy2())
            
        for enemy in self.enemies:
            enemy.update(self.enemies, game)
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

        