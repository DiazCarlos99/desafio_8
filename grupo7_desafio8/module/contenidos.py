from model.modelos import Publico, Colaborador, Comentario, Articulo


usuarios = []
comentarios = []
articulos = []

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



comentario1 = Comentario(1, 1, 1, "Contenido del comentario 1")
comentario2 = Comentario(2, 2, 2, "Contenido del comentario 2")

comentarios.append(comentario1)
comentarios.append(comentario2)



articulo1 = Articulo(1, 1, "Título del artículo 1", "Resumen del artículo 1", "Contenido del artículo 1", "imagen1.jpg")
articulo2 = Articulo(2, 2, "Título del artículo 2", "Resumen del artículo 2", "Contenido del artículo 2", "imagen2.jpg")

articulos.append(articulo1)
articulos.append(articulo2) 