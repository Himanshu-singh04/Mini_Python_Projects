import pygame
import random

white = (255 , 255 , 255)
red = (255 , 0 , 0)
black = (0 , 0 , 0)
blue = (0, 255, 0)

pygame.init()
screen_width = 600
screen_height = 600

gameWindow = pygame.display.set_mode((screen_height,screen_width))
pygame.display.set_caption("Snakes")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 45)

# pygame.display.update()

def screen_display(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def gameloop():

    game_over = False
    exit_game = False
    snake_x = 125
    snake_y = 125
    velocity_x = 0
    velocity_y = 0
    snake_list = []
    snake_length = 1
    # snake_size_const = 20
    # snake_size_var = 20
    food_x = random.randint(0, screen_width)
    food_y = random.randint(0, screen_height)
    score = 0
    init_velocity = 8
    # food_size = 20
    snake_size = 20
    fps = 30

    with open("Python codes\\project\\Project6\\hiscore.txt", "r") as f :
        hiscore = f.read()

    while not exit_game:
        if (game_over == True):
            with open("Python codes\\project\\Project6\\hiscore.txt", "w") as f :
                f.write(str(hiscore))
            gameWindow.fill(white)
            screen_display("GameOver press enter to playagain",red, 45, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        # snake_x = snake_x + 5
                        velocity_x = init_velocity
                        velocity_y = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        # snake_x = snake_x - 5
                        velocity_x = -init_velocity
                        velocity_y = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        # snake_y = snake_y - 5
                        velocity_y = -init_velocity
                        velocity_x = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        # snake_y = snake_y + 5
                        velocity_y = init_velocity
                        velocity_x = 0
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        velocity_x = 0
                        velocity_y = 0

            snake_x = snake_x + velocity_x 
            snake_y = snake_y + velocity_y

            if abs(food_x - snake_x) < 10 and abs(food_y - snake_y) < 10 :
                score +=1
                # snake_size_var = snake_size_var + 5
                # print(score)

                food_x = random.randint(0, screen_width)
                food_y = random.randint(0, screen_height)
                snake_length += 5

                if score > int(hiscore):
                    hiscore = score

            gameWindow.fill(white)
            screen_display("SCORE:"+str(score) + "hiscore" + str(hiscore), blue, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True

            if (snake_x < 0) or (snake_x > screen_width) or (snake_y < 0) or (snake_y > screen_height):
                game_over = True
            plot_snake(gameWindow, black, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
gameloop()