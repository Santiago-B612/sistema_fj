from abc import ABC, abstractmethod
from excepciones import ServicioError

class Servicio(ABC): #Clase base abstracta para servicios del sistema
    def __init__(self, nombre, tarifa):
        if tarifa <= 0:
            raise ServicioError('Tarifa inválida')
        self.nombre = nombre
        self.tarifa = tarifa

    @abstractmethod
    def calcular_costo(self, cantidad, impuesto=0, descuento=0): #Método abstracto que debe ser implementado por las clases que hereden de Servicio, se encarga de calcular el costo total del servicio basado en la cantidad, el impuesto y el descuento. Este metodo no tiene una implementación en la clase base, por lo que cualquier clase que herede de Servicio debe proporcionar su propia implementación de este método para calcular el costo específico del servicio que representa.
        pass

class ServicioSala(Servicio): #En el servicio de reserva de salas se calcula el costo badado en la cantidad de horas que se reserva la sala, aplicando el impuesto y descuento si es necesario.
    def calcular_costo(self, horas, impuesto=0, descuento=0):
        subtotal = self.tarifa * horas
        return subtotal * (1 + impuesto - descuento)

class ServicioEquipo(Servicio): #En el servicio de alquiler de equipos se calcula el costo basado en la cantidad de días que se alquila el equipo, aplicando el impuesto y descuento si es necesario.
    def calcular_costo(self, dias, impuesto=0, descuento=0):
        subtotal = self.tarifa * dias
        return subtotal * (1 + impuesto - descuento)

class ServicioAsesoria(Servicio): #En el servicio de asesorías se calcula el costo basado en la cantidad de sesiones que se contratan, aplicando el impuesto y descuento si es necesario.
    def calcular_costo(self, sesiones, impuesto=0, descuento=0):
        subtotal = self.tarifa * sesiones
        return subtotal * (1 + impuesto - descuento)
