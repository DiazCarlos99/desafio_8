from modulo.Colaborador import Colaborador
from modulo.Publico import Publico


usuarios = []

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

    ########En esta seccion unicamente funcones de inicio de sesion######