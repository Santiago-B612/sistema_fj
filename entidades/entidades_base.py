from abc import ABC, abstractmethod

class EntidadBase(ABC):
    """
    Clase abstracta base para todas las entidades del sistema.
    Cumple con el principio de abstracción.
    """

    def __init__(self, id):
        self._id = id

    def get_id(self):
        return self._id

    @abstractmethod
    def mostrar_info(self):
        pass