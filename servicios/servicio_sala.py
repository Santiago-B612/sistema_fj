from servicios.servicio import Servicio

class ServicioSala(Servicio):
    """
    Servicio de reserva de salas.
    """

    def calcular_costo(self, horas, impuesto=0.0):
        if horas <= 0:
            raise ValueError("Horas inválidas")

        costo = self.precio_base * horas
        return costo + (costo * impuesto)

    def descripcion(self):
        return "Servicio de reserva de salas por horas"