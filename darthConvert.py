from tkinter import *
root = Tk()
etichettaRoot = Label(root, text="Benvenuto in DarthConvert") # creo un'etichetta
etichettaRoot.pack() #metto l'etichetta nella finestra di root

titoloConv = Label(root, text="Inserisci ingredienti da convertire")
titoloConv.pack()
inserzione = Entry(root, width = 50, fg ="#6F6D6D", bg = "#C9C6C6", borderwidth = 2)
inserzione.pack()

def Click():
    etichetta1 = Label(root, text = "Convertito!")
    etichetta1.pack()
bottConverti = Button(root, text="Converti", command = Click, fg = "white", bg = "#8E3400") #sarebbe da mettere Click(), ma mi crea bug
bottConverti.pack()

root.mainloop() #garantisce che la finestra continuerà ad esserci (in loop) per tutta la durata del programma



