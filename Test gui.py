from tkinter import *
import marvel_api
import pe1_7     # marilènes code
from tkinter import *
from time import sleep

time = 0

welkoms_text = "Welcome Player to the awesome world of Marvel! n/"

helv15bi = "Helvetica 15 bold italic"

tekst_description_hero = "Er was ooit een held die heel heldhaftig was "

question_number_tracker = (1,2,3,4,5,6,7,8,9,)


class Marvel_GUI (Frame):
    #eerste frame waarin iets gebeurd.
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.welkoms_scherm()
        # standaard scherm, maakt alleen het welkomscherm aan

    def welkoms_scherm(self):
        # Opend welkoms scherm en presenteerd daarop de game uitleg en start button voor de game
        self.game_explanation = Text(self, font= helv15bi, selectborderwidth=10, wrap=WORD, height=5 )
        self.game_explanation.pack ()
        self.game_explanation.insert(END, welkoms_text)
        self.new_game_button = Button(self, text = "New Game", command = self.new_game)
        self.new_game_button.pack()
        self.view_highscore_button = Button(self, text = "View Highscores", command = self.high_scores)
        self.view_highscore_button.pack()

    def high_scores (self):
        # haalt de onderdelen van het vorige scherm weg en toont de top tien highscores
        self.new_game_button.destroy()
        self.game_explanation.destroy()
        self.view_highscore_button.destroy()
        self.highscore_label = Label(self, text = "Top 10 Highscores")
        self.description_highscore = Label(self, text = "namenlijst highscore") #
        self.menu_button_highscore = Button(self, text = "Back to Menu", command = self.welcoms_screen_from_highscore())
        self.menu_button_highscore.pack()

    def welcoms_screen_from_highscore (self):
        self.highscore_label.destroy()
        self.description_highscore.destroy()
        self.menu_button_highscore.destroy()
        self.welkoms_scherm()


    def new_game(self):
        # verwijderd de buttons en roept de vragen op
        self.new_game_button.destroy()
        self.game_explanation.destroy()
        self.view_highscore_button.destroy()
        self.question_screen()

    def press_hint_comics(self):
        # hiermee zeg je dat de hint series pas te zien zijn als je op de knop drukt
        answer_name, answer_description, answer_comics, answer_series, full_answer_list = marvel_api.create_question()
        self.Hint_label_comics.config(text= answer_comics)

    def press_hint_series(self):
        # met deze def zeg je dat de hint series pas series laat zien als je op de knop drukt
        answer_name, answer_description, answer_comics, answer_series, full_answer_list = marvel_api.create_question()
        self.Hint_label_series.config(text=answer_series)




    def question_screen(self, next_question):
        def next_question(self):
            for number in range(1,10):  # hier door komen de vragen in een loep voor 10x
                number += 1
                print(number)
                self.description_hero.destroy()
                self.Hint_label_comics.destroy()
                self.Hint_button_comics.destroy()
                self.Hint_label_series.destroy()
                self.Hint_button_series.destroy()
                self.button_answer.destroy()
                self.question_screen(number)

                if number != (10):
                    # roept vragen description, hint, en antwoorden op.
                    answer_name, answer_description, answer_comics, answer_series, full_answer_list = marvel_api.create_question()
                    self.description_hero = Label(self, text=answer_description, font=helv15bi)
                    self.description_hero.pack()
                    self.Hint_label_comics = Label(self, text="Click on the 'Hint comics' button to see a list with Comics in which our hero appeared.")
                    self.Hint_button_comics = Button(self, text="Hint Commics", command=self.press_hint_comics).pack()
                    self.Hint_label_comics.pack()
                    self.Hint_label_series = Label(self,text="Click on the 'Hint Series' button to see a list with Comics in which our hero appeared.")
                    self.Hint_button_series = Button(self, text="Hint Series", command=self.press_hint_series).pack()
                    self.Hint_label_series.pack()

                    # Hierons staan de hints beschreven.
                    self.button_answer = Button(self, text = full_answer_list[number], command= next_question)
                    self.button_answer.pack()
                else:
                    self.end_screen_game()


    def end_screen_game(self):
        self.game_done_textbox = Label(self, text= "Thanks for playing")
        self.menu_button = Button(self, text= "Back to menu", command= self.back_to_menu)
        self.game_done_textbox.pack()
        self.menu_button.pack()

    def back_to_menu (self):
        self.game_done_textbox.destroy()
        self.menu_button.destroy()
        self.welkoms_scherm()



root = Tk()
app = Marvel_GUI(master=root)
app.mainloop()