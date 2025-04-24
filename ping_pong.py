from pygame import *


# вынесем размер окна в константы для удобства
# W - width, ширина
# H - height, высота
WIN_W = 700
WIN_H = 500

size = 175

x1 = 0
x2 =650
y1 =0
y2 =0

speed = 5
FPS = 60
width = 50
class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h):
        self.image = transform.scale(
            image.load(img),
            # здесь - размеры картинки
            (w, h)
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, img, x, y, w, h, speed=speed):
        super().__init__(img,x,y,w,h)
        self.speed = speed

    def update(self, up, down):
        keys_pressed = key.get_pressed()
        if keys_pressed[up] and self.rect.y >5:
            self.rect.y-= speed

        if keys_pressed[down] and self.rect.y < WIN_H - size:
            self.rect.y += speed


class Ball(Player):
    def __init__(self, img, x, y, w, h, speed=speed):
        super().__init__(img, x, y, w, h, speed)
        self.speed_x = speed
        self.speed_y = speed
    def update(self):
        if self.rect.x <= 0 or self.rect.x >= WIN_W - self.rect.width:
            self.speed_x *= -1
        if self.rect.y <= 0 or self.rect.y >= WIN_H - self.rect.height:
            self.speed_y *= -1

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
            

# создание окна размером 700 на 500
window = display.set_mode((WIN_W, WIN_H))

clock = time.Clock()

# название окна
display.set_caption("пингпонг")

# задать картинку фона такого же размера, как размер окна

background = GameSprite('pole_chill_gey.jpg', 0,0, WIN_W, WIN_H)

a = Player('chill_gay_vpravo .png', x1,y1, width, size)
b = Player('chill_gay_vlevo.png', x2,y2, width, size)
ball =Ball('бабуз.png', WIN_W/2, WIN_H/2, size, size)
# игровой цикл
game = True
while game:
    background.draw(window)
    a.draw(window)
    b.draw(window)
    ball.draw(window)
    a.update(K_w, K_s)
    b.update(K_UP, K_DOWN)
    ball.update()
    if sprite.collide_rect(ball, a) or sprite.collide_rect(ball, b):
            ball.speed_x *= -1
    for e in event.get():
        # выйти, если нажат "крестик"
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)