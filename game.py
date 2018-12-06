# Reading School 2018, Snake Game by Student Name, Year 8

# import the pygame library and a random number generator
import pygame, random

# import time for wait state
import time

# initialize pygame
pygame.init()

'''
colour setup
'''
# declare colours - (r,g,b)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,200,0)

'''
images setup
'''
# sizes
pos_increment = 10
body_size = 40

# declare background images
# splash screen
splash_image = pygame.image.load("images/splash.png")
# background screen
background_image = pygame.image.load("images/back.png")

# declare snake images
head_image = pygame.image.load("images/head.png")
body_image = pygame.image.load("images/body.png")
body_image_01 = pygame.image.load("images/body_bend_01.png")
body_image_02 = pygame.image.load("images/body_bend_02.png")
body_short = pygame.image.load("images/body_short.png")

twist_image = pygame.image.load("images/twist.png")
tail_image = pygame.image.load("images/tail.png")
short_tail_image = pygame.image.load("images/short_tail.png")

# Add an image (snake head) to the game + apple
apple_image = pygame.image.load('images/apple.png')


'''
audio setup
'''
# declare music
pygame.mixer.music.load("audio/music.mp3")
# set -1 for indefinite repeat
# uncomment next line on release
# pygame.mixer.music.play(-1)



'''
game setup
'''
# size of grid for snake movement
grid_size = 40
counter = 0
paused = False

# declare clock as pygame object
clock = pygame.time.Clock()

# declare the window dimensions
window_width = 1200
window_height = 800

# create a game_display variable and add the pygame window to it
game_display = pygame.display.set_mode((window_width, window_height))

# change the window title
pygame.display.set_caption('Snake Game v0.8')
# Snake Game v0.8 introduced Git support



'''
levels set
'''




# starting position of snake [0,1], angle of snake[2], initial length of snake[3], FPS of game[4] max length of snake[5] all set in level
grid_start =\
            [[120, 120, -90, 20, 6, 20],[100, 100, 0, 1, 15, 10]]

# set starting level = 0
level = 0

# declare frames per second
FPS = grid_start[level][4] # please note this is set on each level also



'''
initial screen to display
'''
# set splash_screen = True for release
splash_screen = False

# set game_running = False for release
game_running = True
# used in setup of snake
game_init = False


'''
snake setup
'''
head_size = grid_size  # Size of the snake head to match grid size
head_x = grid_start[level][0]    # Horizontal snake start position
head_y = grid_start[level][1]   # Vertical snake start position
head_angle = grid_start[level][2]  # Start angle of head

head_x_change = 0   # Constant horizontal movement control
head_y_change = 0   # Constant vertical movement control

# level length of snake
snake_length = grid_start[level][3]

snake_x_y_a = [0] * (1 + snake_length + 1) # add head and tail
#snake_x_y_a = grid_start[level]  # set the list for snake position to being the current level



'''
splash_screen loop
'''
# splash screen
while splash_screen:

    # looking for pygame events
    for event in pygame.event.get():

        # check if close button on window clicked
        if event.type == pygame.QUIT:
            #move out of while game_running
            splash_screen = False

    # check if keyboard enter key or return key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                splash_screen = False
                game_running = True

        # check if mouse clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            splash_screen = False
            game_running = True


    # add image to background
    splash_image = pygame.transform.scale(splash_image, (window_width, window_height))
    game_display.blit(splash_image, (0, 0))
    pygame.display.update()





'''
snake
'''
# calculate body part
def body_calc(i, x, y, angle, image):

    new_body_pos = i * body_size

    if angle == 0:
        calc = [x + new_body_pos,y , angle, image]
    elif angle == 90:
        calc = [x,y - new_body_pos, angle, image]
    elif angle == -90:
        calc = [x,y + new_body_pos, angle, image]
    elif angle == 180:
        calc = [x - new_body_pos,y ,angle, image]
    return calc


