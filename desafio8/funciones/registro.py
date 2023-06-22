from model.Usuario import Colaborador, Publico
from model.Comentario import Comentario
from module.usuarios import usuarios 
from module.articulos import articulos
from module.comentarios import comentarios





def registrarColaborador():
    print(f'\n ******** Registre su usuario aqui *******')
    id = len(usuarios) + 1
    nombre = input('Ingrese un nombre: ')
    apellido = input('Ingrese un apellido: ')
    telefono = input('Ingrese un telefono: ')
    username = input('Ingrese un nombre de usuario: ')
    email = input('Ingrese un email: ')
    password = input('Ingrese una contraseña: ')

    obj1 = Colaborador(id, nombre, apellido, telefono, username, email, password)

    usuarios.append(obj1)
    obj1.registro()
    print('')
    print('')
    

    

def registrarPublico():
    print(f'\n ******** Registre su usuario aqui *******')
    id = len(usuarios) + 1
    nombre = input('Ingrese un nombre: ')
    apellido = input('Ingrese un apellido: ')
    telefono = input('Ingrese un telefono: ')
    username = input('Ingrese un nombre de usuario: ')
    email = input('Ingrese un email: ')
    password = input('Ingrese una contraseña: ')

    obj1 = Publico(id, nombre, apellido, telefono, username, email, password)

    usuarios.append(obj1)
    obj1.registro()
    print('')
    print('')

    ########En esta seccion unicamente funcones de inicio de sesion######

def iniciarSesion():
    print('')
    print('********* Iniciar sesión **********')
    print('')
    user = input('Ingrese su Usuario: ')
    password = input('Ingrese una contraseña: ')
    if len(usuarios) == 0 :
        print('')
        print('No hay usuarios para iniciar sesión')
        print('Por favor Registrese para iniciar sesión')
        print('')
    
    usuarioActivo = None
    for usuario in usuarios:
        if usuario.get_username() == user:
            usuarioActivo = usuario
            break
    
    if usuarioActivo is not None:
        verificar = usuarioActivo.login(user, password)
        if verificar == True:
            menuUsuaurio(usuarioActivo)
    else:
        print(f'Usuario y/o Contraseña invalidos.')
        iniciarSesion()

#######################En esta seccion vamos a verificar a que instancia pertenece el usuario logueado#####

def menuUsuaurio(usuarioActivo):
        print('')
        print('******* Haz iniciado sesion con exito *******')
        print('')
        print(f'Hola {usuarioActivo.get_username()}')
        while True:
            print('')
            if isinstance(usuarioActivo, Publico):
                print(f'\n ******** Menu principal de usuario Publico *******')
                print('')
                print('\n1- Ver articulos')
                print('2- Ver mis comentarios')
                print('3- Cerrar Sesión')
                opcion = int(input(f'Ingrese una opción: '))

                if opcion == 1:
                    articulosPublicados(usuarioActivo)  
                elif opcion == 2:
                    mostrarComentarios(usuarioActivo)
                else:
                    break
            elif isinstance(usuarioActivo, Colaborador):
                print(f'\n ******** Menu principal de usuario Colaborador *******')
                print('')
                print('\n1- Ver articulos')
                print('2- Crear articulos')
                print('3- Ver mis articulos')
                print('4- Ver mis comentarios')
                print('5- Cerrar Sesión')
                opcion = int(input(f'Ingrese una opción: '))
                idUsuario = usuarioActivo.get_id()
                if opcion == 1:
                    articulosPublicados(usuarioActivo)  
                elif opcion == 2:
                    crearArticulo(usuarioActivo)
                elif opcion == 3:
                    print('')
                    print('***********************')
                    print('Tus Articulos creados')
                    print('***********************')
                    misArticulos(idUsuario)
                elif opcion == 4:
                    mostrarComentarios(usuarioActivo)
                else:
                    break
                

##### En esta seccion vamos a mostrar los articulos publicados
def articulosPublicados(usuarioActivo):
    for articulo in articulos:
        print('')
        print(f'****** Articulo: {articulo.get_id()} ********')
        print('')
        print(f'Titulo: {articulo.get_titulo()}')
        print(f'Resumen: {articulo.get_resumen()}')
        idArticulo = articulo.get_id()
        for comentario in comentarios:
            if comentario.get_idArticulo() == articulo.get_id():
                comentarioId = []
                comentarioId.append(comentario)
                cantidadComentario = len(comentarioId)
                print(f'Comentarios: {cantidadComentario}')
    seleccionarArticulo(usuarioActivo)

