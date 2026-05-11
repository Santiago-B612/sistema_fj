from abc import ABC, abstractmethod
import re
from excepciones import ClienteError

class EntidadBase(ABC): #Clase base abstracta para entidades del sistema
    @abstractmethod
    def mostrar_info(self):
        pass

class Cliente(EntidadBase): #Clase que representa a un cliente del sistema, hereda de EntidadBase
    def __init__(self, nombre, email): 
        self.nombre = nombre
        self.email = email

    @property # decorador que indica que el método siguiente es un getter para la propiedad "nombre"
    def nombre(self):
        return self._nombre

    @nombre.setter # decorador que indica que el método siguiente es un setter para la propiedad "nombre". Antes de asignarse un valor a nombre primero debe pasar esta función.
    def nombre(self, valor):
        if not valor or len(valor.strip()) < 3: #Valida que el nombre no esté vacío y tenga al menos 3 caracteres después de eliminar espacios en blanco. Si no cumple esta condición, se lanza una excepción ClienteError con el mensaje "Nombre inválido".
            raise ClienteError('Nombre inválido')
        self._nombre = valor.strip().title() #Si el nombre es válido, se asigna a la variable de instancia _nombre después de eliminar espacios en blanco y convertirlo a formato título (primera letra mayúscula y el resto minúscula).

    @property # decorador que indica que el método siguiente es un getter para la propiedad "email"
    def email(self):
        return self._email

    @email.setter # decorador que indica que el método siguiente es un setter para la propiedad "email". Antes de asignarse un valor a email primero debe pasar esta función.
    def email(self, valor):
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$' #Expresión regular para validar el formato del correo electrónico. El patrón verifica que el correo tenga un formato básico de dirección de correo electrónico (texto antes de @, seguido de un dominio y una extensión).
        if not re.match(patron, valor): # si no cumple con el patrón de correo electrónico, se lanza una excepción ClienteError con el mensaje "Email inválido".
            raise ClienteError('Email inválido')
        self._email = valor.lower() #Si el correo electrónico es válido, se asigna a la variable de instancia _email después de convertirlo a minúsculas.

    def mostrar_info(self): #esta función implementa el método abstracto de la clase base EntidadBase, devuelve una cadena con el nombre y correo electrónico del cliente formateados.
        return f'{self.nombre} - {self.email}'
