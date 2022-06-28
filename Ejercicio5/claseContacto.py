import re
class Contacto(object):
    telefonoRegex = re.compile(r"\([0-9]{3}\)[0-9]{7}")
    __apellido=None
    __nombre=None
    __telefono=None
    __peso = None
    __altura = None

    def __init__(self, apellido, nombre,telefono,peso,altura):
        self.__apellido=self.requerido(apellido, 'Apellido es un valor requerido')
        self.__nombre = self.__nombre=self.requerido(nombre, 'Nombre es un valor requerido')
        self.__telefono = self.formatoValido(telefono, Contacto.telefonoRegex, 'Teléfono no tiene formato correcto')
        self.__peso = self.requerido(float(peso),"Peso es un valor requerido")
        self.__altura = self.requerido(int(altura),"Altura es un valor requerido")
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getTelefono(self):
        return self.__telefono
    def getPeso(self):
        return self.__peso
    def getAltura(self):
        return self.__altura
    
    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor
    def formatoValido(self, valor, regex, mensaje):
        if not valor or not regex.match(valor):
            raise ValueError(mensaje)
        return valor
    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                                    apellido=self.__apellido,
                                    nombre=self.__nombre,
                                    telefono=self.__telefono,
                                    peso=self.__peso,
                                    altura = self.__altura
                                )
                )
        return d

