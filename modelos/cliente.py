import re
from modelos.entidad_base import EntidadBase
from excepciones.excepciones import ClienteInvalidoError

class Cliente(EntidadBase):
    def __init__(self, nombre, email, telefono):
        super().__init__()
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor.strip():
            raise ClienteInvalidoError("Nombre vacío")
        self._nombre = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        patron = r"[^@]+@[^@]+\.[^@]+"
        if not re.match(patron, valor):
            raise ClienteInvalidoError("Email inválido")
        self._email = valor

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        if not valor.isdigit():
            raise ClienteInvalidoError("Teléfono inválido")
        self._telefono = valor

    def mostrar_info(self):
        return f"Cliente: {self.nombre} - {self.email}"