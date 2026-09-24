class ReservaSala:
    def __init__(self, usuario, hora_inicio, tarifa_hora):
        self._usuario = usuario
        self._hora_inicio = hora_inicio
        self._tarifa_hora = tarifa_hora
        self._hora_fin = None

    def registrar_inicio(self, hora_inicio):
        self._hora_inicio = hora_inicio

    def registrar_fin(self, hora_fin):
        self._hora_fin = hora_fin

    def calcular_costo(self, hora_fin):
        horas = hora_fin - self._hora_inicio
        costo = horas * self._tarifa_hora
        return costo

    def obtener_usuario(self):
        return self._usuario

    def obtener_hora_fin(self):
        return self._hora_fin

    def obtener_hora_inicio(self):
        return self._hora_inicio


