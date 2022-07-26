import pygame, sys, time, random

# Mengecek error pygame
check_errors = pygame.init()
if check_errors[1] > 0:
    print("[:] {check_errors} error game")
else:
    print("[*] Game succes install")

# Window frame of Game

size_x = 720
size_y = 420

# Title Game
pygame.display.set_caption("My Snake")
screen = pygame.display.set_mode((size_x, size_y))

# ------------Game Variable----------------

# color
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
green = pygame.Color(0,255,255)

# snake
snake_body = [100,50]
snake_bodies = [[90,50], [80,50], [70,50]]
change_to = "RIGHT"
direction = "RIGHT"

# Food
food_body = [random.randrange(0, (size_x - 10)/10)*10, random.randrange(0, (size_y - 10)/10)*10]

# ------------Game Variable----------------

# Change Background to White
screen.fill(white)

# Running Game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
    # Update Screen to White
    screen.fill(white)

    # Create Snake
    for snake in snake_bodies:
        pygame.draw.ellipse(screen, green, pygame.Rect(snake[0], snake[1], 10, 10))

    # Create Food
    pygame.draw.rect(screen, green, pygame.Rect(food_body[0], food_body[1], 10, 10))

    # ---------------Snake Running------------------------------
    snake_bodies.insert(0, snake_body[:])
    snake_bodies.pop()

    # Fix Sure Move
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"

    if direction == "RIGHT":
        snake_body[0] += 10
    if direction == "LEFT":
        snake_body[0] -= 10
    if direction == "UP":
        snake_body[1] -= 10
    if direction == "DOWN":  
        snake_body[1] += 10
    
    # Snake Over Window
    if snake_body[0] >= size_x:
        snake_body[0] = 0
    if snake_body[0] < 0:
        snake_body[0] = size_x - 10
    if snake_body[1] >= size_y:
        snake_body[1] = 0
    if snake_body[1] < 0:
        snake_body[1] = size_y - 10

    
    print(food_body)
    

    # Level
    pygame.time.Clock().tick(10)

    # Update Screen
    pygame.display.update()