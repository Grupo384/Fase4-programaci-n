import re
from modelos.entidad_base import EntidadBase
from excepciones.excepciones import ClienteInvalidoError


class Cliente(EntidadBase):
    def __init__(self, id_cliente, nombre, email, telefono):
        super().__init__()
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    # ID
    @property
    def id_cliente(self):
        return self._id_cliente

    @id_cliente.setter
    def id_cliente(self, valor):
        if not str(valor).strip():
            raise ClienteInvalidoError("ID vacío")
        self._id_cliente = valor

    # Nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor.strip():
            raise ClienteInvalidoError("Nombre vacío")
        self._nombre = valor

    # Email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        patron = r"[^@]+@[^@]+\.[^@]+"
        if not re.match(patron, valor):
            raise ClienteInvalidoError("Email inválido")
        self._email = valor

    # Teléfono
    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        if not valor.isdigit():
            raise ClienteInvalidoError("Teléfono inválido")
        self._telefono = valor

    # Métodos
    def mostrar_info(self):
        return f"ID: {self.id_cliente} - Cliente: {self.nombre} - Email: {self.email}"

    def __str__(self):
        return f"{self.nombre} - {self.email}"
