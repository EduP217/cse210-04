import os
import random

from services.keyboard_service import KeyboardService
from services.video_service import VideoService

from elements.collection import Collection
from elements.entity import Entity

from utils.point import Point
from utils.color import Color

from screen import Screen

CAPTION = "Rock & Gems Scanner"
MAX_X = 800
MAX_Y = 600
CELL_SIZE = 30
FRAME_RATE = 12
WHITE = Color(255, 255, 255)

def main():
    
    """ Gather all the elements of the game """
    screen_collection = Collection()
    
    """ Initialize the score entity to be setted in the board """
    score_position = Point(5, 5)    
    score = Entity()
    score.set_entity("", CELL_SIZE, WHITE, score_position)
    
    """ Setting the score into the board """
    screen_collection.add_entity("score", score)
    
    """ Initialize the player entity to be setted in the board """
    player_position = Point(int(MAX_X/2), int(MAX_X/2))
    player = Entity()
    player.set_entity("º-º", CELL_SIZE, WHITE, player_position)
    
    """ Setting the player into the board """
    screen_collection.add_entity("player", player)
    
    """ Initialize the services functionality """
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    
    """ INitialize the screen board and start the game"""
    screen = Screen(keyboard_service, video_service)
    screen.start_game(screen_collection)

if __name__ == "__main__":
    main()