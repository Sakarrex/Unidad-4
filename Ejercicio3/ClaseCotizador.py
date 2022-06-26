from urllib import response
import requests

class Cotizador:
    __url = None
    __solicitud = None
    __cotizaciones = None

    def __init__(self,url) -> None:
        self.__url = url
        self.__solicitud = requests.get(self.__url)
        self.__cotizaciones = self.__solicitud.json()
    
    def getPrecio(self):
        precio = 0
        for dolar in self.__cotizaciones:
            if dolar['casa']['nombre'].lower() == "oficial":
                precio = int(dolar['casa']['nombre']['venta']) 
        return precio