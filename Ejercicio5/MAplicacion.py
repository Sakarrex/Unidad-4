
from tkinter import *
from tkinter import ttk,messagebox


class Aplicacion():
    __ventana = None
    __altura = None
    __peso = None
    __resultado = None
    __tipodepeso = None
    def __init__(self):
        opts = {'ipadx': 0, 'ipady': 0, 'sticky': 'nswe'}
        self.__ventana = Tk()
        self.__ventana.title('Calculadora de indice corporal')
        mainframe = ttk.Frame(self.__ventana, padding="2 2 10 10")
        mainframe.grid(column=0, row=0, **opts)
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        
        self.__altura = StringVar()
        self.__peso = StringVar()
        self.__resultado = StringVar()
        self.__tipodepeso = StringVar()

        self.alturaEntry = ttk.Entry(mainframe, width=7, textvariable=self.__altura)
        self.alturaEntry.grid(column=1, row=0, columnspan = 2, **opts)
        ttk.Label(mainframe, text="Altura:").grid(column=0, row=0,**opts)
        ttk.Label(mainframe, text="Cm").grid(column=3, row=0,**opts)

        
        ttk.Label(mainframe, text="Peso:").grid(column=0, row=1, **opts)
        self.pesoEntry = ttk.Entry(mainframe, width=7, textvariable= self.__peso)
        self.pesoEntry.grid(column=1, row=1,columnspan=2,**opts)
        ttk.Label(mainframe, text="Kg").grid(column=3, row=1,**opts)

        ttk.Label(mainframe,text="Tu indice de masa corporal (IMC) es: ").grid(column=0, row=4,**opts)
        ttk.Label(mainframe,textvariable=self.__resultado).grid(column=1, row=4,**opts)
        ttk.Label(mainframe,textvariable=self.__tipodepeso).grid(column=1, row=5,**opts)

        self.botoncalcular = ttk.Button(mainframe, text= "Calcular", padding=(2,2), command= self.calcularIMC).grid(column=0, row=3,**opts)
        self.botonlimpiar = ttk.Button(mainframe, text= "limpiar", padding=(2,2), command= self.limpiar).grid(column=1, row=3,**opts)




        for child in mainframe.winfo_children():
            child.grid_configure(padx=2, pady=2)
        self.alturaEntry.focus()
        self.__ventana.mainloop()
    
    def calcularIMC(self):
        if self.alturaEntry.get() != "" and self.pesoEntry.get() != "":
            try:
                #PREGUNTAR CALCULO
                peso = float(self.pesoEntry.get())
                altura = float(self.alturaEntry.get())/100
                result = peso/(altura*altura)
                self.__resultado.set(result)
                if result < 18.5:
                    self.__tipodepeso.set("Peso inferior al normal")
                elif result >= 18.5 and result < 24.9:
                    self.__tipodepeso.set("Normal")
                elif result >= 25 and result < 29.9:
                    self.__tipodepeso.set("Peso superior al normal")
                elif result >= 30:
                    self.__tipodepeso.set("Obesidad")
                
            except ValueError:
                messagebox.showerror(title="Error",message="Debe ingresar los valores")
                self.__peso.set('')
                self.__altura.set('')
                self.alturaEntry.focus()
    
    def limpiar(self):
        self.__peso.set('')
        self.__altura.set('')
        self.__tipodepeso.set('')
        self.__resultado.set('')


            
    