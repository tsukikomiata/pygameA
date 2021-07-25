import pygame as pg

pg.init()
clock = pg.time.Clock()
FPS = 10

w, n = input('Введите размер поля и кол-во клеток ').split()
w = int(w)
n = int(n)
size = (w, w)

screen = pg.display.set_mode(size)
black_color = (0, 0, 0)
white_color = (255, 255, 255)
vol = n
window_size = w/n
colors = [black_color, white_color]

index = 0
for y in range(vol):
    for x in range(vol):
        pg.draw.rect(screen, colors[index], (x * window_size, y * window_size, window_size, window_size))
        index ^= True
    index = index ^ True if (vol % 2 == 0) else index

pg.display.flip()

while pg.event.wait().type != pg.QUIT:
    pass

pg.quit()