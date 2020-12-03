from tkinter import *

root = Tk()
root.title("Calcolatrice di Farina00sette")
e = Entry(root, width = 35, borderwidth = 2)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
def Button_click(numero):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(numero))
def Button_clear():
    e.delete(0, END)
def Button_add():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)
def Button_equal():
    second_number = e.get()
    e.delete(0, END)
    e.insert(0, f_num + int(second_number))
    #servono degli if per capire operatore
def Button_meno():
    ter_number = e.get()
    e.delete(0, END)
    e.insert(0, f_num - int(ter_number))
def Button_for()
    quar_number = e.get()
    e.delete(0, END)
    e.insert(0, f_num * int(quar_number))
    
def Button_div()
    penta_number = e.get()
    e.delete(0, END)
    e.insert(0, f_num / int(penta_number))
    
#definire i bottoni
bottone1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: Button_click(1))
bottone2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: Button_click(2))
bottone3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: Button_click(3))
bottone4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: Button_click(4))
bottone5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: Button_click(5))
bottone6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: Button_click(6))
bottone7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: Button_click(7))
bottone8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: Button_click(8))
bottone9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: Button_click(9))
bottone0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: Button_click(0))
bottone_piu = Button(root, text = "+", padx = 39, pady = 20, command = Button_add)
bottone_uguale = Button(root, text = "=", padx = 91, pady = 20, command = Button_equal)
bottone_meno = Button(root, text = "-", padx = 39, pady = 20, command = Button_meno)
bottone_per = Button(root, text = "*", padx = 39, pady = 20, command = Button_for)
bottone_diviso = Button(root, text = "/", padx = 39, pady = 20, command = Button_div)
bottone_canc = Button(root, text = "C", padx = 91, pady = 20, command = Button_clear)

#posizionare i bottoni

bottone1.grid(row = 3, column = 0)
bottone2.grid(row = 3, column = 1)
bottone3.grid(row = 3, column = 2)

bottone4.grid(row = 2, column = 0)
bottone5.grid(row = 2, column = 1)
bottone6.grid(row = 2, column = 2)

bottone7.grid(row = 1, column = 0)
bottone8.grid(row = 1, column = 1)
bottone9.grid(row = 1, column = 2)

bottone0.grid(row = 4, column = 0)
bottone_piu.grid(row = 5, column = 0)
bottone_uguale.grid(row = 5, column = 1, columnspan = 2)
bottone_canc.grid(row = 4, column = 1, columnspan = 2)

root.mainloop() #garantisce che la finestra continuerà ad esserci (in loop) per tutta la durata del programma