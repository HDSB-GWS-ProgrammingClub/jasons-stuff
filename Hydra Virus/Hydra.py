from tkinter import *

root = Tk()
root.geometry('300x300')
root.title("Hydra Virus")

hydraLabel = Label(root, text='Cut off one head and two more will take its place')
hydraLabel.pack()

def newWindow():
    global root
    root = Tk()
    root.geometry('300x300')
    root.title("Hydra Virus")
    hydraLabel = Label(root, text='Cut off one head and two more will take its place')
    hydraLabel.pack()

    root.protocol("WM_DELETE_WINDOW", on_closing)

def on_closing():
    root.destroy()

    newWindow()
    newWindow()

root.protocol("WM_DELETE_WINDOW", on_closing)


root.mainloop()