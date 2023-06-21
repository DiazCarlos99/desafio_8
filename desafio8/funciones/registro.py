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
    if isinstance(usuarioActivo, Publico):
        print('******* Haz iniciado sesion con exito *******')
        print(f'Hola {usuarioActivo.get_username()}')
        while True:
            print(f'\n ******** Que deseas hacer *******')
            print('\n1- Ver articulos')
            print('2- Ver mis comentarios')
            print('3- Cerrar Sesión')
            opcion = int(input(f'Ingrese una opción'))
            
            if opcion == 1:
                articulosPublicados()

##### En esta seccion vamos a mostrar los articulos publicados
def articulosPublicados():
    for articulo in articulos:
        print(f'****** Articulo: {articulo.get_id()} ********')
        print(f'Titulo: {articulo.get_titulo()}')
        print(f'')