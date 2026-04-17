from datetime import datetime

def registrar_log(mensaje):
    """
    Registra eventos y errores en un archivo logs.txt
    """
    with open("logs.txt", "a") as archivo:
        archivo.write(f"{datetime.now()} - {mensaje}\n")