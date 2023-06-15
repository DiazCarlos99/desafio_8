class Articulo:
    def __init__(self,id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado):
        self.__id = id
        self.__id_usuario = id_usuario
        self.__titulo = titulo
        self.__resumen = resumen
        self.__contenido = contenido
        self.__fecha_publicacion = fecha_publicacion
        self.__imagen = imagen
        self.__estado = estado