from tkinter import *
from tkinter import Button


root = Tk()

helv15bi = "Helvetica 15 bold italic"

#def hint_screen(root):
    #hint_text = Text(master= root, font= helv15bi, selectborderwidth=10, wrap=WORD, height=5 )
    #hint_text.pack()
    #hint_text.insert(END, "hinttttt")

#def hint_knop(root):
    #hint_button: Button = Button(master= root, text="hint", command= hint_screen(root))
    #hint_button.pack()


Hint_label_comics = Label(root, text="Click on the 'Hint comics' button to see a list with Comics in which our hero appeared.")

def press():
     Hint_label_comics.config(text="Dit is een hint")

Hint_button_comics = Button (root, text = "Hint Commics", command = press).pack()

Hint_label_comics.pack()



Hint_label_series = Label(root, text="Click on the 'Hint Series' button to see a list with Comics in which our hero appeared.")

def press_hint_series():
    Hint_label_series.config(text= "Dit is een lijst met series")

Hint_button_series = Button(root, text ="Hint Series", command = press_hint_series).pack()

Hint_label_series.pack()


#hint_knop(root)

root.mainloop()

