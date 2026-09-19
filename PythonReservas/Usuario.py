
class Usuario:
    def __init__(self, username, password):
        self.__usuario = username
        self.__password = password

    def validar(self, username_ingresado, password_ingresado):
        if self.__usuario == username_ingresado and self.__password == password_ingresado:
            return True
        else:
            return False
