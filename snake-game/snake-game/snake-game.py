import pygame
import time
import random

# Initalizes pygame
pygame.init()

# Defines colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Defines display width and height
dis_width = 600
dis_height = 400


# Creates display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

# Sets fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("bahnschrift", 35)

# A function to display the score of the player on the screen
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

# A function to draw the snake on the screen
# Draws a rectangle at every position in snake_list of size snake_block
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# A function to display messages
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# The main function of the game
def gameLoop():
    game_over = False
    game_close = False

    # START CODING HERE

    # 1. Set x1 and y1 (the position of the block) to the center of the screen
    x1 = 300
    y1 = 200
    # 2. Set x1_change and y1_change to 0 since the snake isn't moving yet
    x1_change = 300
    y1_change = 200
    # A list that will change as the snake gets bigger
    snake_List = []
    # Sets the initial length of the snake to 1
    snake_length = 1

    #Position the food (foodx, foody) to a random location using random module
    foodx = random.randrange(1, 601)
    foody = random.randrange(1, 401)
    #While the game is not over
    while not game_over:

        # A loop to determines what happens after the player loses
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # START CODING HERE
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            # If the user presses an arrow key
                # 3. Create if-statements that determine how the position of the snake
                #   changes depending on which arrow key is pressed
                #   Hint: Change the variables x1_change and y1_change
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP):
                    y1_change= y1_change - snake_block
                if (event.key == pygame.K_DOWN):
                    y1_change = y1_change + snake_block
                if (event.key == pygame.K_RIGHT):
                    x1_change = x1_change + snake_block
                if (event.key == pygame.K_LEFT):
                    x1_change = x1_change - snake_block


        # 4. Check if the position of x1 or y1 is outside of the display
        # 5. Add the change of the position to the position
        if x1_change > dis_width:
            x1_change = dis_width
        if y1_change > dis_height:
            y1_change = dis_height

        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        # 6. Create an empty list for the current position of the snake
        snakePosHist_List = []
        # 7. Append the current position of the snake to the list
<<<<<<< HEAD
        if (x1_change >= 0) & (y1_change >= 0):
=======
        for (x1_change >= 0) & (y1_change >= 0):
>>>>>>> 891d243888ade9f319fc9827ddfefc902c635ff2
            snakePosHist_List.append(x1_change)
            snakePosHist_List.append(y1_change)

        #    Hint: You're creating a list with the length of two where
        #          [0] is x and [1] is y

        # 8. Add the new list you just created to snake_List
        for coordinates in snakePosHist_List:
            snake_List.append(snakePosHist_List[coordinates])

        # 9. If the length of snake_List is bigger than the snake_length,
        #   delete the first index of snake_List
        #   NOTE: You want to do this because you want snake_List to only contain
        #       lists of positions on the display that your snake is occupying.
        #       So you're deleting positions your snake has moved off of
        #       (which would be the oldest entry)

        if len(snake_List) > snake_length:
            snake_List.remove(snake_List[0])

        # 10. Check if any part of your snake is touching any other part of your snake
        #   If so, end the game
        currentSnakePos = x1_change, y1_change
        currentFoodPos = foodx, foody

        our_snake(snake_block, snake_List)
        Your_score(snake_length - 1)



        # 11. Check if the position of the snake's head matches the position of the food
        #   If so, randomly generate a new food item
        #   And increase the length of the snake by 1
        if currentSnakePos == currentFoodPos:
            snake_length += 1

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
