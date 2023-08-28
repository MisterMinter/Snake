import pygame
import sys
import random

# Constants
SCREEN_SIZE = (500, 500)  # Pulsing neon lights background size
GAME_SIZE = (5, 5)  # Game screen size
SCORE_POSITION = (10, 10)  # Position of the score counter
CELL_SIZE = 100  # Size of each cell in the game screen

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

# Game variables
score = 0
running = True
snake = [(2, 2)]  # Starting position of the snake
direction = "RIGHT"
food = (random.randint(0, 4), random.randint(0, 4))  # Random initial food position

# Main game loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = "UP"
            elif event.key == pygame.K_DOWN:
                direction = "DOWN"
            elif event.key == pygame.K_LEFT:
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT:
                direction = "RIGHT"

    # Game logic updates
    if direction == "UP":
        new_head = (snake[0][0], snake[0][1] - 1)
    elif direction == "DOWN":
        new_head = (snake[0][0], snake[0][1] + 1)
    elif direction == "LEFT":
        new_head = (snake[0][0] - 1, snake[0][1])
    elif direction == "RIGHT":
        new_head = (snake[0][0] + 1, snake[0][1])

    # Check if the snake ate the food
    if new_head == food:
        food = (random.randint(0, 4), random.randint(0, 4))
        score += 1
    else:
        snake.pop()  # Remove the tail

    snake.insert(0, new_head)

    # Check if the snake collided with itself or hit the screen edges
    if (
        new_head in snake[1:] or
        new_head[0] < 0 or new_head[0] >= GAME_SIZE[0] or
        new_head[1] < 0 or new_head[1] >= GAME_SIZE[1]
    ):
        running = False

    # Rendering
    screen.fill((0, 0, 0))  # Black background for neon lights
    # [Insert code to render the pulsing neon lights background here]

    # [Insert code to render the game screen here]
    for x in range(GAME_SIZE[0]):
        for y in range(GAME_SIZE[1]):
            rect = (
                x * CELL_SIZE, 
                y * CELL_SIZE, 
                CELL_SIZE, 
                CELL_SIZE
            )
            if (x, y) in snake:
                pygame.draw.rect(screen, (0, 255, 0), rect)  # Snake's body
            elif (x, y) == snake[0]:
                pygame.draw.rect(screen, (0, 200, 0), rect)  # Snake's head
            elif (x, y) == food:
                pygame.draw.rect(screen, (255, 0, 0), rect)  # Food

    # [Insert code to render the score counter here]
    score_font = pygame.font.Font(None, 32)
    score_text = score_font.render("Score: {}".format(score), True, (255, 255, 255))
    screen.blit(score_text, SCORE_POSITION)

    pygame.display.flip()
    clock.tick(10)  # Adjust game speed
```

2. `snake_gui.py` (Graphical User Interface):
```python
import pygame

# Constants
SCREEN_SIZE = (500, 500)  # Pulsing neon lights background size
GAME_SIZE = (5, 5)  # Game screen size
SCORE_POSITION = (10, 10)  # Position of the score counter

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

# [Insert necessary GUI initialization code here]
# ...

# Main game loop
while running:
    # [Insert code to handle GUI events here]
    # ...

    # Rendering
    screen.fill((0, 0, 0))  # Black background for neon lights
    # [Insert code to render the pulsing neon lights background here]
    # [In Warhol style, add vibrant neon lights]

    # [Insert code to render the game screen here]
    for x in range(GAME_SIZE[0]):
        for y in range(GAME_SIZE[1]):
            cell_size = SCREEN_SIZE[0] // GAME_SIZE[0]
            rect = (
                x * cell_size, 
                y * cell_size, 
                cell_size, 
                cell_size
            )
            if (x, y) in snake:
                pygame.draw.rect(screen, (0, 255, 0), rect)  # Snake's body
            elif (x, y) == snake[0]:
                pygame.draw.rect(screen, (0, 200, 0), rect)  # Snake's head
            elif (x, y) == food:
                pygame.draw.rect(screen, (255, 0, 0), rect)  # Food
            # [In Warhol style, use bold contrasting colors and patterns]

    # [Insert code to render the score counter here]
    score_font = pygame.font.Font(None, 32)
    score_text = score_font.render("Score: {}".format(score), True, (255, 255, 255))
    screen.blit(score_text, SCORE_POSITION)
    # [In Warhol style, use bold fonts and vivid color combinations]

    pygame.display.flip()
    clock.tick(10)  # Adjust game speed
