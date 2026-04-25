from tkinter import *
count = 0

def click():
    global count
    count+=1
    lable.config(text=count)
    
window = Tk()
window.config(bg="green")
lable = Label(window,text=count)
lable.config(font=('Monospace',50,'bold'),bg='green')
lable.pack()
button = Button(window,text="click me")
button.config(command=click,font=('Ink Free',20,'bold'),bg="green")
button.config(activebackground='green',activeforeground='yellow')
button.pack()
window.mainloop()
