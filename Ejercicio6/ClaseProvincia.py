
class Provincia:
    __nombre = None
    __capital = None
    __cantHabitantes = None
    __cantDepartamentos = None
    def __init__(self,nombre,capital,habitantes,departamentos):
        self.__nombre = self.__nombre=self.requerido(nombre, 'Nombre es un valor requerido')
        self.__capital = self.__capital=self.requerido(capital, 'Capital es un valor requerido')
        self.__cantHabitantes = self.__cantHabitantes=self.requerido(int(habitantes), 'CantHabitantes es un valor requerido')
        self.__cantDepartamentos = self.__cantDepartamentos=self.requerido(int(departamentos), 'CantDepartamentos es un valor requerido')

    def getNombre(self):
        return self.__nombre
    def getCapital(self):
        return self.__capital
    def getCantHabitantes(self):
        return self.__cantHabitantes
    def getDepartamentos(self):
        return self.__cantDepartamentos
  
    
    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor
   
    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                                    nombre=self.__nombre,
                                    capital=self.__capital,
                                    habitantes=self.__cantHabitantes,
                                    departamentos=self.__cantDepartamentos
                                )
                )
        return d

