from modulo.Usuario import Usuario

class Publico(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña)
        self.__es_publico = True

    def comentar(self, comentario):
        if self.__online:
            return True
        
    def registro(self):
        super().registro()
        print(f'funcion: Publico')