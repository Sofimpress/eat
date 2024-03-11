import pygame
import sys
from settings import *
from car import Car
from obs import Obstacle
from text2 import Text
from text import Text_Obj

# создание объектов
pygame.init()
screen = pygame.display.set_mode((SC_WIDTH, SC_HEIGHT))
clock = pygame.time.Clock()

left_text = Text_Obj(100, 20, obs.get_edible_score(), screen)
right_text = Text(650, 20, obs.get_edible_health(), screen)

#groops
all_sprites = pygame.sprite.Group()
items = pygame.sprite.Group() 

car = Car(PLAYER_Y, PLAYER_X, 'zane.png', pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN)
all_sprites.add(car)

for i in range(5):
    obs = Obstacle('flower.png', True)
    all_sprites.add(obs)
    items.add(obs)
for i in range(2):
    obs = Obstacle('fire.png', False)
    all_sprites.add(obs)
    items.add(obs)

#peremenn

score = 0
health = 100

# главный цикл
while True:
    # задержка
    clock.tick(FPS)
    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # изменение объектов, update
    car.update()
    all_sprites.update()
    left_text.update(eat.get_edible_score())
    right_text.update(hit.get_edible_score())

    #пересечение объектов, collisions
    eats = pygame.sprite.spritecollide(car, items, True)
    for eat in eats:
        if eat.get_edible() == True:
            score += 1
            obs = Obstacle('flower.png', True)
            all_sprites.add(obs)
            items.add(obs)

    hits = pygame.sprite.spritecollide(car, items, False)
    for hit in hits:
        if hit.get_edible() == False:
            health -= 10
            obs = Obstacle('fire.png', False)
            all_sprites.add(obs)
            items.add(obs)
    # обновление экрана
    screen.fill(BLACK)
    car.draw(screen)
    all_sprites.draw(screen)
    
    left_text.draw()
    right_text.draw()
    
    pygame.display.update()

