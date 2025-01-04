import pygame
import time
import random

pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Define dimensions
dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by xAI')

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Load sounds
eat_sound = pygame.mixer.Sound("eat.wav")  # Sound for eating food
game_over_sound = pygame.mixer.Sound("game_over.wav")  # Sound for game over
pygame.mixer.music.load("background_music.mp3")  # Background music
pygame.mixer.music.set_volume(0.5)  # Set music volume to 50%

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# ... updates from gameloop(

def gameLoop():  # Creating a function
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # Start background music
    pygame.mixer.music.play(-1)  # -1 means loop forever

    # Initial speed
    snake_speed = 15  # Start at 15 frames per second
    speed_increase_rate = 0.1  # Increase speed by this amount per point scored

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over_sound.play()
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_over_sound.play()
                game_close = True

        our_snake(snake_block, snake_List)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            eat_sound.play()
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

            # Smooth speed increase
            snake_speed = max(1, snake_speed - speed_increase_rate)  # Increase speed by reducing frame delay

        score = score_font.render("Score: " + str(Length_of_snake - 1), True, black)
        dis.blit(score, [0, 0])

        clock.tick(snake_speed)  # Update the game speed

    pygame.mixer.music.stop()  # Stop the music when the game ends
    pygame.quit()
    quit()

gameLoop()


"""
Smooth Speed Increase: Instead of increasing the speed in discrete steps,
we now increase snake_speed by a small amount (speed_increase_rate) each
time the snake eats food. 
max Function: We use max(1, snake_speed - speed_increase_rate) to ensure
that snake_speed doesn't go below 1, which would make the game unplayably fast. Here, subtracting from snake_speed effectively
increases the speed since clock.tick() will update more frequently with a lower number.
Speed Increase Rate: speed_increase_rate is set to 0.1, which means the
game speed will subtly increase over time. You can adjust this value to
make the speed change faster or slower according to your preference.

"""
