from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class RightPlat(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < win_height - 120:
            self.rect.y += self.speed

class LeftPlat(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < win_height - 120:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__(player_image, player_x, player_y, player_speed, width, height)
        self.original_image = image.load(player_image)
        self.original_image = transform.scale(self.original_image, (width, height))
        self.image = self.original_image
        self.angle = 0

        self.speed_x = 4
        self.speed_y = 4
        
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.y <= 0 or self.rect.y >= win_height - 50:
            self.speed_y *= -1

        if sprite.collide_rect(self, rplat) or sprite.collide_rect(self, lplat):
            self.speed_x *= -1

        self.angle += 2
        self.image = transform.rotate(self.original_image, self.angle)

# Persons
rplat = RightPlat('blue.jpg', 600, 200, 5, 10, 100)
lplat = LeftPlat('blue.jpg', 100, 200, 5, 10, 100)

ball = Ball('ball.png', 325, 225, 5, 50, 50)

# Scene
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping-Pong')
background = transform.scale(image.load('background.jpg'), (win_width, win_height))



game = True
finish = False
clock = time.Clock()
FPS = 60


# Cycle
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0, 0))
        rplat.update()
        lplat.update()
        ball.update()

        rplat.reset()
        lplat.reset()
        ball.reset()

        if ball.rect.x <= -50:
            finish = True
        
        if ball.rect.x >= 650:
            finish = True

    display.update()
    clock.tick(FPS)
