




import pygame


pygame.init()
screen =pygame.display.set_mode((800,600))

background = pygame.image.load("naruto.png")
icon = pygame.image.load("iconnar.png")

pygame.display.set_icon(icon)
pygame.display.set_caption("Space invader")

while True:
    screen.blit(background,(10,10))
    pygame.display.update()




#this part runs the whole game
