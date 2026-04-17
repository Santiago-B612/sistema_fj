from servicios.servicio import Servicio

class ServicioAsesoria(Servicio):
    """
    Servicio de asesoría especializada.
    """

    def calcular_costo(self, sesiones):
        if sesiones <= 0:
            raise ValueError("Sesiones inválidas")

        return self.precio_base * sesiones

    def descripcion(self):
        return "Servicio de asesoría especializada"