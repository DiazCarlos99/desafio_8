import datetime

class Usuario:
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.username = username
        self.email = email
        self.contraseña = contraseña
        self.fecha_registro = datetime.datetime.now()
        self.avatar = None
        self.estado = "Activo"
        self.online = False

    def login(self, username, contraseña):
        if self.username == username and self.contraseña == contraseña:
            self.online = True
            return True
    
    def registrar(self):
        print('********* El usuario se ha registrado con exito ***********') 