from dataclasses import replace
import json

from urllib.request import urlopen

class Cotizador:
    __resultado = None

    def __init__(self) -> None:
        self.__resultado = None
    
    def run(self):
        url_template = 'https://www.dolarsi.com/api/api.php?type=dolar'
        response = urlopen(url_template)
        self.__resultado = json.loads(response.read().decode())
    
    def getResultado(self):
        return self.__resultado
    
    def getPrecio(self):
        precio = float(self.__resultado[0]['casa']['venta'].replace(",","."))
        return precio