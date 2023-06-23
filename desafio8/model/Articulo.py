import datetime

class Articulo:
    def __init__(self,id, id_usuario, titulo, resumen, contenido, imagen):
        self.__id = id
        self.__id_usuario = id_usuario
        self.__titulo = titulo
        self.__resumen = resumen
        self.__contenido = contenido
        self.__imagen = imagen
        self.__estado = True
        self.__fecha_publicacion = datetime.datetime.now()
        
    
    def get_id(self):
        return self.__id
    def get_idUsuario(self):
        return self.__id_usuario
    def get_titulo(self):
        return self.__titulo
    def get_resumen(self):
        return self.__resumen
    def get_contenido(self):
        return self.__contenido
    def get_fechaPublicacion(self):
        return self.__fecha_publicacion
    def get_estado(self):
        return self.__estado