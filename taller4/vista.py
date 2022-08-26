from modelo import Libro

def mostrarLibros(libros: Libro) -> None:
    cont = 1
    for libro in libros:
        print(f"Libro {cont}")
        print(f"\tNombre:\t {libro.getNombre()}")
        print(f"\tAutor:\t {libro.getAutor()}")
        print(f"\tAño P:\t {libro.getAnioPublicacion()}")
        print(f"\tEditorial:\t {libro.getEditorial()}")
        print(f"\tCant Pag:\t {libro.getCantPaginas()}")
        cont += 1

def mostrarSubMenuEntidad(entidad: str) -> None:
    print(f"1. Crear {entidad}")
    print(f"2. Mostrar {entidad} cread@s")

def mostrarSubMenu() -> None:
    print(".: Ejercicio 1 :.")
    print("0. Salir")
    print("1. Libro")
    print("2. Casa")
    print("3. Película")
    print("4. Bodega")
    print("5. Lámpara")
    print("6. Modem")
    print("7. Router")
    print("8. Maletín")
    print("9. Paciente Oncológico")
    print("10. Gato")

def mostrarMensaje(mensaje = "") -> None:
    print("MENSAJE: ", mensaje) 

def leerEntero(mensaje = "") -> int:
    return int(input(mensaje))

def leerCadena(mensaje = "") -> int:
    return input(mensaje)

def mostrarMenuPrincipal():
    print(".: MENU PRINCIPAL :.")
    print("0. Salir")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    print("5. Ejercicio 5")
    print("6. Ejercicio 6")