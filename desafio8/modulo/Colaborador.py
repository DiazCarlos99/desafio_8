from modulo.Usuario import Usuario

class Colaborador(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña)
        self.__es_colaborador = True
    
    def publicar(self, articulo):
        if self.__online:
            return True

    def registro(self):
        super().registro()
        print(f'funcion: Colaborador')

    def comentar(self, comentario):
        if self.__online:
            return True