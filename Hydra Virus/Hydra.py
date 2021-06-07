from tkinter import *


class Hydra(Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x300')
        self.title("Hydra Virus")

        self.hydraLabel = Label(self, text='Cut off one head and two more will take its place')
        self.hydraLabel.pack()

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.destroy()
        new1 = Hydra()
        new2 = Hydra()
        new1.mainloop()
        new2.mainloop()

        


new = Hydra()
new.mainloop()