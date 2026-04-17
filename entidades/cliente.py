from entidades.entidad_base import EntidadBase

class Cliente(EntidadBase):
    """
    Clase Cliente con encapsulación y validaciones estrictas.
    """

    def __init__(self, id, nombre, correo):
        super().__init__(id)
        self.set_nombre(nombre)
        self.set_correo(correo)

    def set_nombre(self, nombre):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = nombre

    def get_nombre(self):
        return self._nombre

    def set_correo(self, correo):
        if "@" not in correo:
            raise ValueError("Correo inválido")
        self._correo = correo

    def get_correo(self):
        return self._correo

    def mostrar_info(self):
        return f"Cliente [{self._id}] - {self._nombre} - {self._correo}"