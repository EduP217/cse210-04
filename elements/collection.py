from elements.entity import Entity

class Collection:
    """A collection of entities.

    Attributes:
        _entities (dict): A dictionary of entities { key: group_name, value: a list of entities }
    """

    def __init__(self):
        """Constructs a new entity."""
        self._entities = {}
        
    def add_entity(self, group, entity):
        """Adds an entity to the given group.
        
        Args:
            group (string): The name of the group.
            entity (entity): The entity to add.
        """
        if not group in self._entities.keys():
            self._entities[group] = []
            
        if not entity in self._entities[group]:
            self._entities[group].append(entity)

    def get_entities(self, group):
        """Gets the entities in the given group.
        
        Args:
            group (string): The name of the group.

        Returns:
            List: The entities in the group.
        """
        results = []
        if group in self._entities.keys():
            results = self._entities[group].copy()
        return results
    
    def get_all_entities(self):
        """Gets all of the entities in the collection.
        
        Returns:
            List: All of the entities in the collection.
        """
        results = []
        for group in self._entities:
            print(group)
            results.extend(self._entities[group])
        return results

    def get_first_entity(self, group) -> Entity:
        """Gets the first entity in the given group.
        
        Args:
            group (string): The name of the group.
            
        Returns:
            List: The first entity in the group.
        """
        result = None
        if group in self._entities.keys():
            result = self._entities[group][0]
        return result

    def remove_entity(self, group, entity):
        """Removes an entity from the given group.
        
        Args:
            group (string): The name of the group.
            entity (entity): The entity to remove.
        """
        if group in self._entities:
            self._entities[group].remove(entity)