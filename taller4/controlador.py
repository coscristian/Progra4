import vista as v
import modelo as mdl

def guardarLibro(libro:mdl.Libro) -> None:
    mdl.libros.append(libro)

def crearLibro() -> mdl.Libro:
    nombre = v.leerCadena("Ingrese el nombre del libro: ")
    autor = v.leerCadena("Ingrese el autor del libro: ")
    anioPubl = v.leerCadena("Ingrese el año de publiación del libro: ")
    editorial = v.leerCadena("Ingrese la editorial del libro: ")
    cantPaginas = v.leerCadena("Ingrese la cantidad de páginas del libro: ")
    return mdl.Libro(nombre, autor, anioPubl, editorial, cantPaginas)
    
def seleccionarOpcionLibros(opcion: int) -> None:
    if opcion == 1:
        libro = crearLibro()
        guardarLibro(libro)
        v.mostrarMensaje("Libro creado correctamente")
    elif opcion == 2:
        v.mostrarLibros(mdl.libros)

def crearCasa() -> mdl.Casa:
    pass

def seleccionarOpcionCasas(opcion: int) -> None:
    if opcion == 1:
        crearCasa()
        v.mostrarMensaje("Casa creada correctamente")
    elif opcion == 2:
        v.mostrarCasas(mdl.casas)

def seleccionarEntidad(opcionEntidad: int) -> None:
    if opcionEntidad == 1:
        v.mostrarSubMenuEntidad("Libros")
        opcionSubMenuEntidad = v.leerEntero("¿Qué opción desea seleccionar?: ")
        seleccionarOpcionLibros(opcionSubMenuEntidad)
    elif opcionEntidad == 2:
        v.mostrarSubMenuEntidad("Casas")
        opcionSubMenuEntidad = v.leerEntero("¿Qué opción desea seleccionar?: ")
        seleccionarOpcionCasas(opcionSubMenuEntidad)
        
def ejercicio1() -> str:
    v.mostrarSubMenu()
    opcionEntidad = v.leerEntero("¿Qué entidad desea seleccionar?: ")
    seleccionarEntidad(opcionEntidad)

def seleccionarEjercicio(opcion: int) -> None:
    if opcion == 1:
        ejercicio1()
    elif opcion == 2:
        #ejercicio2()
        pass
    elif opcion == 3:
        #ejercicio3()
        pass
    elif opcion == 4:
        #ejercicio4()
        pass
    elif opcion == 5:
        #ejercicio5()
        pass
    elif opcion == 6:
        #ejercicio6()
        pass

def menuPrincipal():
    opcion = 1
    while opcion != 0:
        v.mostrarMenuPrincipal()
        opcion = v.leerEntero("¿Qué opción desea seleccionar?: ")
        seleccionarEjercicio(opcion)
    v.mostrarMensaje("Saliendo del Sistema...")

def ejecutarPrograma():
    try:
       menuPrincipal()
    except Exception as e:
        v.mostrarMensaje(e)