from modulo.Usuario import Usuario

class Publico(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña)
        self.es_publico = True

    def comentar(self, comentario):
        if self.online:
            return True
        
    def register(self):
        print('********* El usuario se ha registrado con exito ***********') 
    