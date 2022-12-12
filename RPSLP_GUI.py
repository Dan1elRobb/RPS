import tkinter as tk
from gameobjects import Game, PlayerObject


class OpeningFrame(tk.Frame):

    def __init__(self):
        super().__init__()
        title = 'Welcome to Rock Paper Scissors Lizard Spock'

        t_label = tk.Label(self, text=title, width=40, font=('Arial',20))
        t_label.grid(row=3, column=4)
        p_btn = tk.Label(self, text='1 Player', width=20)
        p_btn.grid(row=25, column=4)









if __name__ == '__main__':
    root = tk.Tk()

    root.title('RPScLSp')

    main_frame = OpeningFrame()

    main_frame.pack()

    root.mainloop()
