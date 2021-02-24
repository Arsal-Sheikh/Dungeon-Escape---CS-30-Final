class Character:
    def __init__(self, name):
        """Creates a character

        Args:
            name (string): The character's name
        """
        self.name = name


class DungeonMaster(Character):
    def __init__(self, name):
        """Create a dungeon master

        Args:
            name (string): The dungeon master's name
        """
        super().__init__(name)

    def __str__(self):
        """Get a description of the dungeon master

        Returns:
            string: Description of the dungeon master
        """
        return f"The dungeon master's name is {self.name}"

    def say(self, message):
        """Make the dungeon master say a message

        Args:
            message (string): The message to be spoken

        Returns:
            string: The words of the dungeon master
        """
        return f"{self.name} says: {message}"


class Player(Character):
    def __init__(self, name):
        """Creates a player

        Args:
            name (string): The name of the player
        """
        super().__init__(name)

    def __str__(self):
        """Get a description of the player

        Returns:
            string: Description of the player
        """
        return f"Your name is {self.name}"
