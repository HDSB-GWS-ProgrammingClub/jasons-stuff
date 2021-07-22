from tkinter import *
from tkinter import ttk
import platform
import os
import subprocess

root = Tk()
root.geometry('700x400')
root.title("Very Fun Surprise")
s = ttk.Style()
s.configure('TLabel', foreground='#00FF00', font=('*', 30))
s.configure('TButton', foreground='#228B22', font=('*', 20))

operatingsystem = str(platform.system())

def shutdown():
    if operatingsystem == 'Windows':
        os.system("shutdown /s /t 1")
    elif operatingsystem == 'Darwin':
        subprocess.run(['shutdown', '-r', 'now'])
        subprocess.run(['sudo', 'shutdown', '-r', 'now'])
    elif operatingsystem == 'Linux':
        subprocess.run(['shutdown', '-h', 'now'])
        subprocess.run(['sudo', 'shutdown', '-r', 'now'])


dangerWarn = ttk.Label(root, text='Fun Surprise\n')
dangerWarn.pack()

shutdownButton = ttk.Button(root, text='Click me!', command=shutdown)
shutdownButton.pack()

Label(root, text='\n\n\n\n\nMade by Jason').pack()

root.mainloop()