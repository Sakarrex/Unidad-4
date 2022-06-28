
from vistaContactos import ContactsView, NewContact, IMCview
from claseManejadorContactos import ManejadorContactos
class ControladorContactos(object):
    def __init__(self, repo, vista):
        self.repo = repo
        self.vista = vista
        self.seleccion = -1
        self.contactos = list(repo.obtenerListaContactos())
    # comandos de que se ejecutan a través de la vista
    def crearContacto(self):
        nuevoContacto = NewContact(self.vista).show()
        if nuevoContacto:
            contacto = self.repo.agregarContacto(nuevoContacto)
            self.contactos.append(contacto)
            self.vista.agregarContacto(contacto)
    def seleccionarContacto(self, index):
        self.seleccion = index
        contacto = self.contactos[index]
        self.vista.verContactoEnForm(contacto)
    def modificarContacto(self):
        if self.seleccion==-1:
            return
        rowid = self.contactos[self.seleccion].rowid
        detallesContacto = self.vista.obtenerDetalles()
        detallesContacto.rowid = rowid
        contacto = self.repo.modificarContacto(detallesContacto)
        self.contactos[self.seleccion] = contacto
        self.vista.modificarContacto(contacto, self.seleccion)
        self.seleccion=-1
    def borrarContacto(self):
        if self.seleccion==-1:
            return
        contacto = self.contactos[self.seleccion]
        self.repo.borrarContacto(contacto)
        self.contactos.pop(self.seleccion)
        self.vista.borrarContacto(self.seleccion)
        self.seleccion=-1
    def start(self):
        for c in self.contactos:
            self.vista.agregarContacto(c)
        self.vista.mainloop()
    def calcularIMC(self):
        if self.seleccion == -1:
            return
        
        contacto = self.contactos[self.seleccion]
        altura = contacto.getAltura()/100
        imc = contacto.getPeso()/(altura*altura)
        Composicion = None
        if imc < 18.5:
            Composicion = "Peso inferior al normal"
        elif imc >= 18.5 and imc < 24.9:
            Composicion = "Normal"
        elif imc >= 25 and imc < 29.9:
            Composicion = "Peso superior al normal"
        elif imc >= 30:
            Composicion = "Obesidad"
        VentanaIMC = IMCview(self.vista,float(imc),Composicion).show()

    def salirGrabarDatos(self):
        self.repo.grabarDatos()
