from entidades import Cliente
from servicios import ServicioSala, ServicioEquipo, ServicioAsesoria
from reservas import Reserva
from logger_config import logger

def ejecutar():   #Función principal para ejecutar las pruebas simuladas

    resultados = []  #Lista para guardar los resultados de las pruebas

    pruebas = [  #Lista de funciones lambda para crear objetos de prueba, algunas con datos válidos y otras con datos inválidos para probar las validaciones y manejo de errores
        lambda: Cliente('Juan Perez','juan@mail.com'),
        lambda: Cliente('Li','badmail'),
        lambda: Cliente('Maria Lopez','maria@mail.com'),
        lambda: ServicioSala('Sala Premium',100),
        lambda: ServicioEquipo('Laptop',50),
        lambda: ServicioAsesoria('Python',200),
        lambda: ServicioSala('Error',-1),
    ]

    objetos = [] #lista para guardar los objetos creados durante las pruebas

    for i,p in enumerate(pruebas,1): #por cada función de prueba, se intenta crear el objeto correspondiente y se guarda el resultado en la lista de resultados, manejando cualquier excepción que pueda ocurrir durante la creación del objeto
        try:
            obj = p()
            objetos.append(obj)
            resultados.append(f'Prueba {i}: OK')  #Si la creación del objeto fue exitosa, se guarda el resultado como "OK" bajo el numero de prueba correspondiente 
        except Exception as e: #Esta excepcion permite que si hay un error se registra pero el sistema continua ejecutandose sin detenerse
            logger.error(str(e)) #convierte la excepción al tipo str (cadena de texto) para poder guardarla en el log de errores utilizando el logger configurado previamente y para ser imprimido en pantalla
            resultados.append(f'Prueba {i}: {e}') #Si hubo un error durante la creación del objeto, se guarda el mensaje de error en los resultados bajo el numero de prueba correspondiente

    #se establece que se usara la prueba 1 (cliente valido) y el servicio 1 (en la posición 4 de la lista) para las pruebas de reserva
    cliente = objetos[0] 
    servicio = objetos[3]

    #en esta lista de tuplas se definen tres casos de prueba con el valor de cantidad de servicio y el monto de pago
    casos = [(2,300),(0,100),(3,50)]

    #En este ciclo se crean reservas utilizando el cliente, servicio y la lista que tiene las tuplas con la cantidad del servicio y el monto del pago previamente definidos.
    for j,(cantidad,pago) in enumerate(casos,8): 
        try: #Se crea la reserva, se confirma y se procesa el pago. Al final se guarda el estado de la reserva en la lista de resultados bado el numero de prueba correspondiente(en este ciclo empieza en 8).
            r = Reserva(cliente, servicio, cantidad)
            r.confirmar()
            cambio = r.procesar_pago(pago)
            resultados.append(f'Prueba {j}: cambio {cambio}')
        except Exception as e: # Si ocurre alguna excepción durante la creación, confirmación o procesamiento de pago de la reserva, se registra el error utilizando el logger y se guarda el mensaje de error en los resultados bajo el numero de prueba correspondiente
            logger.error(str(e))
            resultados.append(f'Prueba {j}: {e}')

    for r in resultados:  #con este ciclo se imprimen en pantalla los resultados de todas las pruebas simuladas
        print(r)

if __name__ == '__main__':  #Ejecutando la función principal
    ejecutar()
