from gameobjects import Game, PlayerObject, ComputerPlayer, Player, HumanPlayer


class CLInterface:

    def __init__(self):
        self.game = Game()
        self.computerplayer = ComputerPlayer()
        self.humanplayer = HumanPlayer()

    def set_up(self):
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

    def run_game(self):
        while not self.game.is_finished():
            self.get_choices()
            print(self.game.report_round())
            print(self.game.report_score())
        print(self.game.report_winner())

    def run_sequence(self):
        hi = False
        while not hi:
            self.set_up()
            self.run_game()
            quit = input('Play again? (y/n)')
            if quit.lower()[0] == 'n':
                hi = True


if __name__ == '__main__':
    CLI = CLInterface()
    CLI.run_sequence()



