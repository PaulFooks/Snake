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
# image size
image_size = 40

# declare background images
# splash screen
splash_image = pygame.image.load("images/splash.png")




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
grid_size = 20

# declare clock as pygame object
clock = pygame.time.Clock()

# declare the window dimensions
window_width = 800
window_height = 600

# create a game_display variable and add the pygame window to it
game_display = pygame.display.set_mode((window_width, window_height))

# change the window title
pygame.display.set_caption('Snake Game v0.06')



'''
levels set
'''




# starting position of snake [0,1], angle of snake[2], initial length of snake[3], FPS of game[4] max length of snake[5] all set in level
grid_start =\
            [[100, 100, -90, 0, 2, 10],[100, 100, 0, 1, 15, 10]]

# set starting level = 0
level = 0

# declare frames per second
FPS = grid_start[level][4] # please note this is set on each level also




'''
initial screen to display
'''
# set splash_screen = True for release
splash_screen = True

# set game_running = False for release
game_running = False


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



    # add image to background
    splash_image = pygame.transform.scale(splash_image, (window_width, window_height))
    game_display.blit(splash_image, (0, 0))

    pygame.display.update()








    '''
    game
    '''
    # update contents window
    pygame.display.update()

    # Setup the game to run at 15 frames per second
    clock.tick(FPS)



'''
tidy up game_display
'''


pygame.display.update()
# time.sleep(2)

# Uninitialise PyGame
pygame.quit()
quit()
