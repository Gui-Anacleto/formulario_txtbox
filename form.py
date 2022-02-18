encoding = "utf-8"

from tkinter import *
import os

c=os.path.dirname(__file__)
nomeArquivo=c+"\\nomes.txt"

def gravarDados():
    arquivo=open(nomeArquivo,"a")
    arquivo.write("Nome...:%s" % fname.get())
    arquivo.write("\nOBS...:%s" % fobs.get("1.0",END))

win=Tk()
win.title("Formulario")
win.geometry("500x300")
win.configure(background="#dde")

#anchor=> N=Norte, S=Sul, E=Lest, W=Oeste
#Ne=Nordeste, SE=Sudeste, SO=Sudeste, No=Noroeste

Label(win, text="Nome", background="#dde", foreground="#009", anchor=W).place(x=10,y=10,width=100,height=20)
fname=Entry(win)
fname.place(x=10,y=30,width=200,height=20)

Label(win, text="OBS", background="#dde", foreground="#009", anchor=W).place(x=10,y=50,width=100,height=20)
fobs=Text(win)
fobs.place(x=10,y=70,width=300,height=80)


btn=Button(win, text="imprimir", command=gravarDados).place(x=10,y=160,width=100,height=20)

win.mainloop()
