from screen.entity import Entity


class Bot(Entity):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an bot is to provide a message about itself.

    Attributes:
        _message (string): A short description about the bot.
    """
    def __init__(self):
        super().__init__()
        self._message = ""
        
    def get_message(self):
        """Gets the bot's message.
        
        Returns:
            string: The message.
        """
        return self._message
    
    def set_message(self, message):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._message = message