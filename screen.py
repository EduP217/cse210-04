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
        
    def start_game(self, collection : Collection):
        """Starts the game using the given collection. Runs the main game loop.

        Args:
            collection (collection): The collection of entities.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(collection)
            self._do_updates(collection)
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

    def _do_updates(self, collection : Collection):
        """Updates the player's position and resolves any collisions with bots.
        
        Args:
            collection (collection): The collection of entities.
        """
        score = collection.get_first_entity("score")
        player = collection.get_first_entity("player")
        bots = collection.get_entities("bots")

        score.set_text("SCORE : %")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)
        
        # for bot in bots:
        #     if player.get_position().equals(bot.get_position()):
        #         message = bot.get_message()
        #         score.set_text(message)
        
    def _do_outputs(self, collection : Collection):
        """Draws the entities on the screen.
        
        Args:
            collection (collection): The collection of entities.
        """
        self._video_service.clear_buffer()
        entities = collection.get_all_entities()
        self._video_service.draw_entities(entities)
        self._video_service.flush_buffer()