import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drawing Objects")

red = (255, 0, 0)
orange = (255, 100, 0)
yellow = (255, 200, 0)
brightgreen = (50, 255, 0)
green = (25, 100, 0)
brightblue = (0, 255, 255)
blue = (0, 100, 255)
solidblue = (0, 0, 255)
purple = (120, 0, 255)
pink = (255, 0, 240)
black = (0, 0, 0)
white = (255, 255, 255)
gray = (99, 99, 99)
darkgray = (45, 45, 45)
brown = (115, 45, 15)

display_surface.fill(white)
center = (300, 300)
radius = 300
pygame.draw.circle(display_surface, black, center, radius, 25)

start_line = (100, 300)
end_line = (500, 300)
pygame.draw.line(display_surface, black, start_line, end_line, 25)

start_line2 = (300, 100)
end_line2 = (300, 500)
pygame.draw.line(display_surface, black, start_line2, end_line2, 25)

top_left_x = 0
top_left_y = 0
width = 600
height = 600
data = (top_left_x, top_left_y, width, height)
pygame.draw.rect(display_surface, black, data, 25)

center = (100, 100)
radius = 100
pygame.draw.circle(display_surface, red, center, radius, 50)

center = (251, 240)
radius = 110
pygame.draw.circle(display_surface, orange, center, radius, 50)

center = (472, 512)
radius = 120
pygame.draw.circle(display_surface, yellow, center, radius, 50)

center = (500, 100)
radius = 130
pygame.draw.circle(display_surface, brightgreen, center, radius, 50)

center = (100, 500)
radius = 140
pygame.draw.circle(display_surface, blue, center, radius, 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()
