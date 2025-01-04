# ... adding speed 

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
    snake_speed = 15  # You can adjust this initial speed

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

            # Increase speed based on score
            if (Length_of_snake - 1) % 5 == 0:  # Every 5 points, increase speed
                snake_speed += 1

        score = score_font.render("Score: " + str(Length_of_snake - 1), True, black)
        dis.blit(score, [0, 0])

        clock.tick(snake_speed)  # Update the game speed

    pygame.mixer.music.stop()  # Stop the music when the game ends
    pygame.quit()
    quit()

gameLoop()



"""
Speed Increase: After the snake eats food (if x1 == foodx and y1 == foody:), we check if the score (Length_of_snake - 1) is divisible by 5. If it is, we increase the snake_speed by 1. This makes the game progressively harder as the player scores more points.
Initial Speed: The initial speed is set to 15, but you can adjust this value to make the game start at a different speed.
Speed Adjustment: clock.tick(snake_speed) now uses the variable snake_speed which changes throughout the game, thus dynamically adjusting the game's pace.

"""
