class SistemaError(Exception):
    """Excepción base del sistema."""

class ClienteError(SistemaError):
    """Errores relacionados con clientes."""

class ServicioError(SistemaError):
    """Errores relacionados con servicios."""

class ReservaError(SistemaError):
    """Errores relacionados con reservas."""
