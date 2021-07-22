from tkinter import *
import platform
import os
import subprocess

root = Tk()
root.geometry('700x400')
root.title("Very Fun Surprise")

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


dangerWarn = Label(root, text='Fun Surprise\n', fg='#00FF00', font=('*', 30))
dangerWarn.pack()

shutdownButton = Button(root, text='Click me!', command=shutdown, fg='#228B22', font=('*', 20))
shutdownButton.pack()

Label(root, text='\n\n\n\n\nMade by Jason').pack()

root.mainloop()