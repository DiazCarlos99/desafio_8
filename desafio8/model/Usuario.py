import datetime

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

    def login(self, username, contraseña):
            if self.__username == username and self.__contraseña == contraseña:
                self.__online = True
                return True
            else:
                print('Usuario y/o contraseña erroneas')
    
    def registro(self):
        print('********* El usuario se ha registrado con exito ***********') 
        print(f'Nombre: {self.__nombre}')
        print(f'Apellido: {self.__apellido}')
        print(f'Usuario: {self.__username}')
        print(f'Correo: {self.__email}')
        print(f'Contraseña: ********')
        

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
