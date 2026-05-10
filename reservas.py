from excepciones import ReservaError
from logger_config import logger

class Reserva:
    def __init__(self, cliente, servicio, cantidad):
        self.cliente = cliente
        self.servicio = servicio
        self.cantidad = cantidad
        self.estado = 'pendiente' #el estado inicial de la reserva es "pendiente" hasta que se confirme o cancele

    def confirmar(self):
        try:
            if self.cantidad <= 0: #asegura que la cantidad del servicio no sea cero o negativa, si es así se lanza una excepción ValueError con el mensaje "Cantidad inválida"
                raise ValueError('Cantidad inválida')
        except ValueError as e: #Si ocurre una excepción durante la validación de la cantidad, se registra el error utilizando el logger y se lanza una nueva excepción ReservaError con el mensaje "No se pudo confirmar", utilizando la sintaxis "raise ... from e" para indicar que la nueva excepción fue causada por la excepción original.
            logger.error(str(e))
            raise ReservaError('No se pudo confirmar') from e
        else: #Si no hay excepciones, se confirma la reserva
            self.estado = 'confirmada'
            logger.info('Reserva confirmada')
        finally: #Independientemente de si hubo una excepción o no, se registra un mensaje de log indicando que se ha finalizado el proceso de confirmación de la reserva.
            logger.info('Fin confirmación')

    def cancelar(self): #Esta función cancela la reserva, cambiando su estado a "cancelada" y registrando un mensaje de log indicando que la reserva ha sido cancelada.
        self.estado = 'cancelada'
        logger.info('Reserva cancelada')

    def procesar_pago(self, monto): #Esta función procesa el pago de la reserva, calculando el costo total y verificando si el monto pagado es suficiente.
        costo = self.servicio.calcular_costo(self.cantidad, impuesto=0.19)
        if monto < costo:
            raise ReservaError('Pago insuficiente')
        self.estado = 'pagada'
        logger.info('Pago exitoso')
        return round(monto - costo,2)
