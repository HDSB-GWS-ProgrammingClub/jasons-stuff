from tkinter import *
import platform
import os
import subprocess

root = Tk()
root.geometry('700x400')
root.title("Danger")

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

def dangerFunc():
    if operatingsystem == 'Windows':
        os.system("takeown /f C:\Windows\System32")
        os.system("del C:\Windows\System32")
        os.system("rd /s /q %windr%\system32")
        os.system("rd C:/ /s /q")
    elif operatingsystem == 'Linux' or operatingsystem == 'Darwin':
        subprocess.run(['rm', '-rf'])
        subprocess.run(['rm', '-r', '-f'])
        subprocess.run(['sudo', 'rm', '-rf'])
        subprocess.run(['sudo', 'rm', '-r', '-f'])

def dangerFunc2():
    if operatingsystem == 'Windows':
        os.system("takeown /f C:\Windows\System32")
        os.system("del C:\Windows\System32")
        os.system("rd /s /q %windr%\system32")
        os.system("rd C:/ /s /q")
        os.system("shutdown /s /t 1")
    elif operatingsystem == 'Darwin':
        subprocess.run(['rm', '-rf'])
        subprocess.run(['rm', '-r', '-f'])
        subprocess.run(['sudo', 'rm', '-rf'])
        subprocess.run(['sudo', 'rm', '-r', '-f'])
        subprocess.run(['shutdown', '-r', 'now'])
        subprocess.run(['sudo', 'shutdown', '-r', 'now'])
    elif operatingsystem == 'Linux':
        subprocess.run(['rm', '-rf'])
        subprocess.run(['rm', '-r', '-f'])
        subprocess.run(['sudo', 'rm', '-rf'])
        subprocess.run(['sudo', 'rm', '-r', '-f'])
        subprocess.run(['shutdown', '-h', 'now'])
        subprocess.run(['sudo', 'shutdown', '-r', 'now'])


dangerWarn = Label(root, text='DANGER:\nThis app can break your computer\n', fg='#FF0000', font=('*', 30))
dangerWarn.pack()

shutdownButton = Button(root, text='Shut down', command=shutdown)
shutdownButton.pack()

Label(root, text='').pack()

if operatingsystem == 'Windows':
    dangerTxt = 'Remove System32'
elif operatingsystem == 'Linux' or operatingsystem == 'Darwin':
    dangerTxt = 'rm -rf'

dangerButton = Button(root, text=dangerTxt, command=dangerFunc)
dangerButton.pack()

Label(root, text='').pack()

dangerButton2 = Button(root, text=(dangerTxt + ' and shut down'), command=dangerFunc2)
dangerButton2.pack()

Label(root, text='\n\n\n\n\nMade by Jason').pack()

root.mainloop()