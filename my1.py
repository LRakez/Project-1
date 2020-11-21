from tkinter import *
from tkinter import messagebox

root = Tk()
message = StringVar()
info_str = StringVar()

def btn_click():
    login = message.get()
    word = str(login)
    word1 = word[::-1]
    if word == word1:
        messagebox.showinfo(title='Ответ', message='Да')
    else:
        messagebox.showinfo(title='Ответ', message='Нет')




root['bg'] = '#fafafa'
root.title('Является ли заданное слово палиндромом')
root.wm_attributes('-alpha', 0.7)
root.geometry('450x100')

frame = Frame(root, bg='black')
frame.place(relwidth=1, relheight=1)

message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.1, anchor="c")

btn = Button(frame, text='Жмяк', bg='white', command=btn_click)
btn.place(relx=0.5, rely=0.5, anchor="c")

root.mainloop()




