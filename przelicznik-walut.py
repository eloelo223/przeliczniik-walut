from tkinter import *
root = Tk()

ile = Entry(root)
waluta = Entry(root)
waluta_nawalute = Entry(root)
ile.grid(row=0, column=2)
waluta.grid(row=1, column=2)
waluta_nawalute.grid(row=2, column=2)


def Myclick():
    if (waluta.get() == 'zl') & (waluta_nawalute.get() == '$'):
        wynik=(int(ile.get()) / 4.20)
    
    if (waluta.get() == 'zl') & (waluta_nawalute.get() == '€'):
        wynik=(int(ile.get()) / 4.65)

    if (waluta.get() == 'zl') & (waluta_nawalute.get() == 'zl'):
        wynik=(int(ile.get()) * 1)

    if (waluta.get() == '$') & (waluta_nawalute.get() == 'zl'): 
        wynik=(int(ile.get()) * 4.20)

    if (waluta.get() == '$') & (waluta_nawalute.get() == '€'): 
        wynik=(int(ile.get()) * 0.90)

    if (waluta.get() == '$') & (waluta_nawalute.get() == '$'):
        wynik=(int(ile.get()) * 1)

    if (waluta.get() == '€') & (waluta_nawalute.get() == 'zl'):
        wynik=(int(ile.get()) * 4.65)

    if (waluta.get() == '€') & (waluta_nawalute.get() == '$'):
        wynik=(int(ile.get()) * 1.11)

    if (waluta.get() == '€') & (waluta_nawalute.get() == '€'):
        wynik=(int(ile.get()) * 1)
    mylabel = Label(root,text=wynik)
    mylabel.grid(row=4,column=2)
def wyczysc():
    mylabel = Label(root,text="                                 ")
    mylabel.grid(row=4,column=2)


mylabel1 = Label(root,text="ilosc")
mylabel2 = Label(root,text="waluta")
mylabel3 = Label(root,text="na walute")


mylabel1.grid(row=0, column=1)
mylabel2.grid(row=1, column=1)
mylabel3.grid(row=2, column=1)
myButton = Button(root,text="zamien", command=Myclick)
myButton.grid(row=3,column=2)
myButton = Button(root,text="wyczysc", command=wyczysc)
myButton.grid(row=3,column=1)

root.mainloop()