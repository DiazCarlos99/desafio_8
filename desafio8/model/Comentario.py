import datetime
class Comentario:
    def __init__(self, id, id_articulo, id_usuario, contenido,):
        self.__id = id
        self.__id_articulo = id_articulo
        self.__id_usuario = id_usuario
        self.__contenido = contenido
        self.__fecha_hora = datetime.datetime.now()
        self.__estado = True
        
    def get_id(self):
        return self.__id
    def get_idArticulo(self):
        return self.__id_articulo
    def get_idUsuario(self):
        return self.__id_usuario
    def get_contenido(self):
        return self.__contenido
    def get_fechaHora(self):
        return self.__fecha_hora
    def get_estado(self):
        return self.__estado