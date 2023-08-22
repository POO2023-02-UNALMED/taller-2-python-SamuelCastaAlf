class Asiento:
    def _init_(self,color,precio,registro):
        self.color= color
        self.precio= precio
        self.registro = registro
    def cambiarColor(color):
        color=str(input())
        if (color == "rojo" or color=="verde" or color=="amarillo" or color=="negro" or color=="blanco"):
            self.color=color
            return self.color

class Motor:
    def _init_(self,numeroCilindros,tipo,registro):
        self.numeroCilindros = numeroCilindros
        self.tipo= tipo
        self.registro= registro
    def cambiarRegistro(registro):
        self.registro= registro
        return self.registro
    def asignarTipo(tipo):
        if(tipo=="electrico" or tipo=="gasolina"):
            self.tipo = tipo
            return self.tipo
        
class Auto:
    cantidadCreados
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo = modelo
        self.precio= precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        pass