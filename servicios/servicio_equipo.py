from servicios.servicio import Servicio

class ServicioEquipo(Servicio):
    """
    Servicio de alquiler de equipos.
    """

    def calcular_costo(self, dias, descuento=0.0):
        if dias <= 0:
            raise ValueError("Días inválidos")

        costo = self.precio_base * dias
        return costo - descuento

    def descripcion(self):
        return "Servicio de alquiler de equipos"