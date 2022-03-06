from elements.collection import Collection
from services.keyboard_service import KeyboardService
from services.video_service import VideoService

class Screen:
    """A person who directs the game. 
    
    The responsibility of a Screen is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service : KeyboardService, video_service : VideoService):
        """Constructs a new Screen using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._banner_timer = 0
        
    def start_game(self, collection : Collection, element_size):
        """Starts the game using the given collection. Runs the main game loop.

        Args:
            collection (collection): The collection of entities.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(collection)
            self._do_updates(collection, element_size)
            self._do_outputs(collection)
        self._video_service.close_window()

    def _get_inputs(self, collection : Collection):
        """Gets directional input from the keyboard and applies it to the player.
        
        Args:
            collection (collection): The collection of entities.
        """
        player = collection.get_first_entity("player")
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)

    def _do_updates(self, collection : Collection, element_size):
        """Updates the player's position and resolves any collisions with bots.
        
        Args:
            collection (collection): The collection of entities.
        """
        score = collection.get_first_entity("banners")
        banner = collection.get_entity("banners", 1)
        player = collection.get_first_entity("player")
        bots = collection.get_entities("bots")

        self._banner_timer += 1
        if self._banner_timer >= 75:
            banner.set_text("")
            self._banner_timer = 0
            
        score.set_text(f"SCORE : {player.get_score()}")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)
        
        for bot in bots:
            bot.set_falling(True)
            if bot.get_falling():
                #print(self._video_service.get_height())
                #print(bot.get_position().get_y())
                bot_y_position = bot.get_position().get_y()
                max_falling = max_y - element_size
                
                if bot_y_position <=  max_falling:
                    bot_y_position = bot_y_position + bot.get_velocity()
                    bot.get_position().set_y(bot_y_position)
                    if bot_y_position ==  max_falling:
                        bot.get_position().set_y(0)
            
            if player.get_position().equals(bot.get_position()):
                self._banner_timer = 0
                message = bot.get_message()
                bot_score = bot.get_score()
                player_score = player.get_score()
                if bot.get_type() == 0:
                    message += f" +{bot_score}pts"
                    player_score += bot_score
                else:
                    message += f" -{bot_score}pts"
                    player_score -= bot_score
                
                bot.get_position().set_y(800)
                player.set_score(player_score)
                banner.set_text(message)
                #collection.remove_entity("bots", bot)
        
    def _do_outputs(self, collection : Collection):
        """Draws the entities on the screen.
        
        Args:
            collection (collection): The collection of entities.
        """
        self._video_service.clear_buffer()
        entities = collection.get_all_entities()
        self._video_service.draw_entities(entities)
        self._video_service.flush_buffer()