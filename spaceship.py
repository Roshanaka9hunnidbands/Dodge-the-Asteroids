import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dodge the Asteroids!")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player
player_image = pygame.image.load("spaceship.png")  # You need to have a spaceship image
player_width = 64
player_height = 64
player_x = (screen_width - player_width) // 2
player_y = screen_height - player_height - 20
player_speed = 5

# Asteroids
asteroids = []
asteroid_speed = 3

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    # Spawn new asteroid
    if random.randint(1, 100) == 1:
        asteroid_x = random.randint(0, screen_width - player_width)
        asteroid_y = 0
        asteroids.append([asteroid_x, asteroid_y])

    # Move and draw asteroids
    for asteroid in asteroids:
        asteroid[1] += asteroid_speed
        pygame.draw.circle(screen, WHITE, (asteroid[0], asteroid[1]), 20)
        if asteroid[1] > screen_height:
            asteroids.remove(asteroid)
            score += 1

    # Draw player
    screen.blit(player_image, (player_x, player_y))

    # Draw score
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    # Check for collisions
    for asteroid in asteroids:
        distance = math.sqrt((player_x - asteroid[0])**2 + (player_y - asteroid[1])**2)
        if distance < 32:  # Assuming player and asteroid are both 32x32
            running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()