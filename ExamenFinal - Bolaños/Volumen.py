from tkinter import *

pi=float(3.14)

def ventana():
    def calc_Vol():
        global pi
        try:
            _radio=float(entrada_texto.get())
            _vol=float((_radio**3)* (4/3)* pi)
            etiqueta.config(text=_vol)
        except ValueError:
            etiqueta.config(text="Introduce el radio de la esfera")
    
    vesf=Tk()
    vesf.title("Volumen Esfera")

    vp=Frame(vesf)
    
    vp.grid(column=0, row=0, padx=(50,50), pady=(80,80))
    vp.columnconfigure(0, weight=1)
    vp.rowconfigure(0, weight=1)

    etiqueta = Label(vp, text="Volumen esfera...")
    etiqueta.grid(column=2, row=2, sticky=(W,E))
    
    boton = Button(vp, text="Calcular", command=calc_Vol)
    boton.grid(column=1, row=1)

    valor=""
    entrada_texto = Entry(vp, width=10, textvariable=valor)
    entrada_texto.grid(column=2, row=1)

    



