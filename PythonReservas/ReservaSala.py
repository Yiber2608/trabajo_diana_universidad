class ReservaSala:
    def __init__(self, usuario, hora_inicio, tarifa_hora):
        self.__usuario = usuario
        self.__hora_inicio = hora_inicio
        self.__tarifa_hora = tarifa_hora
        self.__hora_fin = None

    def registrar_inicio(self, hora_inicio):
        self.__hora_inicio = hora_inicio

    def registrar_fin(self, hora_fin):
        self.__hora_fin = hora_fin

    def calcular_costo(self, hora_fin):
        horas = hora_fin - self.__hora_inicio
        costo = horas * self.__tarifa_hora
        return costo

    def obtener_usuario(self):
        return self.__usuario

    def obtener_hora_fin(self):
        return self.__hora_fin

    def obtener_hora_inicio(self):
        return self.__hora_inicio


