from abc import ABC, abstractmethod
import re
from excepciones import ClienteError

class EntidadBase(ABC):
    @abstractmethod
    def mostrar_info(self):
        pass

class Cliente(EntidadBase):
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or len(valor.strip()) < 3:
            raise ClienteError('Nombre inválido')
        self._nombre = valor.strip().title()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(patron, valor):
            raise ClienteError('Email inválido')
        self._email = valor.lower()

    def mostrar_info(self):
        return f'{self.nombre} - {self.email}'
