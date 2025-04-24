class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro {self.titulo} ha sido prestado")
        else:
            print(f"El libro {self.titulo} no esta disponible")

    def devolver_libro(self):
        self.disponible = True
        print(f"El libro {self.titulo} ha sido devuelto")


class Usuario:
    def __init__(self, usuario, id):
        self.usuario = usuario
        self.id = id
        self.libros_prestados = []

    def prestar_libro(self, libro):
        if libro.disponible:
            libro.prestar()
            self.libros_prestados.append(libro)
        else:
            print(f"El libro {libro.titulo} no esta disponible")

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.devolver_libro()
            self.libros_prestados.remove(libro)
        else:
            print(f"El libro {libro.titulo} no esta en la lista de prestados")


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"El libro {libro.titulo} ha sido agregado")

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"El usuario {usuario.usuario} ha sido registrado")

    def mostrar_libros_disponibles(self):
        print("Los libros diponibles son:")
        for libro in self.libros:
            if libro.disponible:
                print(f"{libro.titulo} por {libro.autor}")


libro1 = Libro("Cien años de soledad", "Gabriel Garcia Marquez")
libro2 = Libro("1984", "George Orwell")

usuario1 = Usuario("Elkin", "001")
biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.registrar_usuario(usuario1)

biblioteca.mostrar_libros_disponibles()

usuario1.prestar_libro(libro1)

biblioteca.mostrar_libros_disponibles()

usuario1.devolver_libro(libro1)

biblioteca.mostrar_libros_disponibles()
