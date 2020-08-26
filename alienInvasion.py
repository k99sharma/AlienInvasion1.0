""" Alien Invasion Game
    Version: 1.0
    Author: Kalash Sharma
    Github: ghost_32
    Date: 25 August 2020 """

# Importing libraries
import math
import random
import sys

import pygame

# Initializing pygame
pygame.init()

# screen
screen = pygame.display.set_mode((800, 600))

# Images
ship1 = 'images/spaceship.png'
ship2 = 'images/spaceship2.png'
ship3 = 'images/spaceship3.png'
ship4 = 'images/spaceship4.png'

enemy1 = 'images/alien.png'
enemy2 = 'images/alien2.png'
enemy3 = 'images/alien3.png'
enemy4 = 'images/alien4.png'

background1 = 'images/background.png'

front1 = 'images/front.png'
front2 = 'images/front2.png'

bullet1 = 'images/bullet.png'


# Title and icon
def titleAndIcon():
    # Game Window Name
    pygame.display.set_caption("Alien Invasion")

    # Game Window Icon
    icon = pygame.image.load('images/icon.png')
    pygame.display.set_icon(icon)


# Player
playerImg = pygame.image.load(ship2)

# initial ship coordinates to appear on starting of game
playerX = 370
playerY = 480
playerVel = 6


# Blitting ship image on the screen at given coordinates
def player(x, y):
    screen.blit(playerImg, (x, y))


# Ship Movement
def playerMovement(playerX, vel_change):
    # player movement
    playerX += vel_change

    # movement restrictions
    if playerX >= 736:
        playerX = 736

    elif playerX <= 0:
        playerX = 0

    return playerX


# Enemy

# Enemy image to load on the screen
enemyImg = pygame.image.load(enemy3)

# using list for multiple enemies
enemyX = []
enemyY = []
enemyVel = 5

# Number of enemies to appear on the screen
numberOfEnemies = 10

# getting random enemy position
for i in range(numberOfEnemies):
    enemyX_pos = random.randint(0, 736) + numberOfEnemies + 32
    enemyY_pos = random.randint(0, 200) + numberOfEnemies + 20

    if enemyX_pos not in enemyX:
        enemyX.append(enemyX_pos)

    if enemyY_pos not in enemyY:
        enemyY.append(enemyY_pos)


# Blitting enemy on the screen at given coordinates
def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Enemy movement
def enemyMovement(enemyX, enemyY, envel_change):
    # enemy movement
    enemyX += envel_change

    # Enemy Movement restrictions
    if enemyX >= 736:
        envel_change = -enemyVel
        enemyY += 28

    elif enemyX <= 0:
        envel_change = enemyVel
        enemyY += 28

    elif enemyY >= 650:
        envel_change = 0
        enemyY = 650

    return enemyX, enemyY, envel_change


# Bullets

# Bullet image
bulletImg = pygame.image.load(bullet1)
bulletX = 0
bulletY = 0
bullet_status = "ready"
bullet_vel = 7


# Blitting bullet on the screen at given coordinates
def bullet(x, y):
    screen.blit(bulletImg, (x, y))


# collision
def isCollision(x1, y1, x2, y2):
    dist = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
    if dist <= 30:
        return True

    return False


# Score
score = 0
font = pygame.font.Font('freesansbold.ttf', 25)
textX = 10
textY = 10


# showing score on the screen
def showScore(x, y):
    score_font = font.render('Score: {}'.format(score), True, (250, 250, 250))
    screen.blit(score_font, (x, y))


# lost
lostFontX = 300
lostFontY = 250


# Lost Case Scenario
def lost(x, y):
    lost_font = font.render('ALIENS GOT YOU !!!', True, (250, 250, 250))
    screen.blit(lost_font, (x, y))


# win
winFontX = 100
winFontY = 250


# Winning Case Scenario
def winner(x, y):
    win_font = font.render('YOU SMASHED THE ALIENS OUT OF THE ORBIT !', True, (250, 250, 250))
    screen.blit(win_font, (x, y))


# Font
title_font_text = pygame.font.Font('font/Banquet.ttf', 75)
titleX = 65
titleY = 220


def titleText(x, y):
    title_font = title_font_text.render('ALIEN INVASION', True, (20, 180, 140))
    screen.blit(title_font, (x, y))


