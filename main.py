import pygame

# init game engine
pygame.init()

# Clock
clock = pygame.time.Clock()
FPS = 60

# height == 80% of width
screen_width = 1080
screen_height = int(screen_width * 0.8)

# Build Window + Game Title as Caption
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shooter Game")

# Define Player Action Variables
moving_left = False
moving_right = False

# Define Colors
BG = (144, 201, 120)


def draw_bg():
    screen.fill(BG)


class Soldier(pygame.sprite.Sprite):

    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.flip = False
        img = pygame.image.load(f'img/{self.char_type}/Idle/0.png')
        self.image = pygame.transform.scale(
            img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move(self, moving_left, moving_right):
        # Reset Movement Variables
        dx = 0
        dy = 0

        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1

        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        # Update Rectangle Position
        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        screen.blit(pygame.transform.flip(
            self.image, self.flip, False), self.rect)


player = Soldier('player', 200, 200, 3, 5)
enemy = Soldier('enemy', 200, 200, 3, 5)


running = True
while (running):
    clock.tick(FPS)
    draw_bg()

    player.draw()
    enemy.draw()
    player.move(moving_left, moving_right)

    for event in pygame.event.get():
        # Pygame event handler for quitting game with "x"
        if event.type == pygame.QUIT:
            running = False
        # keyboard Button Presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_ESCAPE:
                running = False

        # Keyboard Button Releases
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False

    pygame.display.update()

pygame.quit()
