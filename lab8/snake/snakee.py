import pygame as pg
import time
import random

pg.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

screen_width = 600
screen_height = 400

screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('Snake')

clock = pg.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pg.font.SysFont("arial", 25)
score_font = pg.font.SysFont("georgia",20)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    screen.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pg.draw.rect(screen, white, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 6])

def generate_food(snake_List):
    while True:
        foodx = round(random.randrange(230, screen_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(50, screen_height - snake_block) / 10.0) * 10.0
        if [foodx, foody] not in snake_List:
            return foodx, foody

def gameLoop():
    global snake_speed
    game_over = False
    game_close = False

    x1 = screen_width // 2
    y1 = screen_height // 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx, foody = generate_food(snake_List)

    score = 0
    level = 1
    food_eaten = 0

    while not game_over:

        while game_close:
            screen.fill(black)
            message("You Lost! Press C to Play Again", red)
            Your_score(score)
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        game_over = True
                        game_close = False
                    elif event.type == pg.QUIT:
                        game_over = True
                        game_close = False
                    if event.key == pg.K_c:
                        gameLoop()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pg.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pg.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pg.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check for border collision
        if x1 >= screen_width:
            x1 = 0
        elif x1 < 0:
            x1 = screen_width - snake_block
        elif y1 >= screen_height:
            y1 = 0
        elif y1 < 0:
            y1 = screen_height - snake_block

        x1 += x1_change
        y1 += y1_change
        screen.fill(black)
        pg.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pg.display.update()

        if x1 == foodx and y1 == foody:
            foodx, foody = generate_food(snake_List)
            Length_of_snake += 1
            score += 1
            food_eaten += 1
            if food_eaten >= 3:  # Increase level every 3 foods eaten
                level += 1
                food_eaten = 0
                snake_speed += 2  # Increase speed when level up

        clock.tick(snake_speed)

    pg.quit()
    quit()

gameLoop()