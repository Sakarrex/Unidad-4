


class Fraccion():
    __numerador = None
    __denominador = None
    def __init__(self, numerador, denominador):
        self.__numerador = numerador
        self.__denominador = denominador
    
    def getNumerador(self):
        return self.__numerador
    
    def getDenominador(self):
        return self.__denominador
    
    def __str__(self) -> str:
        if self.__denominador != 1:
            return str(self.__numerador) + "/" + str(self.__denominador)
        else:
            return str(self.__numerador)
    def __add__(self, other):
        if type(other) == Fraccion:
            denominador = self.__denominador * other.getDenominador()
            numerador = (self.__numerador * other.getDenominador())+(self.__denominador*other.getNumerador())
            return Fraccion(numerador,denominador)
        elif type(other) == int or type(other) == float:
            numerador = self.__numerador + (other * self.__denominador)
            return Fraccion(numerador,self.__denominador)
    
    def __sub__ (self, other):
        if type(other) == Fraccion:
            denominador = self.__denominador * other.getDenominador()
            numerador = (self.__numerador * other.getDenominador())-(self.__denominador*other.getNumerador())
            return Fraccion(numerador,denominador)
        elif type(other) == int or type(other) == float:
            numerador = self.__numerador - (other * self.__denominador)
            return Fraccion(numerador,self.__denominador)
    
    def __mul__(self,other):
        if type(other) == Fraccion:
            return Fraccion(self.__numerador * other.getNumerador(),self.__denominador* other.getDenominador())
        elif type(other) == int or type(other) == float:
            return Fraccion(self.__numerador * other,self.__denominador)
    
    

    def __truediv__(self, other):
        if type(other) == Fraccion:
            return self.__mul__(Fraccion(other.getDenominador(), other.getNumerador()))
        if type(other) == int or type(other) == float:
            return self.__mul__(Fraccion(1,other))         
    
    def simplificar(self):
        if self.__denominador != 0:
            resto = self.__numerador % self.__denominador
            if resto != 0:
                if self.__numerador < self.__denominador:
                    i = self.__numerador
                    while i > 1:
                        resto_numerador = self.__numerador % i
                        resto_denominador = self.__denominador % i
                        if resto_numerador == 0 and resto_denominador == 0:
                            self.__numerador = self.__numerador / i
                            self.__denominador = self.__denominador / i 
                        i -= 1
                elif self.__denominador < self.__numerador:
                    i = self.__denominador
                    while i > 1:
                        resto_numerador = self.__numerador % i
                        resto_denominador = self.__denominador % i
                        if resto_numerador == 0 and resto_denominador == 0:
                            self.__numerador = self.__numerador / i
                            self.__denominador = self.__denominador / i 
                        i -= 1
        else:
            self.__numerador = self.__numerador / self.__denominador
            self.__denominador = 1
            
        

