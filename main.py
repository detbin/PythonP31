import tkinter
from tkinter import ttk
def selected_item():
    for i in listbox.curselection():
        print(listbox.get(i))
        return seleccion
window = tkinter.Tk()
window.columnconfigure(0, weight=3)
window.columnconfigure(1, weight=1)
window.columnconfigure(1, weight=3)
window.columnconfigure(1, weight=2)
label= tkinter.Label(window, text='Seleccione uns de las siguientes opciones:', bg='blue', fg='white')
label.grid(row=0, column=0, sticky=tkinter.NW)
lista=['Amarillo','Azul', 'Rojo','Verde','Rosa','Morado']
listaitems = tkinter.StringVar (value=lista)
listbox= tkinter.Listbox(window,'',listvariable=listaitems)
listbox.grid(row=0, column=1, sticky=tkinter.W)
btn = tkinter.Button(window, text='print selection', command=selected_item)
btn.grid(row=0,column=2, sticky=tkinter.S)
window.mainloop()
window.quit()
