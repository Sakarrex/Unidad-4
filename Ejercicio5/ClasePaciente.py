import re
class Paciente:
    __nombre = None
    __apellido = None
    __telefono = None
    __peso = None
    __altura = None
    telefonoRegex = re.compile(r"\([0-9]{3}\)[0-9]{7}")

    def __init__(self,nombre,apellido,telefono,peso,altura):
        self.__nombre = self.requerido(nombre,"Nombre es un campo requerido")
        self.__apellido = self.requerido(apellido,"Apellido es un campo requerido")
        self.__telefono = self.formatovalido(telefono,self.telefonoRegex,"Telefono no teine formato valido")
        self.__peso = int(peso)
        self.__altura = int(altura)
    
    def requerido(self,valor,mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor
    
    def formatovalido(self,valor,regex,mensaje):
        if not valor or not regex.match(valor):
            raise ValueError(mensaje)
        return valor


    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getTelefonmo(self):
        return self.__telefono
    
    def getPeso(self):
        return self.__peso
    
    def getAltura(self):
        return self.__altura
    
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                apellido = self.__apellido,
                nombre = self.__nombre,
                telefono = self.__telefono,
                peso = self.__peso,
                altura = self.__altura
            )
        )
        return d