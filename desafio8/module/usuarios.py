from model.Usuario import Publico, Colaborador 
usuarios = []

usuario1 = Colaborador(1, "Usuario1", "Apellido1", "123456789", "usuario1", "usuario1@example.com", "contraseña1")
usuario2 = Colaborador(2, "Usuario2", "Apellido2", "987654321", "usuario2", "usuario2@example.com", "contraseña2")
usuario3 = Publico(3, "Usuario3", "Apellido3", "555555555", "usuario3", "usuario3@example.com", "contraseña3")
usuario4 = Publico(4, "Usuario4", "Apellido4", "111111111", "usuario4", "usuario4@example.com", "contraseña4")
usuario5 = Publico(5, "Usuario5", "Apellido5", "999999999", "usuario5", "usuario5@example.com", "contraseña5")

usuarios.append(usuario1)
usuarios.append(usuario2)
usuarios.append(usuario3)
usuarios.append(usuario4)
usuarios.append(usuario5)
