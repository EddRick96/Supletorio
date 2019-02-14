from tkinter import *
import Volumen
import Archivo
import Pygame_name

def app_Volumen():
    Volumen.ventana()
    
def app_Archivo():
    Archivo.copiarArch()
def app_Pygame():
    Pygame_name.main()


app=Tk()

app.title("EXAMEN FINAL - ERICK BOLAÑOS")

#Ventana Principal

vpp = Frame(app)
vpp.grid(column=0, row=0, padx=(150,150), pady=(150,150))
vpp.columnconfigure(0, weight=1)
vpp.rowconfigure(0, weight=1)

#LABELS
etiqueta_1 = Label(vpp, text="APLICACION 1")
etiqueta_1.grid(column=1, row=0, sticky=(W,E))

etiqueta_2 = Label(vpp, text="APLICACION 2")
etiqueta_2.grid(column=1, row=2, sticky=(W,E))

etiqueta_2 = Label(vpp, text="APLICACION 3")
etiqueta_2.grid(column=1, row=4, sticky=(W,E))

#BUTTONS

boton_1 = Button(vpp, text="1", command=app_Volumen)
boton_1.grid(column=3, row=0)

boton_2 = Button(vpp, text="2", command=app_Archivo)
boton_2.grid(column=3, row=2)

boton_3 = Button(vpp, text="3", command=app_Pygame)
boton_3.grid(column=3, row=4)


vpp.mainloop()
