from elements.entity import Entity


class Player(Entity):
    """
    An item of cultural or historical interest.

    Attributes:
        _score (string): the punctuation of the player
    """
    def __init__(self):
        super().__init__()
        self._score = 0
        
    def get_score(self):
        """Gets the player's score.
        
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