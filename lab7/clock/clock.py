import pygame
from datetime import datetime


pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()


background = pygame.image.load(r"mainclock.png")
leftarm = pygame.image.load(r"leftarm.png")
rightarm = pygame.image.load(r"rightarm.png")
bg_rect = background.get_rect(center = (400, 400))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    ct = datetime.now().time()

    sec_angle = -(ct.second * 6)
    min_angle = -(ct.minute * 6)
    rotated_leftarm = pygame.transform.rotate(leftarm, sec_angle - 3)
    rotated_rightarm = pygame.transform.rotate(rightarm, min_angle - 45)

    leftarm_rect = rotated_leftarm.get_rect(center = bg_rect.center)
    rightarm_rect = rotated_rightarm.get_rect(center = bg_rect.center)

    screen.blit(background, bg_rect)
    screen.blit(rotated_leftarm, leftarm_rect)
    screen.blit(rotated_rightarm, rightarm_rect)

    pygame.display.flip()
    clock.tick(60)
