import pygame

pygame.init()


# Crea una ventana de 640x480
screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption("Test Game")

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

