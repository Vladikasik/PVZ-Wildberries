import tkinter
import ttkSimpleDialog


def dialog(event):
    result = ttkSimpleDialog(title='Заголовок окна', prompt='Текст вопроса')
    print(result)


root =tkinter.Tk()
root.title("Основное окно приложения")
root.geometry('-450-250')
but = tkinter.Button(root, text='Открыть диалог')
but.grid(row=0, column=0)
but.bind("<ButtonRelease-1>", dialog)
tkinter.mainloop()