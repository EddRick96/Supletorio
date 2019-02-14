from tkinter import *

def copiarArch():
    def creartxt():
        try:
            #print("Ingrese el nombre del archivo")
            name=entrada_texto.get()
            name2=entrada_texto2.get()
            datos=""
            archi=open(name+'.txt','r')
            while linea != "":
                print(linea)
                
        except ValueError:
            etiq_Exist.config(text="Ingrese un nombre de archivo")

    appcy=Tk()
    appcy=Tk()
    appcy.title("Copiar Archivo")

    vp=Frame(appcy)
    
    vp.grid(column=0, row=0, padx=(50,50), pady=(80,80))
    vp.columnconfigure(0, weight=1)
    vp.rowconfigure(0, weight=1)

    #LABELS
    etiqueta = Label(vp, text="Nombre del archivo base:")
    etiqueta.grid(column=1, row=2, sticky=(W,E))
    
    etiqueta2 = Label(vp, text="Nombre del archivo destino:")
    etiqueta2.grid(column=1, row=3, sticky=(W,E))

    etiq_Exist = Label(vp, text="Copiando..")
    etiq_Exist.grid(column=1, row=4, sticky=(W,E))

    #Button
    boton = Button(vp, text="Copiar", command=creartxt)
    boton.grid(column=3, row=5)

    #ENTRY
    valor=""
    entrada_texto = Entry(vp, width=10, textvariable=valor)
    entrada_texto.grid(column=2, row=2)

    valor2=""
    entrada_texto2 = Entry(vp, width=10, textvariable=valor2)
    entrada_texto2.grid(column=2, row=3)

    
    
