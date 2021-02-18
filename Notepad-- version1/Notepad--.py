from tkinter import *

root = Tk()
root.geometry('600x600')
root.title("Jason's Bad Text Editor (only text, code doesn't work)")

text_input = Text(root, bg='gray', fg='white')
text_input.pack()

buttonFrame = Frame(root, bg='green')
buttonFrame.pack()

output = Label()
def button1():
    global output
    output.destroy()
    text_input_text = text_input.get("1.0",END)
    output = Label(root, text=text_input_text)
    output.pack()

def clearfunc():
    global output
    output.destroy()

printButton = Button(buttonFrame, text='print', command=button1)
printButton.pack(side=LEFT)

clearButton = Button(buttonFrame, text='clear', command=clearfunc)
clearButton.pack(side=LEFT)

root.mainloop()