import pygame
import sys
import config # Import the config module
import shapes

def init_game():
  pygame.init()
  screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
  pygame.display.set_caption(config.TITLE)
  return screen

def handle_events():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      return False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        return False
  return True

def draw_text(screen, text, font, color, x_cord, y_cord):
  img = font.render(text, True, color)
  screen.blit(img, (x_cord, y_cord))

def main():
  screen = init_game()
  clock = pygame.time.Clock() # Initialize the clock here
  running = True
  while running:
    running = handle_events()

    # Background
    # Sky
    screen.fill(config.SKY_BLUE)

    # Road
    shapes.draw_polygon(screen, config.ROAD, [(50, 600), (400, 300), (750, 600)], 0)

    # Off-road
    shapes.draw_polygon(screen, config.OFF_ROAD, [(0, 600), (0, 300), (800, 300), (800, 600), (750, 600), (400, 300), (50, 600)], 0)

    # Road border
    shapes.draw_polygon(screen, config.ROAD_BORDER, [(50, 600), (400, 300), (750, 600)], 1)
    
    # Fences

    # random sky blocks
    lines = 0
    offsetX = 0
    while lines < 5:
      shapes.draw_rect(screen, config.WHITE, [(150 + offsetX, 150), (50, 10)], 0)
      offsetX += 100
      lines += 1

    # Font
    font = pygame.font.SysFont("Agency FB Regular", 30, False, False)
    draw_text(screen, "Career Tech Center", font, config.BLACK, 300, 100)

    pygame.display.flip()
    
    # Limit the frame rate to the specified frames per second (FPS)
    clock.tick(config.FPS) # Use the clock to control the frame rate

  pygame.quit()
  sys.exit()

if __name__ == "__main__":
  main()
