import tkinter as tk
from tkinter import ttk,messagebox
from tkinter import *

from ClaseCotizador import Cotizador
class Aplicacion(tk.Tk):
    __dolar = None
    __pesos = None
    __cotizador = None

    def __init__(self):
        self.__cotizador = Cotizador("https://www.dolarsi.com/api/api.php?type=dolar")
        super().__init__()
        opts = {'ipadx': 3, 'ipady': 3, 'sticky': 'nswe'}
        self.title = "Conversor de dolares"
        self.resizable(0,0)

        self.__dolar = StringVar()
        self.__pesos = StringVar()
        self.__pesos.trace('w',self.calcular)

        self.entryDolares = tk.Entry(self,width=7,textvariable=self.__dolar)
        self.entryDolares.grid(row=0,column=1,**opts)
        ttk.Label(self,text="dolares").grid(row=0,column=2,**opts)
        ttk.Label(self,text="es equivalente a").grid(row=1,column=0,**opts)
        ttk.Label(self,textvariable=self.__pesos).grid(row=1,column=1,**opts)
        ttk.Label(self,text="pesos").grid(row=1,column=2,**opts)
        ttk.Button(self,text = "Salir", command= self.destroy).grid(row=1,column=3,**opts)
        
        self.entryDolares.focus()
        self.mainloop()
    
    def calcular(self,*args):
        if self.entryDolares.get() != "":
            try:
                valor = float(self.entryDolares.get())
                self.__pesos.set(valor*self.__cotizador.getPrecio())
            except ValueError:
                messagebox.showerror(title="Error de valor", message = "Ingresar solo valores numericos")
                self.__dolar.set("")
                self.entryDolares.focus()
        else:
            self.__pesos.set("")

