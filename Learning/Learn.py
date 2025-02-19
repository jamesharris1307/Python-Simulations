import pygame

# Pygame setup
pygame.init()
pygame.display.set_caption("James Harris")

# Set Pygame window resolution
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# Main Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0)) # Background Color Black

    pygame.display.flip()

    clock.tick(60)

pygame.quit()