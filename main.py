from character import DungeonMaster, Player
from gamemap import gamemap


def menu(options):
    """Waits for an option to be picked

    Args:
        options (list[string]): A list of options

    Returns:
        string: The option selected by the user
    """
    while True:
        entered = input("> ").lower().strip()
        if entered in options:
            return entered
        print("Invalid input! Try again")


def quiz(riddle, answer):
    """Asks a question and returns true if the user answered correctly

    Args:
        riddle (string): The question
        answer (string): The answer

    Returns:
        boolean: True if user answered correctly, false if not
    """
    print(riddle)
    return answer in input("> ").lower().strip()


class Game:
    def __init__(self, gamemap):
        """Creates the game

        Args:
            gamemap (GameMap): The map
        """
        self.gamemap = gamemap
        self.master = DungeonMaster("Edward")
        self.player=  Player("Joe")
        self.position = 0

    def start(self):
        """Start the continuous gameplay"""
        while True:
            print("Dungeon Escape")
            print("You are trapped in a dungeon where you'll")
            print("need to answer riddles to escape.")
            print(self.master)
            print(self.player)
            print()
            print("1. Start")
            print("2. Quit")
            option = menu(["1", "2", "start", "quit"])
            if option in ["quit", "2"]:
                return
            for i, question in enumerate(self.gamemap.gamemap):
                self.gamemap.display(i)
                if not quiz(self.master.say(question.riddle), question.answer):
                    break
                print("That's Correct!\n")
            else:
                print("You escaped the dungeon!\n")
                continue
            print("Incorrect! You couldn't escape the dungeon!\n")


Game(gamemap).start()
