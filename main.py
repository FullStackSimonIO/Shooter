import pygame

# init game engine
pygame.init()

# height == 80% of width
screen_width = 1080
screen_height = int(screen_width * 0.8)

# Build Window + Game Title as Caption
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shooter Game")


x = 200
y = 200
img = pygame.image.load('img/player/Idle/0.png')
rect = img.get_rect()
rect.center = (x, y)


running = True
while (running):
    for event in pygame.event.get():
        # Pygame event handler for quitting game with "x"
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
