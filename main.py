import pygame, sys
from pygame.locals import *
pygame.init()
pygame.display.init()
running = True

GREEN = (0,255,0)
RED = (255,0,0)
FPS = 60
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((400,400))
color = RED
while running:
  color = RED
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.key == pygame.K_SPACE:
      color = GREEN
  DISPLAYSURF.fill(color)
  pygame.display.update()
  FPSCLOCK.tick(FPS)