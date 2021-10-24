import tkinter as tk
import boggle_board_randomizer as bbr




def read_wordlist_file(filename):
    """
    Loads a list of words from a txt file
    :param filename: The file of words
    :return: A list containing all the words from the file
    """
    with open(filename, 'r') as fd:
        legit_words = fd.read().splitlines()
        return legit_words


class GameBoard:

    ROW_NUM = 4
    COL_NUM = 4
    TITLE= "boggel"
    BG_DEFAULT="light grey"


    def __init__(self, parent, legit_words):
        """
        This class defines the board's characteristics and initializes it.
        """
        self.legit_words = legit_words

        self.__parent = parent
        self.__parent.title(self.TITLE)

        self.__start_button = tk.Button(self.__parent, text="START", height=1, fg='red')
        self.__start_button["command"]= self.start_of_game_widgets
        self.__start_button.grid(row=0,column=0)
        self.buttons = []
        self.ok_buttons =[]

        self.__score = 0
        self.__score_variable = tk.StringVar(self.__parent, f'score: {self.__score}')
        score_lbl = tk.Label(self.__parent, textvariable=self.__score_variable)
        score_lbl.grid(row=0, column=2)

        self.clear_button = tk.Button(self.__parent, text="enter word", state="disabled",
                                      command=lambda: self.chosen_word())
        self. clear_button.grid(row=1,column=5)

        self.__timer = Timer(self.__parent)

        self.choice = ""
        self.choice_label = tk.StringVar()
        self.choice_label.set("Play Boggle!")
        self.choice_display = tk.Label(self.__parent, textvariable=self.choice_label, font=20)#, width=1)
        self.choice_display.grid(row=1,column=0, columnspan=4)


        self.word_list = []
        self.word_list_label = tk.StringVar()
        self.word_list_tk= tk.Message(self.__parent, textvariable=self.word_list_label)
        self.word_list_tk.grid(row=3, column=5, columnspan=3)
        self.flicker()

    def start_of_game_widgets(self):
        """
        Calls buttons, labels and relevant configurations when a initiating a new game.
        """
        #self.__timer.mins,self.__timer.secs = 0,0
        self.__start_button.configure(state='disabled')
        self.clear_button.configure(state='normal')
        self.buttons.clear()
        self.set_buttons()
        self.refresh_screen()
        self.__score = 0
        self.__score_variable.set(f'score: {self.__score}')
        self.word_list.clear()
        self.word_list_label.set(self.word_list)
        self.quit = tk.Button(self.__parent, text="Quit", command=root.destroy).grid(row=6, column=5)
        self.__timer.start()
        self.end_game()


    def set_buttons(self):
        """
        Creates a grid of buttons, each carries a randomized letter; the games buttons board.
        """
        board_letters= [lower_list(i) for i in bbr.randomize_board()]
        for i in range(GameBoard.ROW_NUM):
            self.buttons.append([])
            for j in range(GameBoard.COL_NUM):
                button = tk.Button(self.__parent, text=board_letters[i][j], width=10, height= 5,
                activebackground="red", activeforeground="yellow", borderwidth="5", bg=self.BG_DEFAULT)
                self.buttons[i].append(button)
                button.grid(row=i + 3, column=j, sticky="")
                button['command'] = lambda the_button=button, c=board_letters[i][j], row=i, col=j: \
                    self.button_command(the_button, c, row, col)

    def button_command(self, button, letter, i, j):
        """
        Configures the visuals of the buttons upon pressing: changes the color of the button and
        displays the button's letter on the screen.
        :param button: a widget, eventful python object
        :param letter: a text string on the button
        :param i , j: the row and column in the grid

        """
        if button in self.ok_buttons:
            for button in self.ok_buttons:
                 button.config(bg=self.BG_DEFAULT)
            self.buttons[i][j].config(bg="purple", state='disabled')
            self.change_ok_buttons(i, j)
            self.choice += letter
            self.choice_label.set(self.choice)

    def change_ok_buttons(self, row, col):
        """
        :param row: row of specific button
        :param col: column of specific button
        change ok_button (the list of the allowed button to press)
        """
        self.ok_buttons.clear()
        size = GameBoard.ROW_NUM
        for i in range(size):
            for j in range(size):
                if row - 1 <= i <= row + 1 and col - 1 <= j <= col + 1:
                    if self.buttons[i][j].cget("state") != "disabled":
                        self.ok_buttons.append(self.buttons[i][j])

    def chosen_word(self):
        """
        Configures the visuals of the grid of buttons upon pressing the enter word button.
        Updates the score if chosen word is legit.
        Resets the the letter choices and button to press.
        """
        if self.choice in self.legit_words and self.choice not in self.word_list:
            self.score_update(self.choice)
            self.word_list.append(self.choice[:])
            self.word_list_label.set(self.word_list)
        self.refresh_screen()


    def flicker(self):
        """
        Makes all the legit buttons flicker (see "ok buttons"). Legit buttons are those which surround the
        button most recently clicked.
        """
        if len(self.ok_buttons) < 10:
            for button in self.ok_buttons:
                current_color = button.cget("background")
                next_color = self.BG_DEFAULT if current_color == "ghost white" else "ghost white"
                button.config(background=next_color)
        self.__parent.after(1000, self.flicker)

    def refresh_screen(self):
        """
        change all buttons to default state ,and refresh the list of legit buttons to press,
        and refresh choice screen
        """
        self.choice = ""
        self.choice_label.set("Choose a letter:" + self.choice)
        self.ok_buttons = [button for sublist in self.buttons for button in sublist]
        [button.config(bg=self.BG_DEFAULT, state='normal') for button in self.ok_buttons]

    def score_update(self, word):
        """
        Updates the the player's score.
        :param word: a legit word the player has just found
        """
        self.__score += int(len(word)**2)
        self.__score_variable.set(f'score: {self.__score}')

    def end_game(self):
        """
        Calls buttons, labels and relevant configurations when the time is up.
        """
        if not self.__timer.you_have_time:
            self.__start_button.configure(state='normal', text="Play Again")
            self.clear_button.configure(state="disabled")
            self.ok_buttons = []
        self.__parent.after(1000, self.end_game)


