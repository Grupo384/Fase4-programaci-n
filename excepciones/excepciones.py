class SistemaError(Exception):
    """Excepción base del sistema"""
    pass


class ClienteInvalidoError(SistemaError):
    pass


class ServicioNoDisponibleError(SistemaError):
    pass


class ReservaError(SistemaError):
    pass


class DuracionInvalidaError(SistemaError):
    pass