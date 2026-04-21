from entidades import Cliente
from servicios import ServicioSala, ServicioEquipo, ServicioAsesoria
from reservas import Reserva
from logger_config import logger

def ejecutar():
    resultados = []

    pruebas = [
        lambda: Cliente('Juan Perez','juan@mail.com'),
        lambda: Cliente('Li','badmail'),
        lambda: Cliente('Maria Lopez','maria@mail.com'),
        lambda: ServicioSala('Sala Premium',100),
        lambda: ServicioEquipo('Laptop',50),
        lambda: ServicioAsesoria('Python',200),
        lambda: ServicioSala('Error',-1),
    ]

    objetos = []
    for i,p in enumerate(pruebas,1):
        try:
            obj = p()
            objetos.append(obj)
            resultados.append(f'Prueba {i}: OK')
        except Exception as e:
            logger.error(str(e))
            resultados.append(f'Prueba {i}: {e}')

    cliente = objetos[0]
    servicio = objetos[3]

    casos = [(2,300),(0,100),(3,50)]
    for j,(cantidad,pago) in enumerate(casos,8):
        try:
            r = Reserva(cliente, servicio, cantidad)
            r.confirmar()
            cambio = r.procesar_pago(pago)
            resultados.append(f'Prueba {j}: cambio {cambio}')
        except Exception as e:
            logger.error(str(e))
            resultados.append(f'Prueba {j}: {e}')

    for r in resultados:
        print(r)

if __name__ == '__main__':
    ejecutar()
