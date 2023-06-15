class Comentario:
    def __init__(self, id, id_articulo, id_usuario, contenido, fecha_hora):
        self.__id = id
        self.__id_articulo = id_articulo
        self.__id_usuario = id_usuario
        self.__contenido = contenido
        self.__fecha_hora = fecha_hora
        self.__estado = True