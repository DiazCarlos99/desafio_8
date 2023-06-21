import datetime
class Comentario:
    def __init__(self, id, id_articulo, id_usuario, contenido,):
        self.__id = id
        self.__id_articulo = id_articulo
        self.__id_usuario = id_usuario
        self.__contenido = contenido
        self.__fecha_hora = datetime.datetime.now()
        self.__estado = True