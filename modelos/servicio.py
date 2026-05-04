from abc import ABC, abstractmethod
from modelos.entidad_base import EntidadBase

class Servicio(EntidadBase, ABC):
    def __init__(self, nombre, precio_base):
        super().__init__()
        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, duracion):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    @abstractmethod
    def validar_parametros(self):
        pass