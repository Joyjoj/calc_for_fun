пimport random
from tkinter import Tk, Button, Entry, Label

window = Tk()
window.config(background='black')
window.minsize(width=500, height=200)


def change_text():
    ran_list = ['QWE', "FDSF", 'RWER', 'TERTERT', 'TERTERT']
    tre = random.choice(ran_list)
    text_entry.config(text=f'{tre}')


text_entry = Label(text='Yo', background='white')
text_entry.grid(column=0, row=0, sticky='we')
button_test = Button(text='Click me', command=change_text, background='white')
button_test.grid(column=0, row=1)



window.mainloop()


