from utils.logger import registrar_log
from excepciones.excepciones import ReservaError

class Reserva:
    """
    Clase que gestiona las reservas.
    """

    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        try:
            if self.duracion <= 0:
                raise ValueError("Duración inválida")

            self.estado = "Confirmada"

        except Exception as e:
            registrar_log(f"Error al confirmar reserva: {e}")
            raise ReservaError("No se pudo confirmar la reserva") from e

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar_pago(self):
        try:
            costo = self.servicio.calcular_costo(self.duracion)

        except Exception as e:
            registrar_log(f"Error en cálculo de pago: {e}")
            raise ReservaError("Error en el pago") from e

        else:
            return costo

        finally:
            registrar_log("Intento de procesamiento de pago ejecutado")