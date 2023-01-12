import tkinter as tk
from gameobjects import Game, PlayerObject, RPS_OBJECTS, RPS_WIN_DICT
from PIL import ImageTk, Image
#Creating images to place on buttons with PIL
rock = PhotoImage(file = "C:\Users\danie\OneDrive\Documents\School\CODING\the-rock-eyebrow-dwayne-johnson.avif")
mark = PhotoImage(file = "C:\Users\danie\OneDrive\Documents\School\CODING\Mark_Zuckerberg_F8_2019_Keynote_(32830578717)_(cropped).jpg")
scissors = PhotoImage(file = "C:\Users\danie\OneDrive\Documents\School\CODING\scissors.jpg")
paper = PhotoImage(file = "C:\Users\danie\OneDrive\Documents\School\CODING\61qSdyDYbZL._SL1185_.jpg")
spock = PhotoImage(file = "C:\Users\danie\OneDrive\Documents\School\CODING\spock.jpg")
rockimage = rock.subsample(1, 2)
markimage = mark.subsample(1,2)
scissorsimage = scissors.subsample(1,2)
paperimage = paper.subsample(1,2)
spockimage = spock.subsample(1,2)


class GameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.game = create_game()
        title_string = 'Rock Paper Scissors Lizard Spock'

        self.title(title_string)
        title_label = tk.Label(self,
                               text=title_string,
                               bg="green", fg="blue",
                               width=40,
                               font=("Arial", 20))
        title_label.pack(side=tk.TOP)

        self.frames = {
            "game_options": Starting(self),
            "main_game": Gamer(self)}

        self.show_frame("game_options")

    def show_frame(self, current_frame):
        widgets = self.winfo_children()
        for w in widgets:
            if w.winfo_class() == "Frame":
                w.pack_forget()

        frame_to_show = self.frames[current_frame]
        frame_to_show.pack(expand=True, fill=tk.BOTH)
        frame_to_show.set_up()


class Starting(tk.Frame):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.game = controller.game
        self.player = self.game.player

        self.user_name = tk.StringVar()
        self.num_rounds = tk.IntVar()

        name_label = tk.Label(self, text="Player Name:")
        rounds_label = tk.Label(self, text="Number of Rounds:")

        vcmd = (self.register(self.validate_entry), '%P')
        self.name_edit = tk.Entry(self, textvariable=self.user_name,
                                  name='editbox',
                                  validate='key',
                                  validatecommand=vcmd,
                                  justify=tk.CENTER, width=15)
        rounds = tk.Spinbox(self, textvariable=self.num_rounds,
                                state='readonly',
                                from_=1, to=100, justify=tk.CENTER, width=20)
        self.start_button = tk.Button(self, text="Start game",
                                      state=tk.DISABLED,
                                      command=self.start_game,
                                      width=15)

        name_label.grid(row=1, column=7, pady=5)
        rounds_label.grid(row=2, column=7, pady=5)
        self.name_edit.grid(row=1, column=8, pady=5)
        rounds.grid(row=2, column=8, pady=5)
        self.start_button.grid(row=5, column=8, pady=(5, 10))

    def set_up(self):
        if self.game.players:
            self.user_name.set(self.player.name)
        if self.game.max_rounds:
            self.num_rounds.set(self.game.max_rounds)

    def start_game(self):
        self.game.set_max_rounds(self.num_rounds.get())
        self.controller.show_frame("main_game")

    def validate_entry(self, user_name):
        if (0 < len(user_name) < 13) and user_name.isalpha():
            self.start_button.config(state=tk.NORMAL)
            self.player.set_name(user_name)
        elif len(user_name) == 0:
            self.start_button.config(state=tk.DISABLED)
        else:
            return False
        return True


class Gamer(tk.Frame):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller
        self.game = controller.game

        self.report_message = tk.StringVar()
        self.results_message = tk.StringVar()

        self.outcome = tk.Label(self, textvariable=self.report_message, bg="red", fg="white", width=35)

        self.rockbutton = tk.Button(self, image=rockimage)
        self.markbutton = tk.Button(self, image=markimage)
        self.paperbutton = tk.Button(self, image=paperimage)
        self.spockbutton = tk.Button(self, image=spockimage)
        self.scissorsbutton = tk.Button(self, image=scissorsimage)

        self.quit_button = tk.Button(self, text="Quit", width=15, command=self.controller.destroy, bg='red', fg='blue')
        self.options_button = tk.Button(self, text="Change Options (O)", width=15, command=self.reset_game, bg='red', fg='blue')
        self.results = tk.Label(self, textvariable=self.results_message, height=2, bg='green', fg='orange')

        self.rockbutton.grid(row=3, column=1)
        self.markbutton.grid(row=4, column=1)
        self.paperbutton.grid(row=5, column=1)
        self.spockbutton.grid(row=6, column=1)
        self.scissorsbutton.grid(row=7, column=1)
        self.outcome.grid(row=1, column=1, rowspan=3)
        self.results.grid(row=2, column=0, columnspan=2, pady=5)
        self.quit_button.grid(row=3, column=0, pady=(5, 10), rowspan=2)
        self.options_button.grid(row=4, column=1, pady=(5, 10))

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)


    def set_up(self):
        self.report_message.set('Make a move to begin')
        self.results_message.set(
            f"Welcome {self.game.players[0].name}. there are {self.game.max_rounds} left")


    def select_object(self, item):
        self.game.next_round()
        self.game.players[0].choose_object(item)
        self.game.players[1].choose_object()
        self.game.find_winner()
        self.show_report()

    def show_report(self):
        if self.game.current_round == 0:
            self.set_up()
        else:
            self.report_message.set(self.game.report_round())
            result_msg = self.game.report_score()
            result_msg = result_msg.replace("\n", " ")

            if self.game.is_finished():
                result_msg += "\n" + self.game.report_winner()
                self.rockbutton.config(state=tk.DISABLED)
                self.markbutton.config(state=tk.DISABLED)
                self.paperbutton.config(state=tk.DISABLED)
                self.spockbutton.config(state=tk.DISABLED)
                self.scissorsbutton.config(state=tk.DISABLED)
            else:
                result_msg += f"\nYou have {self.game.max_rounds - self.game.current_round} rounds left to play"

            self.results_message.set(result_msg)

    def restart_game(self):
        self.game.reset()
        self.show_report()
        self.rockbutton.config(state=tk.NORMAL)
        self.markbutton.config(state=tk.NORMAL)
        self.spockbutton.config(state=tk.NORMAL)
        self.paperbutton.config(state=tk.NORMAL)
        self.scissorsbutton.config(state=tk.NORMAL)

    def reset_game(self):
        self.restart_game()
        self.controller.show_frame("game_options")


def create_game():
    game = Game()
    game.player = game.add_human_player()
    game.add_computer_player()
    return game


if __name__ == "__main__":
    app = GameApp()
    app.mainloop()