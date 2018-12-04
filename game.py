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

#



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



# create a game_display variable and add the pygame window to it
game_display = pygame.display.set_mode((window_width, window_height))

# change the window title
pygame.display.set_caption('Snake Game v0.06')
