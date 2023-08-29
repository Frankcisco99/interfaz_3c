import tkinter
from tkinter import ttk

def obtenerValores():
    valor = entrada.get()
    print(valor)
ventana = tkinter.Tk()
ventana.geometry("300x200")
ventana.title("Codigos de error")
#Etiqueta de texto
titulo = ttk.Label(ventana, text="Ingresa el codigo")
titulo.pack()
#entrada de texto
entrada = ttk.Entry(ventana)
entrada.pack()
boton = ttk.Button(ventana, text="Buscar codigo", command=obtenerValores)
boton.pack()
ventana.mainloop()
