from entidades.cliente import Cliente
from servicios.servicio_sala import ServicioSala
from servicios.servicio_equipo import ServicioEquipo
from servicios.servicio_asesoria import ServicioAsesoria
from reservas.reserva import Reserva
from utils.logger import registrar_log

def main():
    clientes = []
    reservas = []

    # CASOS DE PRUEBA (mínimo 10)
    try:
        c1 = Cliente(1, "Juan", "juan@gmail.com")
        clientes.append(c1)

        c2 = Cliente(2, "", "correo_invalido")  # ERROR
    except Exception as e:
        registrar_log(f"Error cliente: {e}")

    try:
        servicio1 = ServicioSala("Sala VIP", 100)
        servicio2 = ServicioEquipo("Laptop", 50)
        servicio3 = ServicioAsesoria("Consultoría", 200)

        r1 = Reserva(c1, servicio1, 2)
        r1.confirmar()
        print("Costo:", r1.procesar_pago())
        reservas.append(r1)

        r2 = Reserva(c1, servicio2, -1)  # ERROR
        r2.confirmar()

    except Exception as e:
        registrar_log(f"Error reserva: {e}")

    try:
        r3 = Reserva(c1, servicio3, 3)
        r3.confirmar()
        print("Costo:", r3.procesar_pago())
        reservas.append(r3)

    except Exception as e:
        registrar_log(f"Error reserva: {e}")

if __name__ == "__main__":
    main()