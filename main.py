import pygame
import grid

pygame.init()
scene = pygame.display.set_mode((1024, 700))
scene.fill([0,0,0])

g1 = grid.Grid(scene, 25, 10, 25,25,64,650, [255,255,255])
g1.setup()
g2 = grid.Grid(scene, 25, 10, 25, 25, 500, 650, [255,255,255])
g2.setup()
g1.update((0,0), [215,0,0])



running = True
while running:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
    
    
    pygame.display.update()
    