from modelos.servicio import Servicio


class ServicioEquipo(Servicio):

    def __init__(self, nombre, precio_base, tipo_equipo):
        super().__init__(nombre, precio_base)
        self.tipo_equipo = tipo_equipo

    def calcular_costo(self, duracion, impuesto=0):
        costo = self.precio_base * duracion
        return costo + impuesto

    def describir_servicio(self):
        return f"Alquiler de equipo: {self.tipo_equipo}"

    def validar_parametros(self):
        if not self.tipo_equipo.strip():
            raise ValueError("Tipo de equipo inválido")
