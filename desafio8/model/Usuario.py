import datetime
from model.Comentario import Comentario
from model.Articulo import Articulo

class Usuario:
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono
        self.__username = username
        self.__email = email
        self.__contraseña = contraseña
        self.__fecha_registro = datetime.datetime.now()
        self.__avatar = None
        self.__estado = "Activo"
        self.__online = False

    def get_username(self):
        return self.__username
    def get_id(self):
        return self.__id
    def login(self, username, contraseña):
            if self.__username == username and self.__contraseña == contraseña:
                self.__online = True
                return True
            else:
                print('Usuario y/o contraseña erroneas')

    def registro(self):
        print('\n********* El usuario se ha registrado con exito ***********')
        print(f'Nombre: {self.__nombre}')
        print(f'Apellido: {self.__apellido}')
        print(f'Correo: {self.__email}')
        print(f'Usuario: {self.__username}')
        print(f'Contraseña: ********')


class Publico(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña)
        self.__es_publico = True
    def get_esPublico(self):
        return self.__es_publico
    def comentar(self, idArticulo, idComentario):
        contenido = input(f'Ingrese comentario: ')
        idUsuario = self.get_id()
        comentario = Comentario(idComentario, idArticulo, idUsuario, contenido)
        return comentario

    def registro(self):
        super().registro()
        print(f'Usuario: Publico')

class Colaborador(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña)
        self.__es_colaborador = True
    def get_esColaborador(self):
        return self.__es_colaborador

    def publicar(self, idArticulo):
        print('')
        print('*******Creando un Articulo *********')
        print('')
        titulo = input(f'Ingrese un titulo: ')
        resumen = input(f'Resumen del articulo: ')
        contenido = input(f'Contenido: ')
        imagen = input(f'Imagen: ')
        idUsuario = self.get_id()
        articulo = Articulo(idArticulo, idUsuario, titulo, resumen, contenido, imagen)
        return articulo

    def registro(self):
        super().registro()
        print(f'Usuario: Colaborador')

    def comentar(self, idArticulo, idComentario):
        contenido = input(f'Ingrese comentario: ')
        idUsuario = self.get_id()
        comentario = Comentario(idComentario, idArticulo, idUsuario, contenido)
        return comentario
