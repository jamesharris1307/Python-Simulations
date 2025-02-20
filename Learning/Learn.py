import pygame
import math

# Pygame setup
pygame.init()
pygame.display.set_caption("James Harris")

# Set Pygame window resolution
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

(pygame.mouse.set_visible(False))

# Load Character Sprites
spider_idle = pygame.image.load("spiderIdle.png")
spider_walk = [
    pygame.image.load("spiderWalk1.png"),
    pygame.image.load("spiderWalk2.png")
]

# Resize Sprites (Divide Spider Size by 2)
scale_factor = 0.25
new_size = (int(spider_idle.get_width() * scale_factor), int(spider_idle.get_height() * scale_factor))

spider_idle = pygame.transform.smoothscale(spider_idle, new_size)
spider_walk = [pygame.transform.smoothscale(sprite, new_size) for sprite in spider_walk]

# Character Variables
spider_x, spider_y = 800 // 2, 600 // 2
spider_speed = 3  # Adjust speed
current_sprite = spider_idle
frame_index = 0
animation_speed = 10
frame_counter = 0
stop_threshold = 5 # Minimum distance before moving (Prevents Cursor Movement Crazy)

# Function to rotate the sprite towards the cursor
def get_rotated_sprite(sprite, x, y):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    angle = math.degrees(math.atan2(mouse_y - y, mouse_x - x))
    rotated_sprite = pygame.transform.rotate(sprite, -angle)  # Negate angle to match rotation
    return rotated_sprite, rotated_sprite.get_rect(center=(x, y))

# Main Loop
while running:
    for event in pygame.event.get():

        # Quit Logic
        if event.type == pygame.QUIT:
            running = False
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False

    # Set Background
    screen.fill((50, 50, 50))  # Background Color White

    # Get Mouse Position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Calculate Direction Vector
    direction_x = mouse_x - spider_x
    direction_y = mouse_y - spider_y

    # Normalize Direction (to prevent fast movement close to the cursor)
    distance = math.sqrt(direction_x ** 2 + direction_y ** 2)
    if distance > stop_threshold:
        direction_x /= distance
        direction_y /= distance
    else:
        direction_x = 0
        direction_y = 0

    # Movement Handling (Move Towards Mouse)
    keys = pygame.key.get_pressed()
    moving = False  # Track if character is moving

    if keys[pygame.K_LSHIFT]:
        speed = spider_speed * 2.5
        stop_threshold = 10
    else:
        speed = spider_speed
        stop_threshold = 5

    if keys[pygame.K_w]:  # Move in the mouse's direction
        spider_x += direction_x * speed
        spider_y += direction_y * speed
        moving = True
    if keys[pygame.K_s]:
        spider_x -= direction_x * speed
        spider_y -= direction_y * speed
        moving = True
    if keys[pygame.K_a]:
        spider_x -= speed / 1.5
        moving = True
    if keys[pygame.K_d]:
        spider_x += speed / 1.5
        moving = True

    # Animate Sprite
    if moving:
        frame_counter += 1
        if frame_counter >= animation_speed:
            frame_index = (frame_index + 1) % len(spider_walk)
            frame_counter = 0
        current_sprite = spider_walk[frame_index]
    else:
        current_sprite = spider_idle

    # Rotate the sprite towards the mouse
    rotated_sprite, sprite_rect = get_rotated_sprite(current_sprite, spider_x, spider_y)

    # Draw Spider
    screen.blit(rotated_sprite, sprite_rect.topleft)

    pygame.display.flip()

    # Max FPS = 60fps
    clock.tick(60)

pygame.quit()
