from modulo.Usuario import Usuario
from funciones.funciones import registrarUsuario

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
