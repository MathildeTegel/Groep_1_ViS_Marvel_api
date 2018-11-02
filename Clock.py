from tkinter import *
from time import sleep

root = Tk()
clock = Label(root, font=('times', 20, 'bold'))
clock.pack()
time = 0
def tick():
    global time
    sleep(1)
    time += 1
    clock.config(text=time)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)
tick()
root.mainloop()


def tick(self):  # klok functie
    global time
    sleep(1)
    time += 1
    self.clock = Label(self, font=('times', 20, 'bold'))
    self.clock.config(text=time)
    self.clock.after(200, self.tick)
    self.clock.pack()
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky