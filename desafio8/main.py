from funciones.registro import registrarColaborador, registrarPublico
from funciones.iniciarSesion import iniciarSesion

def menuInicial():
    while True:
        print('1- registrar usuario')
        print('2- Iniciar sesión')
        print('3- Salir')
        opcion =int(input('ingrese una opción: '))
    
        if opcion == 1:
            registrarUsuario()
        elif opcion == 2:
            iniciarSesion()
        elif opcion == 3:
            print('Hasta luego')
            break
        else:
            print('\n******** Opción invalidad *******')
            print('Ingrese una opción valida')



def registrarUsuario():
    while True:
        print(f'\n ******** Registros de Usuarios *******')
        print('\n1- Registrar un Colaborador')
        print('2- Registrar un Publico')
        print('3- Ir atras')
        opcion =int(input('ingrese una opción: '))

        if opcion == 1:
            registrarColaborador()
        elif opcion == 2:
            registrarPublico()
        elif opcion == 3:
            print('')
            print('')
            print('')
            break
        else:
            print('\n******** Opción invalidad *******')
            print('Ingrese una opción valida')

menuInicial()