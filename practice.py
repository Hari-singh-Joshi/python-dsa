import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("I Love You Niki")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.SysFont('Comic Sans MS', 50)

# Text settings
text = "I Love You Niki"
text_surface = font.render(text, True, RED)

# Create a function to draw a simple cartoon character
def draw_cartoon(x, y):
    # Draw head
    pygame.draw.circle(screen, BLUE, (x, y), 50)
    pygame.draw.circle(screen, WHITE, (x - 20, y - 10), 10)  # Left eye
    pygame.draw.circle(screen, WHITE, (x + 20, y - 10), 10)  # Right eye
    pygame.draw.arc(screen, BLACK, (x - 30, y, 60, 30), 3.14, 0, 2)  # Smile

    # Draw body
    pygame.draw.line(screen, BLUE, (x, y + 50), (x, y + 150), 5)

    # Draw arms
    pygame.draw.line(screen, BLUE, (x, y + 70), (x - 50, y + 100), 5)
    pygame.draw.line(screen, BLUE, (x, y + 70), (x + 50, y + 100), 5)

    # Draw legs
    pygame.draw.line(screen, BLUE, (x, y + 150), (x - 30, y + 200), 5)
    pygame.draw.line(screen, BLUE, (x, y + 150), (x + 30, y + 200), 5)

# Animation loop
x, y = 200, 200  # Initial position of the cartoon character
text_x, text_y = WIDTH, HEIGHT // 2  # Start position for the text animation

running = True
while running:
    screen.fill(WHITE)  # Fill the background with white
    draw_cartoon(x, y)  # Draw the cartoon at its position

    # Animate text
    if text_x > WIDTH // 2 - 150:  # Stop moving once it's centered
        text_x -= 5
    screen.blit(text_surface, (text_x, text_y))

    # Handle events (close window, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the screen
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)

