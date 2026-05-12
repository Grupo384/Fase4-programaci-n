import logging

logging.basicConfig(
    filename="logs/sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Reserva:

    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    # VALIDAR DATOS
    def validar_datos(self):

        if self.cliente is None:
            raise Exception("Cliente inválido")

        if self.servicio is None:
            raise Exception("Servicio no disponible")

        if self.duracion <= 0:
            raise Exception("Duración inválida")

    # PROCESAR RESERVA
    def procesar_reserva(self):

        self.validar_datos()

        costo = self.servicio.calcular_costo(
            self.duracion
        )

        logging.info(
            f"Reserva procesada para {self.cliente.nombre}"
        )

        return costo

    # CONFIRMAR RESERVA
    def confirmar_reserva(self):

        try:

            costo = self.procesar_reserva()

            self.estado = "Confirmada"

            logging.info(
                f"Reserva confirmada para {self.cliente.nombre}"
            )

            return costo

        except Exception as e:

            logging.error(
                f"Error al confirmar reserva: {e}"
            )

            raise Exception(
                "No se pudo confirmar la reserva"
            )

    # CANCELAR RESERVA
    def cancelar_reserva(self):

        if self.estado == "Cancelada":
            raise Exception(
                "La reserva ya estaba cancelada"
            )

        self.estado = "Cancelada"

        logging.info(
            f"Reserva cancelada de {self.cliente.nombre}"
        )

        return "Reserva cancelada correctamente"