def misArticulos(idUsuario):
    for articulo in articulos:
        if articulo.get_idUsuario() == idUsuario:
            print('')
            print(f'****** Articulo: {articulo.get_id()} ********')
            print('')
            print(f'Titulo: {articulo.get_titulo()}')
            print(f'Resumen: {articulo.get_resumen()}')
            idArticulo = articulo.get_id()
            for comentario in comentarios:
                if comentario.get_idArticulo() == articulo.get_id():
                    comentarioId = []
                    comentarioId.append(comentario)
                    cantidadComentario = len(comentarioId)
                    print(f'Comentarios: {cantidadComentario}')
        
    

def seleccionarArticulo(usuarioActivo):
    print('')
    print(f'\n ******** Seleccionar articulo segun su indice *******')
    print('')
    print(f'1- Seleccionar articulo')
    print(f'2- Ir atras')
    opcion = int(input('ingrese una opción: '))

    if opcion == 1:
        id = int(input('¿Que articulo quieres selccionar?: '))
        mostrarArticulo(id)
        crearComentario(usuarioActivo, id)

def mostrarArticulo(id):
    
    for articulo in articulos:
            if articulo.get_id() == id:
                for usuario in usuarios:
                    if usuario.get_id() == articulo.get_idUsuario():
                        print('')
                        print(f'*********** Articulo {articulo.get_id()} ***********')
                        print(f'Articulo creado por el {usuario.get_esColaborador()} {usuario.get_username()}')
                        print('')
                print(f'Titulo: {articulo.get_titulo()}')
                print(f'Contenido: {articulo.get_contenido()}')
                print(f'Fecha de publicacion: {articulo.get_fechaPublicacion()}')
                print('')
                print(f'Estado: {articulo.get_estado()}')
                for comentario in comentarios:
                    print('')
                    if comentario.get_idArticulo() == id:
                        for usuario in usuarios:
                            
                            if usuario.get_id() == comentario.get_idUsuario():
                                print('')
                                print(f'Comentario realizado por {usuario.get_username()}')
                                if isinstance(usuario, Publico):
                                    print('Publico')
                                elif isinstance(usuario, Colaborador):
                                    print('Colaborador')
                                print('')
                        print(f'Contenido: {comentario.get_contenido()}')
                        print(f'Fecha de publicacion: {comentario.get_fechaHora()}')
                        estado = comentario.get_estado()
                        print('')
                        if estado:
                            print(f'Estado: activo')
                            print('')
                        else:
                            print(f'Inactivo')
                            print('')

#Crear comentario
def crearComentario(usuarioActivo, idArticulo):
    print(f'1- Deseas realizar un comentario?: ')
    print(f'2- Ir atras')
    opcion = int(input(f'Seleccionar opción: '))
    if opcion == 1:
        idComentario = len(comentarios) + 1
        comentario = usuarioActivo.comentar(idArticulo, idComentario)
        comentarios.append(comentario)
        mostrarArticulo(idArticulo)
        

#mostrar comentarios
def mostrarComentarios(usuarioActivo):

    idUsuario = usuarioActivo.get_id()
    contador = 0
    for comentario in comentarios:
        if comentario.get_idUsuario() == idUsuario:
            contador += 1
            print('')
            for articulo in articulos:
                if articulo.get_id() == comentario.get_idArticulo():
                    print(f'En el articulo: {articulo.get_titulo()}')
                    print(f'Tienes el comentario: {comentario.get_contenido()}')
                    print(f'A las {comentario.get_fechaHora()}')
    if contador == 0:
        print('')
        print('No tienes comentarios')


#Crear articulos
def crearArticulo(usuarioActivo):
    idArticulo = len(articulos) + 1
    articulo = usuarioActivo.publicar(idArticulo)
    articulos.append(articulo)
    idUsuario = usuarioActivo.get_id
    print('')
    print('Articulo creado con exito')
    mostrarArticulo(idUsuario)
