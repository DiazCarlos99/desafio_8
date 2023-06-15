from modulo.Usuario import Usuario

class Colaborador(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña)
        self.es_colaborador = True
    
    def publicar(self, articulo):
        if self.online:
            return True

    def registrar(self):
            print('********* El usuario se ha registrado con exito ***********') 

    def comentar(self, comentario):
        if self.online:
            return True