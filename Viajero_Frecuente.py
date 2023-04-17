class Viajero:
    __num_viajero = 0
    __dni = ''
    __nombre= ''
    __apellido = ''
    __millas_acum = 0


    def __init__(self, num_viajero, dni, nombre, apellido, millas_acum) -> None:
        self.__num_viajero = num_viajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas_acum
        pass

    def getmillas(self):
        return self.__millas_acum
    
    def getnombrecompleto(self):
        return self.__nombre + ' ' +self.__apellido

    def acumularMillas(self, entero):
        self.__millas_acum += entero
        print('Sus millas se acumularon con exito, sus millas actuales son {}' .format(self.getmillas()))

    def getnumv(self):
        return self.__num_viajero
    
    def getdni(self):
        return self.__dni
    

    def canjearMillas(self, millascanje):
        if millascanje <= self.__millas_acum:
            self.__millas_acum = self.__millas_acum - millascanje
            print('millas canjeadas con exito, sus millas actuales son {}' .format(self.getmillas()))
        else: return print('Sus millas son insuficientes')