# Start Exit Icon
startIcon = pygame.image.load('images/start.png')
exitIcon = pygame.image.load('images/exit.png')
sx = 250
sy = 400
ex = 520
ey = 400
waitCounter = 0


def startExitIcon(sx, sy, ex, ey):
    screen.blit(startIcon, (sx, sy))
    screen.blit(exitIcon, (ex, ey))


# main function
def game():
    global waitCounter  # end time sleep

    # Player Variables
    global playerX
    global playerVel
    vel_change = 0

    # Enemy Variables
    global enemyX
    global enemyY

    envel_change = []
    for k in range(numberOfEnemies):
        envel_change.append(enemyVel)

    # Bullet Variable
    global bulletX
    global bulletY
    global bullet_status
    global bullet_vel
    bullet_vel_change = bullet_vel

    # Score Variable
    global score

    # Title and Icon
    titleAndIcon()

    # Game Loop
    run = True

    while run:
        # background
        screen.fill((255, 255, 255))
        bg_img = pygame.image.load(background1)
        screen.blit(bg_img, (0, 0))

        for event in pygame.event.get():
            # checking if close option is clicked
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            # checking for key press
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    vel_change = -playerVel

                if event.key == pygame.K_RIGHT:
                    vel_change = playerVel

                # bullet firing conditions
                if bullet_status == "ready":
                    if event.key == pygame.K_SPACE:
                        # shooting bullets
                        bulletX = playerX + 12
                        bulletY = playerY - 12
                        bullet_status = "fired"
                        bullet_vel_change = bullet_vel

            if event.type == pygame.KEYUP:
                vel_change = 0

        # player movement
        playerX = playerMovement(playerX, vel_change)

        # enemy movement
        for k in range(numberOfEnemies):
            enemyX[k], enemyY[k], envel_change[k] = enemyMovement(enemyX[k], enemyY[k], envel_change[k])

        # bullet movement
        bulletY -= bullet_vel_change

        if bulletY <= -100:
            bullet_status = "ready"
            bullet_vel_change = 0

        # Collision
        for k in range(numberOfEnemies):
            alien_collision_status = isCollision(bulletX, bulletY, enemyX[k], enemyY[k])
            if alien_collision_status:
                score += 1

                # position of enemy to go after collision
                enemyY[k] = 2000
                bullet_status = "ready"

                # position of bullet after collision
                bullet_vel_change = 0
                bulletY = 2000

            # Lost Condition
            ship_collision_status = isCollision(playerX, playerY, enemyX[k], enemyY[k])
            if ship_collision_status:
                for _ in range(numberOfEnemies):
                    envel_change[_] = 0
                bullet_vel_change = 0
                vel_change = 0
                bullet_status = "fire"
                lost(lostFontX, lostFontY)

                waitCounter += 1

                # end time sleep condition
                if waitCounter == 400:
                    waitCounter = 0
                    return True

            # Winning Condition
            if score == numberOfEnemies:
                bullet_vel_change = 0
                bullet_status = "fire"
                vel_change = 0
                winner(winFontX, winFontY)

                waitCounter += 1
                if waitCounter == 400:
                    waitCounter = 0
                    return True

        # object to put on the screen
        showScore(textX, textY)
        player(playerX, playerY)

        # multiple enemies to be blitted on the screen
        for k in range(numberOfEnemies):
            enemy(enemyX[k], enemyY[k])
        bullet(bulletX, bulletY)

        # Updating Display
        pygame.display.update()


# Main Window
def main():
    main_run = True

    while main_run:
        screen.fill((0, 0, 0))

        # background of the front screen
        bg_img = pygame.image.load(front1)
        screen.blit(bg_img, (0, -100))

        # main text on the front screen
        titleText(titleX, titleY)
        startExitIcon(sx, sy, ex, ey)  # giving coordinates to start and exit icon

        # events of pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_run = False
                pygame.quit()

            # checking if mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left mouse button
                    px, py = pygame.mouse.get_pos()  # getting coordinates where mouse is clicked

                    if px >= sx and px <= sx + 64 and py >= sy and py <= sy + 64:
                        return 'start'

                    elif px >= ex and px <= ex + 64 and py >= ey and py <= ey + 64:
                        return 'exit'

        # updating display for changes
        pygame.display.update()


if __name__ == "__main__":
    # front screen
    main_flag = main()

    if main_flag == 'start':
        # if start button is pressed game will start
        game()

    else:
        sys.exit()
