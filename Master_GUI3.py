from tkinter import *
import marvel_api
import Score_program   # marilènes code
from tkinter import *
from time import sleep


points = 25
min_points = 0
hint = 3
wrongAnswer = 1
question = 'correct'

welkoms_text = "Welcome Player to the awesome world of Marvel!"

helv15bi = "Helvetica 15 bold italic"

tekst_description_hero = "Er was ooit een held die heel heldhaftig was "

question_number_tracker = (1,2,3,4,5,6,7,8,9)



class Marvel_GUI (Frame):
    #eerste frame waarin iets gebeurd.
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.welkoms_scherm()
        # standaard scherm, maakt alleen het welkomscherm aan

    def welkoms_scherm(self):
        # Opend welkoms scherm en presenteerd daarop de game uitleg en start button voor de game
        self.question_count = 0
        self.list_of_widgets = []
        self.game_explanation = Label(self, text=welkoms_text, font= helv15bi, height=10, wraplength=600)
        self.game_explanation.pack ()
        # button to start a new game
        self.new_game_button = Button(self, text = "New Game", command = self.new_game)
        self.new_game_button.pack(side= RIGHT)
        # button to view highscore
        self.view_highscore_button = Button(self, text = "View Highscores", command = self.high_scores)
        self.view_highscore_button.pack(side= RIGHT)

    def high_scores (self):
        # haalt de onderdelen van het vorige scherm weg en toont de top tien highscores
        self.new_game_button.destroy()
        self.game_explanation.destroy()
        self.view_highscore_button.destroy()
        #haalt highscore's op
        self.highscore_label = Label(self, font=helv15bi  ,text = "Top 10 Highscores", height=1, wraplength=600)
        self.highscore_label.pack()
        self.list_of_widgets.append(self.highscore_label)
        #maakt een loop aan dat de tien hoogste waardes te zien zijn
        for highscore_count in range (0,10):
            self.description_highscore = Label(self, text = [highscore_count], height=1) #
            self.description_highscore.pack()
            self.list_of_widgets.append(self.description_highscore)
        # button terug naar main manu
        self.menu_button_highscore = Button(self, text="Back to Menu", command=self.welcoms_screen_from_highscore)
        self.menu_button_highscore.pack(side=BOTTOM)
        self.list_of_widgets.append(self.menu_button_highscore)
        #maakt loop aan dat de 10 beste scores van de dag te zien zijn
        for dayscore_count in range (0,10):
            self.description_dayscore = Label(self, text = "namenlijst highscore"[dayscore_count], height=1)
            self.description_dayscore.pack(side=BOTTOM)
            self.list_of_widgets.append(self.description_dayscore)

        self.dayscore_label = Label(self, font=helv15bi, text="Best scores of the day", height=1)
        self.dayscore_label.pack(side=BOTTOM)
        self.list_of_widgets.append(self.dayscore_label)



    def welcoms_screen_from_highscore (self):
        # verwijderd widgets uit vorige scherm en opend welkoms scherm
        self.clearGrid(self.list_of_widgets)
        self.welkoms_scherm()

    def new_game(self):
        # verwijderd de buttons en roept de vragen op
        self.new_game_button.destroy()
        self.game_explanation.destroy()
        self.view_highscore_button.destroy()
        # vraagt om een username
        self.username_label = Label (self, font= helv15bi, text= "Please choose a user name")
        self.username_label.pack()
        self.name = Entry(self, bd=10 )
        self.name.pack()

        # button om de game te starten
        self.start_game = Button (self, text="Start Game", command = self.start_game_screen)
        self.start_game.pack()
        self.user_name = Score_program.store_points(str(self.name))

    def start_game_screen(self):
        #verwijdert widgets uit vorig scherm en haalt het vragen scherm op
        self.username_label.destroy()
        self.name.forget()
        self.start_game.destroy()
        self.question_screen()


    def question_screen(self):
        #update_score = Score_program.update_score(question,points)

        def press_hint_comics():
            # hiermee zeg je dat de hint series pas te zien zijn als je op de knop drukt
            self.Hint_label_comics.config(text=answer_comics)


        def press_hint_series():
            # met deze def zeg je dat de hint series pas series laat zien als je op de knop drukt
            self.Hint_label_series.config(text=answer_series)

        def check_answer(answer_input, answer_name):
            # controlleerd of de vraag correct is
            print(answer_input)
            if answer_input == answer_name:
                return ('correct')
            else:
                return ('incorrect')
        self.Points = Score_program.update_score(check_answer, points)
        print(self.Points)

        # roept vragen description, hint, en antwoorden op uit marvel_api.
        answer_name, answer_description, answer_comics, answer_series, full_answer_list = marvel_api.create_question()

        # maakt een label aan met description hero
        self.description_hero_labelframe = LabelFrame(self)
        self.description_hero_labelframe.pack(fill="both", expand="yes")
        self.list_of_widgets.append(self.description_hero_labelframe)
        self.description_hero = Label(self.description_hero_labelframe,text=answer_description, font=helv15bi,height=10, wraplength=600)
        self.description_hero.pack()
        self.list_of_widgets.append(self.description_hero)

        # maakt een frame aan voor de comic hint
        self.labelframe_comics = LabelFrame(self)
        self.labelframe_comics.pack(fill="both", expand="yes", side= BOTTOM)
        self.list_of_widgets.append(self.labelframe_comics)

        # maakt een knop aan om de hints te zien
        self.Hint_label_comics = Label(self.labelframe_comics, text="Click on the 'Hint comics' button to see a list with Comics\n in which our hero appeared.",height=8, wraplength=600)
        self.Hint_label_comics.pack()
        self.list_of_widgets.append(self.Hint_label_comics)
        self.Hint_button_comics = Button(self.labelframe_comics, text="Hint Comics", command=press_hint_comics)
        self.Hint_button_comics.pack(side= BOTTOM)
        self.list_of_widgets.append(self.Hint_button_comics)

        # maakt een frame aan voor de series hint
        self.labelframe_series = LabelFrame(self)
        self.labelframe_series.pack(fill="both", expand="yes", side=BOTTOM)
        self.list_of_widgets.append(self.labelframe_series)

        # maakt een label en button aan voor de series hint
        self.Hint_label_series = Label(self.labelframe_series, text="Click on the 'Hint Series' button to see a list with Comics \n in which our hero appeared.",height=8, wraplength=600)
        self.Hint_label_series.pack()
        self.list_of_widgets.append(self.Hint_label_series)
        self.Hint_button_series = Button(self.labelframe_series, text="Hint Series", command=press_hint_series)
        self.Hint_button_series.pack(side=BOTTOM)
        self.list_of_widgets.append(self.Hint_button_series)

        for answer_count in range(0,10):
            #maakt een loop aan voor 10 buttons met antwoorden
            # haalt de waarde uit de geselcteerde knop en stuurt die naar def check _answer
            self.button_answer = Button(self, text = full_answer_list[answer_count], command=lambda t=full_answer_list[answer_count]: [check_answer(t, answer_name), self.next_question()])
            self.button_answer.pack()
            self.list_of_widgets.append(self.button_answer)


        print(full_answer_list)
        print(answer_name)

    def next_question(self):
        # verwijdert alles uit het vorige scherm
        #  maakt een loop aan dat de speler 10 vragen krijgt
        self.clearGrid(self.list_of_widgets)
        print(self.question_count)
        if self.question_count == 9:
            self.end_screen_game()
        else:
            self.question_count += 1
            self.question_screen()

    def clearGrid(self, list_of_widgets):
        # verwijdert alle widgets die in de lijst van widgets zit
        for widget in list_of_widgets:
            widget.destroy()


    def end_screen_game(self):
        # vermeld dat alle vragen beantwoord zijn en wat de punten zijn
        self.game_done_textbox = Label(self, text= "Thanks for playing")
        self.game_done_textbox.pack()
        #self.show_score = Label(self, text=self.Points )
        #self.show_score.pack()
        # button terug naar menu
        self.menu_button = Button(self, text= "Back to menu", command= self.back_to_menu)
        self.menu_button.pack()

    def back_to_menu (self):
        # verwijdert alle widgets en gaat terug naar main menu
        self.game_done_textbox.destroy()
        self.menu_button.destroy()
        self.welkoms_scherm()


root = Tk()
app = Marvel_GUI(master=root)
app.mainloop()