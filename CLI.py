from gameobjects import Game, PlayerObject, ComputerPlayer, Player, HumanPlayer


class CLInterface:

    def __init__(self):
        self.game = Game()
        self.computerplayer = ComputerPlayer()
        self.humanplayer = HumanPlayer()

    def players(self):
        print('Hello and welcome to rock paper scissors lizard spock')
        playerone = input('Will player one be a computer (c) or human(h)')
        if playerone.lower()[0] == 'h':
            player_one_name = str(input('What will their name be'))
            self.game.add_human_player(player_one_name)
        if playerone.lower()[0] == 'c':
            self.game.add_computer_player()
        playertwo = input('Will player one be a computer (c) or human(h)')
        if playertwo.lower()[0] == 'h':
            player_two_name = str(input('What will their name be'))
            self.game.add_human_player(player_two_name)
        if playertwo.lower()[0] == 'c':
            self.game.add_computer_player()
        self.input_max_rounds()

    def input_max_rounds(self):
        num_rounds = input('How many rounds would you like to play')
        self.game.set_max_rounds(num_rounds)

    def get_choices(self):
        choice = input('Please choose your object')
        self.computerplayer.choose_object()
        self.humanplayer.choose_object(choice)







