class Asiento:
    def _init_(self,color,precio,registro):
        self.color= color
        self.precio= precio
        self.registro = registro
    def cambiarColor(self,color):
        if (color == "rojo" or color=="verde" or color=="amarillo" or color=="negro" or color=="blanco"):
            self.color=color
            return self.color

class Motor:
    def _init_(self,numeroCilindros,tipo,registro):
        self.numeroCilindros = numeroCilindros
        self.tipo= tipo
        self.registro= registro
    def cambiarRegistro(self,registro):
        self.registro= registro

    def asignarTipo(self,tipo):
        if(tipo=="electrico" or tipo=="gasolina"):
            self.tipo = tipo
        
class Auto:
    cantidadCreados=0
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo = modelo
        self.precio= precio
        self.asientos = []
        self.marca = marca
        self.motor = Motor
        self.registro = registro
    def cantidadAsientos(self):
        countAsientos=0
        for i in range(len(self.asientos)):
            if(self.asientos[i]!=None):
                countAsientos+=1
        return countAsientos
    def verificarIntegridad(self):
        if(self.registro==self.motor.registro):
            for i in range(len(self.asientos)):
               if(self.asientos[i]!=None):
                    if(self.asientos[i].registro!=self.registro):
                        return print("Las piezas no son originales") 
            return print("Auto original")
        else:
            return print("Las piezas no son originales")