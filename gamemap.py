class Dungeon:
    def __init__(self, name, riddle, answer):
        """Creates a dungeon

        Args:
            name (string): The name of the dungeon
            riddle (string): The riddle to solve the dungeon
            answer (string): The answer to the riddle
        """
        self.name = name
        self.riddle = riddle
        self.answer = answer

    def __str__(self):
        """Returns the name of the dungeon

        Returns:
            string: The name of the dungeon
        """
        return self.name

    def __len__(self):
        """Returns the length of the name of the dungeon

        Returns:
            int: Length of the dungeon name
        """
        return len(self.name)


class GameMap:
    def __init__(self, gamemap):
        """Creates a gamemap

        Args:
            gamemap (list[Dungeon]): A list of the dungeons in order
        """
        self.gamemap = gamemap

    def display(self, position):
        """Prints the dungeons out

        Args:
            position (int): The dungeon the player is in
        """
        size = max(map(len, self.gamemap))

        print(f"|{'-'*(size+2)}|")
        print(f"| {'Start'.ljust(size)} |")

        for i, line in enumerate(self.gamemap):
            if i == position:
                print(f"|{'='*(size+2)}|")
                print(f"| {str(line).ljust(size)} |")
                print(f"|{'='*(size+2)}|")
            else:
                print(f"| {str(line).ljust(size)} |")

        print(f"| {'Finish'.ljust(size)} |")
        print(f"|{'-'*(size+2)}|")


gamemap = GameMap(
    [
        Dungeon(
            "Dungeon 1",
            "What has to be broken before you can use it? (Hint: It's food)",
            "egg",
        ),
        Dungeon(
            "Dungeon 2",
            "I’m tall when I’m young, and I’m short when I’m old. What am I?",
            "candle",
        ),
        Dungeon(
            "Dungeon 3",
            "What month of the year has 28 days?",
            "all",
        ),
        Dungeon(
            "Dungeon 4",
            "What is full of holes but still holds water?",
            "sponge",
        ),
        Dungeon(
            "Dungeon 5",
            "What question can you never answer yes to?",
            "asleep",
        ),
        Dungeon(
            "Dungeon 6",
            "What is always in front of you but can’t be seen?",
            "future",
        ),
        Dungeon(
            "Dungeon 7",
            "What can you break, even if you never pick it up or touch it?",
            "promise",
        ),
    ]
)
