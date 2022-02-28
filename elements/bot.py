from elements.entity import Entity


class Bot(Entity):
    """
    An item of cultural or historical interest. 
    
    Attributes:
        _id (number): An identifier for the bot
        _message (string): A short description about the bot.
        _type (number): To recognize the characteristic of the bot
        _score (number): what is the alue of the bot.
    """
    def __init__(self):
        super().__init__()
        self._id = 0
        self._message = ""
        self._type = 0
        self._score = 0
        
    def get_id(self):
        """Gets the bot's id.
        
        Returns:
            number: The id.
        """
        return self._id
    
    def set_id(self, id):
        """Updates the id to the given one.
        
        Args:
            id (number): The given id.
        """
        self._id = id
    
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
    
    def get_type(self):
        """Gets the bot's type.
        
        Returns:
            number: The type.
        """
        return self._type
    
    def set_type(self, type):
        """Updates the type to the given one.
        
        Args:
            type (number): The given type.
        """
        self._type = type
        
    def get_score(self):
        """Gets the bot's score.
        
        Returns:
            number: The score.
        """
        return self._score
    
    def set_score(self, score):
        """Updates the score to the given one.
        
        Args:
            score (number): The given score.
        """
        self._score = score