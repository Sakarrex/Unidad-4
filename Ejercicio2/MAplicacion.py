
from tkinter import *
from tkinter import ttk,messagebox

import tkinter as tk

class Aplicacion(tk.Tk):
    __precioBase = None
    __grabado = None
    __IVA = None
    __precioIVA = None

    def __init__(self):
        super().__init__()
        
        
        self.title('Calculadora de IVA')
        self.config(padx=5, pady=5)
       
        self.__precioBase = StringVar()
        self.__IVA = StringVar()
        self.__grabado = IntVar()
        self.__precioIVA = StringVar()

        ttk.Label(self, text = "Precio sin IVA").grid(row=0, column=0)
        self.entryPrecioBase = ttk.Entry(self,width=7,textvariable=self.__precioBase)
        self.entryPrecioBase.grid(row=0, column=1,ipadx=3,ipady=3)

        ttk.Radiobutton(self,text="IVA 10.5%",value=0,variable=self.__grabado).grid(row =1, column=0, columnspan=1, sticky='w')
        ttk.Radiobutton(self,text="IVA 21%",value=1,variable=self.__grabado).grid(row =2, column=0, columnspan=1, sticky='w')

        ttk.Label(self,text="IVA").grid(row =3, column=0)
        ttk.Label(self,textvariable=self.__IVA).grid(row =3, column=1)

        ttk.Label(self,text="precio con IVA").grid(row =4, column=0)
        ttk.Label(self,textvariable=self.__precioIVA).grid(row =4, column=1)

        ttk.Button(self,text="Calcular",command=self.calcular).grid(row = 5, column=0)
        ttk.Button(self,text="Salir",command=self.destroy).grid(row = 5, column= 1)

        self.__grabado.set(-1)
        
    
    def calcular(self):
        if self.entryPrecioBase != "" and self.__grabado != -1:
            try:
                IVA = 0
                precioBase = float(self.entryPrecioBase.get())
                if self.__grabado.get() == 0:
                    IVA = precioBase * 10.5/100
                elif self.__grabado.get() == 1:
                    IVA = precioBase * 21/100
                self.__IVA.set(IVA)
                self.__precioIVA.set(IVA+precioBase)
            except ValueError:
                messagebox.showerror(title="Valor incorrecto",message="Ingresar solo valores numericos")


