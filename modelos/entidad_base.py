from abc import ABC, abstractmethod
import uuid

class EntidadBase(ABC):
    def __init__(self):
        self._id = str(uuid.uuid4())

    @abstractmethod
    def mostrar_info(self):
        pass

    @property
    def id(self):
        return self._id