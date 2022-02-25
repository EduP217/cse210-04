import random

from services.keyboard_service import KeyboardService
from services.video_service import VideoService

from elements.collection import Collection
from elements.entity import Entity
from elements.bot import Bot

from utils.point import Point
from utils.color import Color

from screen import Screen

CAPTION = "Rock & Gems Scanner"
MAX_X = 800
MAX_Y = 600
CELL_SIZE = 20
FRAME_RATE = 15
WHITE = Color(255, 255, 255)
BOTS_IN_SCREEN = 50
GRID_COLS = 35
GRID_ROWS = 30

BOTS_TEXT = ["*", "o"]
BOTS_MESSAGE = ["You found a gem !!", "You found a rock !!"]

def main():
    
    """ Gather all the elements of the game """
    screen_collection = Collection()
    
    """ Initialize the score entity to be setted in the board """
    score_position = Point(5, 5)
    score = Entity()
    score.set_entity("", CELL_SIZE, WHITE, score_position)
    
    """ Setting the score into the board """
    screen_collection.add_entity("banners", score)
    
    """ Initialize the score entity to be setted in the board """
    banner_position = Point(5, (MAX_Y - CELL_SIZE) - 5)
    banner = Entity()
    banner.set_entity("", CELL_SIZE, WHITE, banner_position)
    
    """ Setting the banner into the board """
    screen_collection.add_entity("banners", banner)
    
    for n in range(BOTS_IN_SCREEN):
        bot_random_selected = random.randint(0, 1)
        
        text = BOTS_TEXT[bot_random_selected]
        message = BOTS_MESSAGE[bot_random_selected]

        x = random.randint(1, GRID_COLS - 1)
        y = random.randint(1, GRID_ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        """ Setting the bot into the board """
        bot = Bot()
        bot.set_entity(text, CELL_SIZE, color, position)
        bot.set_message(message)
        screen_collection.add_entity("bots", bot)
    
    """ Initialize the player entity to be setted in the board """
    player_position = Point(int(MAX_X/2), int(MAX_X/2))
    player = Entity()
    player.set_entity("P", CELL_SIZE, WHITE, player_position)
    
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