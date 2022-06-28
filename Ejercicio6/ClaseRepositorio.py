from ClaseManejadorDeProvincias import ManejadorProvincias
from ClaseObjectEncoder import ObjectEncoder
from ClaseProvincia import Provincia
class Repositorio:
    __encoder = None
    __manejador = None

    def __init__(self,encoder):
        self.__encoder = encoder
        diccionario = self.__encoder.leerJSONArchivo()
        self.__manejador = self.__encoder.decodificarDiccionario(diccionario)
    
    def agregarProvincia(self,provincia):
        self.__manejador.agregarProvincia(provincia)
        return provincia
    
    def obtenerListaProvincias(self):
        return self.__manejador.getProvincias()
    
    def guardarJSON(self):
        self.__encoder.guardarJSONArchivo(self.__manejador.toJSON())
        