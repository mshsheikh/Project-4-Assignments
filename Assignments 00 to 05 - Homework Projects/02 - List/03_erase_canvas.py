print("\n-- -- -- -- -- -- --")
print("     02 - LIST        ")
print("   Erase  Canvas      ")
print("-- -- -- -- -- -- --")

print('''
** ** ** ** ** ** ** ** ** ** ** ** ** **
    THIS PROGRAM CREATES A BLUE CANVAS
  AND ALLOWS YOU TO ERASE PORTIONS OF IT
       USING A RECTANGULAR ERASER
** ** ** ** ** ** ** ** ** ** ** ** ** **
      
import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
GRID_COLS = WIDTH // CELL_SIZE
GRID_ROWS = HEIGHT // CELL_SIZE
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ERASER_SIZE = 40  # Size of the eraser rectangle

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Canvas Eraser")
clock = pygame.time.Clock()

# Create the canvas - initially all blue
canvas = [[BLUE for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]

# Eraser properties
eraser_rect = pygame.Rect(0, 0, ERASER_SIZE, ERASER_SIZE)
dragging = False

def draw_canvas():
    """Draw the canvas grid"""
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, canvas[row][col], rect)
            pygame.draw.rect(screen, BLACK, rect, 1)  # Grid lines

def apply_eraser():
    """Set all cells under the eraser to white"""
    # Get the cells covered by the eraser
    left_col = max(0, eraser_rect.left // CELL_SIZE)
    right_col = min(GRID_COLS - 1, eraser_rect.right // CELL_SIZE)
    top_row = max(0, eraser_rect.top // CELL_SIZE)
    bottom_row = min(GRID_ROWS - 1, eraser_rect.bottom // CELL_SIZE)
    
    # Erase those cells
    for row in range(top_row, bottom_row + 1):
        for col in range(left_col, right_col + 1):
            canvas[row][col] = WHITE

def main():
    global dragging, eraser_rect
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if eraser_rect.collidepoint(event.pos):
                        dragging = True
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    dragging = False
            
            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    # Move the eraser to mouse position (centered)
                    eraser_rect.center = event.pos
                    apply_eraser()
        
        # Draw everything
        screen.fill(WHITE)
        draw_canvas()
        
        # Draw the eraser (semi-transparent)
        eraser_surface = pygame.Surface((ERASER_SIZE, ERASER_SIZE), pygame.SRCALPHA)
        pygame.draw.rect(eraser_surface, (255, 255, 255, 128), (0, 0, ERASER_SIZE, ERASER_SIZE))
        pygame.draw.rect(eraser_surface, BLACK, (0, 0, ERASER_SIZE, ERASER_SIZE), 2)
        screen.blit(eraser_surface, eraser_rect)
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
''')

footer_A : str = "\nCoded by Artificial Intelligence\n"
print(footer_A)
