# Shapes module
import config
import pygame

# Shapes
def draw_polygon(screen, color, coords, width):
    pygame.draw.polygon(screen, color, coords, width)

def draw_rect(screen, color, coords, width):
    pygame.draw.rect(screen, color, coords, width)

def draw_line(screen, color, start_pos, end_pos, width):
    pygame.draw.line(screen, color, start_pos, end_pos, width)

def draw_circle(screen, color, center, radius, width):
    pygame.draw.circle(screen, color, center, radius, width)