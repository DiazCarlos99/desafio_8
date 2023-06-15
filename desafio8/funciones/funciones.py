from modulo.Colaborador import Colaborador
from modulo.Publico import Publico

usuarios = []

def registrarUsuario():
    while True:
        print(f'\n ******** Registros de Usuarios *******')
        print('\n1- Registrar un Colaborador')
        print('2- Registrar un Publico')
        print('3- Ir atras')
        print('4- Salir')
        opcion =int(input('ingrese una opción: '))

        if opcion == 1:
            registrarColaborador()
        elif opcion == 2:
            registrarPublico()
        elif opcion == 4:
            print('Hasta luego')
            break
        else:
            print('\n******** Opción invalidad *******')
            print('Ingrese una opción valida')

def registrarColaborador():
    print(f'\n ******** Registre su usuario aqui *******')
    id = len(usuarios) + 1
    nombre = input('Ingrese un nombre: ')
    apellido = input('Ingrese un apellido: ')
    telefono = input('Ingrese un telefono: ')
    username = input('Ingrese un nombre de usuario: ')
    email = input('Ingrese un email: ')
    password = input('Ingrese una contraseña: ')

    obj1 = Colaborador[id, nombre, apellido, telefono, username, email, password]

    usuarios.append(obj1)
    obj1.registrar()
    

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
    obj1.registrar()