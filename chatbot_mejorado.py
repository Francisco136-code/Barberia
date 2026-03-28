# chatbot_mejorado.py

class Servicio:
    def __init__(self, nombre, descripcion, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio


class Personal:
    def __init__(self, nombre, posicion, bio):
        self.nombre = nombre
        self.posicion = posicion
        self.bio = bio


class Cita:
    def __init__(self, cliente, servicio, personal, fecha_hora):
        self.cliente = cliente
        self.servicio = servicio
        self.personal = personal
        self.fecha_hora = fecha_hora


class Menu:
    def mostrar_menu(self):
        print("Bienvenido a nuestra barbería!")
        print("1. Servicios")
        print("2. Personal")
        print("3. Citas")
        print("4. Promociones")
        print("5. Calificaciones")
        print("6. Salir")


class Barberia:
    def __init__(self):
        self.servicios = []
        self.personal = []
        self.citas = []
        self.promociones = []
        self.calificaciones = []

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)

    def agregar_personal(self, personal):
        self.personal.append(personal)

    def agendar_cita(self, cita):
        self.citas.append(cita)

    def agregar_promocion(self, promocion):
        self.promociones.append(promocion)

    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)


# Ejemplo de uso
barberia = Barberia()

# Agregar servicios
barberia.agregar_servicio(Servicio("Corte de cabello", "Corte elegante y moderno.", 15))
barberia.agregar_servicio(Servicio("Afeitado", "Afeitado clásico con productos premium.", 10))

# Agregar personal
barberia.agregar_personal(Personal("Juan Pérez", "Barbero", "Con 10 años de experiencia en cortes modernos."))

# Mostrar menú interactivo
menu = Menu()
menu.mostrar_menu()