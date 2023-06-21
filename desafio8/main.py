from funciones.registro import registrarColaborador, registrarPublico, iniciarSesion


def menuInicial():
    while True:
        print('********** Menu Inicial ************')
        print('1- registrar usuario')
        print('2- Iniciar sesión')
        print('3- Salir')
        opcion =int(input('ingrese una opción: '))
    
        if opcion == 1:
            registrarUsuario()
            break
        elif opcion == 2:
            iniciarSesion()
            break
        elif opcion == 3:
            print('Hasta luego')
            break
        else:
            print('\n******** Opción invalidad *******')
            print('Ingrese una opción valida')



def registrarUsuario():
    print(f'\n ******** Registros de Usuarios *******')
    print('\n1- Registrar un Colaborador')
    print('2- Registrar un Publico')
    print('3- Ir atras')
    opcion =int(input('ingrese una opción: '))
    if opcion == 1:
        registrarColaborador()
        menuInicial()
    elif opcion == 2:
        registrarPublico()
        menuInicial()
    elif opcion == 3:
        menuInicial()
    else:
        print('\n******** Opción invalidad *******')
        print('Ingrese una opción valida')
menuInicial()