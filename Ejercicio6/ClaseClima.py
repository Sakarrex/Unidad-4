import requests
class Clima:
    __url = None
    __clima = None
    
    def __init__(self):
        self.__url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=6842f2b6378e3b38fadba554975c2d96"
        self.__clima = None
    
    def obtener(self,nombreCapital):
        
        response = requests.get(self.__url.format(nombreCapital))
        self.__clima = response.json()
    
    def getTemperatura(self):
        temperatura = ""
        if self.__clima != None:
            temperatura = self.__clima['main']['temp']
        return temperatura
    
    def getTermica(self):
        termica = ""
        if self.__clima != None:
            termica = self.__clima['main']['feels_like']
        return termica
    
    def getHumedad(self):
        humedad = ""
        if self.__clima != None:
            humedad = self.__clima['main']['humidity']
        return humedad

    