import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

run = True

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


def startExitIcon(sx, sy, ex, ey):
    screen.blit(startIcon, (sx, sy))
    screen.blit(exitIcon, (ex, ey))


while run:
    screen.fill((0, 0, 0))

    bg_img = pygame.image.load('images/frontimg.png')
    screen.blit(bg_img, (0, -100))

    titleText(titleX, titleY)
    startExitIcon(sx, sy, ex, ey)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                px, py = pygame.mouse.get_pos()
                # print(px)
                # print(py)
                if px >= sx and px <= sx + 64 and py >= sy and py <= sy + 64:
                    print('start')

                elif px >= ex and px <= ex + 64 and py >= ey and py <= ey + 64:
                    print('exit')

    pygame.display.update()
