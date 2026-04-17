from abc import ABC, abstractmethod

class Servicio(ABC):
    """
    Clase abstracta Servicio.
    Define el comportamiento común de todos los servicios.
    """

    def __init__(self, nombre, precio_base):
        if precio_base <= 0:
            raise ValueError("El precio base debe ser mayor a 0")

        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, *args, **kwargs):
        pass

    @abstractmethod
    def descripcion(self):
        pass