class Timer:
    MINUTES=0
    SECONDS=30

    def __init__(self, board):
        """
        This class initializes the games's timer.
        The player has 3 minutes to complete one round.
        """
        self.board = board  # A tk root object the belongs to the game
        self.you_have_time = False    # A Boolean variable that gets False when the time is up
        self.start_minutes_value = self.MINUTES
        self.start_seconds_value = self.SECONDS
        self.mins = None                 # will be updated along the countdown
        self.secs = None                 # will be updated along the countdown
        self.display = tk.Label(self.board, height=1, width=10, textvariable="")
        self.display.config(text="00:00")  # Display timer label as "00:00" *before* the game starts
        self.display.grid(row=0, column=5, columnspan=2)

    def countdown(self):
        """
        Updates the text variable of the display label. Displays the min:sec in a 00:00 format.
        """
        if self.you_have_time is True:
            if self.mins == 0 and self.secs == 0:
                self.display.config(text="Time Out!")
                self.you_have_time = False
            else:
                self.display.config(text="%02d:%02d" % (self.mins, self.secs))  # creates the 00:00 format
                self.min_sec_updater()
                self.board.after(1000, self.countdown)

    def min_sec_updater(self):
        """
        Updates the minutes and seconds of the timer.
        """
        if self.secs == 0:
            self.mins -= 1
            self.secs = 59
        else:
            self.secs -= 1

    def start(self):
        """
        Turns on the timer.
        """
        if self.you_have_time is False:
            self.you_have_time = True
            self.mins = self.start_minutes_value
            self.secs = self.start_seconds_value
            self.countdown()


def lower_list(lst):
    """
    lower cap letters in the list
    :param lst: A list of words
    :return: A list of words with low letters
    """
    for i in range(len(lst)):
        lst[i] = lst[i].lower()
    return lst


if __name__ == '__main__':
    legit_words = lower_list(read_wordlist_file('boggle_dict.txt'))
    root = tk.Tk()
    GameBoard(root, legit_words)
    root.mainloop()