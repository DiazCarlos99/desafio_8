import datetime

class Articulo:
    def __init__(self,id, id_usuario, titulo, resumen, contenido, imagen, estado):
        self.__id = id
        self.__id_usuario = id_usuario
        self.__titulo = titulo
        self.__resumen = resumen
        self.__contenido = contenido
        self.__fecha_publicacion = datetime.datetime.now()
        self.__imagen = imagen
        self.__estado = estado
    
    def get_id(self):
        return self.__id
    def get_titulo(self):
        return self.__titulo