import pygame
import random

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Set the title and logo of the window
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('images/spaceship.png')
pygame.display.set_icon(icon)

# Add Player
playerImg = pygame.image.load('images/player2.png')
playerImg = pygame.transform.scale(playerImg, (58, 58))
playerX = 370
playerY = 480
playerX_change = 0

# Add Enemy
enemyImg = pygame.image.load('images/enemy.png')
enemyImg = pygame.transform.scale(enemyImg, (58, 58))
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.2
enemyY_change = 30


# Function to draw the player on the screen
def player(x, y):
    screen.blit(playerImg, (x, y))


# Function to draw the enemy on the screen
def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Keep game in an infinite loop until closed
running = True
while running:
    # Fill the screen with a background color
    screen.fill((0, 0, 0))

    # Add event to close game when user clicks the close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Add keystroke event for when the left or right keys are pressed
    if event.type == pygame.KEYDOWN:
        # Player should move left when the left arrow is pressed
        if event.key == pygame.K_LEFT:
            playerX_change = -0.2

        # Player should move right when the right arrow is pressed
        if event.key == pygame.K_RIGHT:
            playerX_change = 0.2

    # Add keystroke event for when the left or right keys are released
    if event.type == pygame.KEYUP:
        # Player should stop moving when left or right arrow is released
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    # Move the player on the screen
    playerX += playerX_change

    # Check if the player is out of the screen
    if playerX <= 0:
        playerX = 0
    elif playerX >= 742:
        playerX = 742

    # Move the enemy on the screen
    enemyX += enemyX_change

    # Check if the enemy is out of the screen
    if enemyX <= 0:
        enemyX_change = 0.2
        enemyY += enemyY_change
    elif enemyX >= 742:
        enemyX_change = -0.2
        enemyY += enemyY_change

    # Draw the player on the screen
    player(playerX, playerY)

    # Draw the enemy on the screen
    enemy(enemyX, enemyY)

    # Update the screen
    pygame.display.update()
