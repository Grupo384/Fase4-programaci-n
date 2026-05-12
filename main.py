from modelos.cliente import Cliente
from modelos.reserva import Reserva

from modelos.servicio_sala import ServicioSala
from modelos.servicio_equipo import ServicioEquipo
from modelos.servicio_asesoria import ServicioAsesoria

from logs.logs import registrar_log


def ejecutar_pruebas():

    print("=== INICIO DE PRUEBAS ===")

    # 1. Cliente válido
    try:
        c1 = Cliente("Juan Perez", "juan@email.com", "123456")
        print(c1.mostrar_info())
    except Exception as e:
        print(e)
        registrar_log(str(e), "ERROR")

    # 2. Cliente inválido
    try:
        c2 = Cliente("", "correo_malo", "abc")
    except Exception as e:
        print("Error:", e)
        registrar_log(str(e), "ERROR")

    # 3. Servicio sala válido
    try:
        sala = ServicioSala("Sala VIP", 100, 20)
        print(sala.describir_servicio())
    except Exception as e:
        print(e)
        registrar_log(str(e), "ERROR")

    # 4. Servicio equipo válido
    try:
        equipo = ServicioEquipo("PC Gamer", 50, "Computador")
        print(equipo.describir_servicio())
    except Exception as e:
        print(e)
        registrar_log(str(e), "ERROR")

    # 5. Servicio asesoría válido
    try:
        asesoria = ServicioAsesoria("Python", 80, "Carlos")
        print(asesoria.describir_servicio())
    except Exception as e:
        print(e)
        registrar_log(str(e), "ERROR")

    # 6. Reserva válida
    try:
        r1 = Reserva(c1, sala, 2)
        costo = r1.confirmar_reserva()
        print("Reserva confirmada. Costo:", costo)
    except Exception as e:
        print(e)
        registrar_log(str(e), "ERROR")

    # 7. Reserva inválida
    try:
        r2 = Reserva(c1, sala, -1)
        r2.confirmar_reserva()
    except Exception as e:
        print("Error reserva:", e)
        registrar_log(str(e), "ERROR")

    # 8. Cancelar reserva
    try:
        r1.cancelar_reserva()
        print("Reserva cancelada")
    except Exception as e:
        print(e)
        registrar_log(str(e), "ERROR")

    # 9. Servicio inválido
    try:
        mala_sala = ServicioSala("Sala Mala", 100, -5)
        mala_sala.validar_parametros()
    except Exception as e:
        print("Error servicio:", e)
        registrar_log(str(e), "ERROR")

    # 10. Polimorfismo
    try:
        servicios = [sala, equipo, asesoria]

        for s in servicios:
            print(s.describir_servicio())

    except Exception as e:
        print(e)
        registrar_log(str(e), "ERROR")

    finally:
        registrar_log("Pruebas finalizadas", "INFO")
        print("=== FIN DE PRUEBAS ===")


if __name__ == "__main__":
    ejecutar_pruebas()
