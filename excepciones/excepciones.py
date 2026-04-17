class SistemaError(Exception):
    """Excepción base del sistema"""
    pass

class ClienteError(SistemaError):
    pass

class ServicioError(SistemaError):
    pass

class ReservaError(SistemaError):
    pass