# draw snake
def draw_snake(x_y, angle):

    # set counter as global variable
    global counter

    if snake_x_y_a[2] == 0:
        print("start", snake_x_y_a)

        snake_x_y_a[0] = body_calc(0, x_y[0], x_y[1], angle, head_image) # head

        for i in range(1, snake_length + 1):
            snake_x_y_a[i] = body_calc(i, x_y[0], x_y[1], angle, body_image) # body

        snake_x_y_a[snake_length + 1] = body_calc(snake_length + 1, x_y[0], x_y[1], angle, tail_image) # tail

    elif game_init:

        # insert t 0 index
        snake_x_y_a.insert(0, body_calc(0, x_y[0], x_y[1], angle, head_image)) # head

        # remove from end of array
        snake_x_y_a.pop()

    # print(snake_x_y_a)

    # draw the snake from contents of snake_x_y_a array
    for idx, x_y_a in enumerate(snake_x_y_a):

        if idx == 0:

            image_rotation = pygame.transform.rotate(x_y_a[3], angle)
            game_display.blit(image_rotation, [x_y_a[0], x_y_a[1]])

        elif idx > 0 and idx < len(snake_x_y_a) -1:

            if idx%2 == 0:
                if counter%2 == 0 and game_init:
                    body_part = body_image_01
                else:
                    body_part = body_image_02
            else:
                if counter%2 == 0 and game_init:
                    body_part = body_image_02
                else:
                    body_part = body_image_01

            # set counter
            counter += 1

            if snake_x_y_a[idx - 1][2] == x_y_a[2]:
                image_rotation = pygame.transform.rotate(body_part, x_y_a[2])
            else:

                # set corner piece
                if x_y_a[2] == -90 and snake_x_y_a[idx - 1][2] == 180:
                    calc = 0
                elif x_y_a[2] == 180 and snake_x_y_a[idx - 1][2] == 90:
                    calc = -90
                elif x_y_a[2] == 90 and snake_x_y_a[idx - 1][2] == 0:
                    calc = -180
                elif x_y_a[2] == 0 and snake_x_y_a[idx - 1][2] == -90:
                    calc = 90
                elif x_y_a[2] == 90 and snake_x_y_a[idx - 1][2] == 180:
                    calc = 90
                elif x_y_a[2] == 180 and snake_x_y_a[idx - 1][2] == -90:
                    calc = -180
                elif x_y_a[2] == -90 and snake_x_y_a[idx - 1][2] == 0:
                    calc = -90
                elif x_y_a[2] == 0 and snake_x_y_a[idx - 1][2] == 90:
                    calc = 0
                elif x_y_a[2] == 0 and snake_x_y_a[idx - 1][2] == 180:
                    calc = 180

                image_rotation = pygame.transform.rotate(twist_image, calc)

            game_display.blit(image_rotation, [x_y_a[0], x_y_a[1]])

        elif idx == len(snake_x_y_a) -1:
            if snake_x_y_a[idx - 1][2] == x_y_a[2]:
                # rotate to same value
                image_rotation = pygame.transform.rotate(tail_image, x_y_a[2])
            else:
                # rotate to previous piece body piece
                image_rotation = pygame.transform.rotate(tail_image, snake_x_y_a[idx - 1][2])

            # set the tail piece
            game_display.blit(image_rotation, [x_y_a[0], x_y_a[1]])
'''
end snake
'''






'''
apple
'''
# draw apple
def draw_apple():

    offset = grid_size * 3

    randAppleX = round(random.randrange(offset, window_width - offset) / grid_size) * grid_size
    randAppleY = round(random.randrange(offset, window_height - offset) / grid_size) * grid_size
    # print
    return [randAppleX, randAppleY]

apple_position = draw_apple()


'''
end apple
'''







'''
game_running loop. This is where the logic of game is found with snake move input from keyboard and drawing of background and snake
'''
while game_running:

    # looking for pygame events
    for event in pygame.event.get():

        # print(event)

        # check if close button on window clicked
        if event.type == pygame.QUIT:
            #move out of while game_running
            game_running = False


        # Look Key event
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_p:
                paused = not paused
                game_init = not game_init
                print(paused)


            if event.key == pygame.K_LEFT and paused == False:
                # following stops snake eating itself
                if snake_length > 0 and head_angle == 180:
                    print("left refused")
                else:
                    head_x_change = -grid_size
                    head_y_change = 0
                    head_angle = 0
                game_init = True

            elif event.key == pygame.K_RIGHT and paused == False:
                if snake_length > 0 and head_angle == 0:
                    print("right refused")
                else:
                    head_x_change = grid_size
                    head_y_change = 0
                    head_angle = 180
                game_init = True

            elif event.key == pygame.K_UP and paused == False:
                if snake_length > 0 and head_angle == 90:
                    print("up refused")
                else:
                    head_x_change = 0
                    head_y_change = -grid_size
                    head_angle = -90
                game_init = True

            elif event.key == pygame.K_DOWN and paused == False:
                if snake_length > 0 and head_angle == -90:
                    print("down refused")
                else:
                    head_x_change = 0
                    head_y_change = grid_size
                    head_angle = 90
                game_init = True

    # Set the constant direction
    if not paused:
        head_x += head_x_change
        head_y += head_y_change
    else:
        game_init = False


    # Example 2: check for snake inside display window
    if head_x >= window_width or head_x <= 0 - head_size:
        game_running = False
    elif head_y >= window_height or head_y <= 0 - head_size:
        game_running = False

    '''
    background
    '''
    # set the background colour to over write the previous position of the snake head. Not necessary as using image below
    # game_display.fill(WHITE)

    # draw background
    background_image = pygame.transform.scale(background_image, (window_width, window_height))
    game_display.blit(background_image, (0, 0))


    '''
    snake
    '''
    draw_snake([head_x, head_y], head_angle)



    '''
    apple
    '''
    game_display.blit(apple_image, (apple_position[0], apple_position[1]))



    '''
    check for collisions
    '''
    if head_x == apple_position[0] and head_y == apple_position[1]:
        # add to snake length by appending
        snake_x_y_a.append(0)

        if snake_length == grid_start[level][5]:
            # game_running = False
            print("next level")

        # redraw the apple
        apple_position = draw_apple()

    else:

        # check for collision with snake
        for idx, x_y_a in enumerate(snake_x_y_a):
            # checks if idx > 0 which is the head
            if idx > 0 and head_x == x_y_a[0] and head_y == x_y_a[1]:

                paused = True
                time.sleep(2)
                paused = False
                # game_running = False


    '''
    game
    '''
    # update contents window
    # game_display.fill(RED)
    pygame.display.update()

    # Setup the game to run at 15 frames per second
    clock.tick(FPS)




# if game_running = False move out of while game_running:

'''
tidy up game_display
'''
print('tidy up game display and quit/credits sequence')

game_display.fill(WHITE)
pygame.display.update()

# time.sleep(2)# comment this line out to speed up quit

# Uninitialise PyGame
pygame.quit()
quit()
