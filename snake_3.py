#@jamaludeen madaki snake game using pygame
import pygame
import time
import random

try:
    pygame.init()
except pygame.error as e:
    print(f"Error initializing pygame: {e}")
    raise SystemExit("Pygame could not be initialized. Please ensure it's installed correctly.")

# Define colors for the game
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Define dimensions of the game window
dis_width = 800
dis_height = 600

try:
    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Snake Game by xAI')
except pygame.error as e:
    print(f"Error setting up display: {e}")
    raise SystemExit("Failed to set up the game display. Check your video settings or drivers.")

clock = pygame.time.Clock()
snake_block = 10  # Size of each snake segment
snake_speed = 15  # Initial game speed in frames per second

# Fonts for messages and score
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Load sounds
try:
    eat_sound = pygame.mixer.Sound("eat.wav")
    game_over_sound = pygame.mixer.Sound("game_over.wav")
    pygame.mixer.music.load("background_music.mp3")
    pygame.mixer.music.set_volume(0.5)  # Set music volume to 50%
except pygame.error as e:
    print(f"Error loading sounds: {e}")
    raise SystemExit("Failed to load game sounds. Check if the sound files exist in the correct directory.")

def our_snake(snake_block, snake_list):
    """Draw the snake on the screen."""
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    """Display a message on the screen."""
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    """Main game loop where the snake game logic is handled."""
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
    try:
        pygame.mixer.music.play(-1)  # -1 means loop forever
    except pygame.error as e:
        print(f"Error playing background music: {e}")

    while not game_over:
        try:
            while game_close:
                dis.fill(blue)
                message("You Lost! Press Q-Quit or C-Play Again", red)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            return gameLoop()  # Restart game by calling gameLoop again

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.KEYDOWN:
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

            # Check if snake has hit the wall
            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                try:
                    game_over_sound.play()
                except pygame.error:
                    print("Could not play game over sound.")
                game_close = True

            x1 += x1_change
            y1 += y1_change
            dis.fill(blue)
            pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

            # Update snake position
            snake_Head = [x1, y1]
            snake_List.append(snake_Head)

            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            # Check for self-collision
            for x in snake_List[:-1]:
                if x == snake_Head:
                    try:
                        game_over_sound.play()
                    except pygame.error:
                        print("Could not play game over sound.")
                    game_close = True

            our_snake(snake_block, snake_List)
            pygame.display.update()

            if x1 == foodx and y1 == foody:
                try:
                    eat_sound.play()
                except pygame.error:
                    print("Could not play eat sound.")
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake += 1

            # Display score
            score = score_font.render("Score: " + str(Length_of_snake - 1), True, black)
            dis.blit(score, [0, 0])

            clock.tick(snake_speed)

        except Exception as e:
            print(f"An error occurred in the game loop: {e}")
            game_over = True

    # Ensure music stops and pygame quits properly
    pygame.mixer.music.stop()
    pygame.quit()
    quit()

if __name__ == "__main__":
    gameLoop()



"""
Error Handling: Added try-except blocks to catch and report issues
with initializing pygame, setting up the display, loading sounds,
and playing sounds or music.
Comments: Expanded comments to explain the function of each part of the
code more thoroughly.
Game Loop: Included error handling for potential exceptions during gameplay.
Code Structure: Improved readability with more structured comments and function descriptions.

This version should provide better feedback in case of errors, making debugging or troubleshooting easier. Remember to have your sound files (eat.wav, game_over.wav,
background_music.mp3) in the same directory or adjust the paths accordingly.

"""
