#Key Holding Code:
'''
import pygame, sys
pygame.init()
pygame.display.init()
running = True

GREEN = (0,255,0)
RED = (255,0,0)
FPS = 120
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((400,400))
color = RED

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE: 
        color = GREEN
    elif event.type == pygame.KEYUP:
      if event.key == pygame.K_SPACE:
        color = RED
  DISPLAYSURF.fill(color)
  pygame.display.update()
  FPSCLOCK.tick(FPS)
'''
#Dictionaries
'''
dictionary = {'Stick':2,'Apple':4}
print(dictionary['Stick'])
'''
