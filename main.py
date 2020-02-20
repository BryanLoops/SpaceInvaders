import pygame
import random

# Initialize the game
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('Images/background.png')

# Title and Icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('Images/rocket.png')
pygame.display.set_icon(icon)

# Player image and starting coordinates
player_img = pygame.image.load('Images/spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy image and starting coordinates
enemy_img = pygame.image.load('Images/alien.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(0, 300)
enemyX_change = 1
enemyY_change = 20


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y):
    screen.blit(enemy_img, (x, y))


# Game Loop
running = True
while running:

    # RGB config
    screen.fill((0, 0, 0))

    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # If keystroke is pressed check whether its right or left
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -2
            """if playerX == 0:
                playerX_change = 0"""
        if event.key == pygame.K_RIGHT:
            playerX_change = 2
            """if playerX == 736:
                playerX_change = 0"""
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 1
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -1
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
