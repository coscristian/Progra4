
def ejercicio8():
    lista = []
    for i in range(2):
        lista.append(input("Ingrese una cadena: "))
    cont = 0
    for cadena in lista:
        for caracter in cadena:
            if caracter not in ['a', 'e', 'i','o', 'u'] and caracter != ' ':
                cont += 1
    print(cont)
    
def ejercicio7():
    caracter = input("Ingrese un caracter: ")
    long = int(input("Ingrese la cantidad de la lista: "))
    lista = []
    for i in range(long):
        lista.append(input("Ingrese un número: "))
    
    for cadena in lista:
        if caracter in cadena:
            print(cadena)
            if len(cadena) % 2 == 0:
                print("\tEs par")
            else:
                print("\tEs impar")
                    
def ejercicio6():
    long = int(input("Ingrese la cantidad de la lista: "))
    numero = int(input("Ingrese el numero a verificar: "))
    lista = []
    for i in range(long):
        lista.append(input("Ingrese un número: "))
    
    for cadena in lista:
        if len(cadena) == numero:
            print(cadena)

def ejercicio5():
    long = int(input("Ingrese la cantidad de cadenas: "))
    cadenas = []
    mayor = 0
    menor = 9999
    for i in range(long):
        cadenas.append(input("Ingrese una cadena: "))
        longitud_cadena = len(cadenas[i])
        if longitud_cadena > mayor:
            mayor = longitud_cadena
            pos_mayor = i
        if longitud_cadena < menor:
            menor = longitud_cadena
            pos_menor = i
    print(f"Cadena mayor: {cadenas[pos_mayor]}\n Cadena menor: {cadenas[pos_menor]}")
    
def ejercicio4():
    long = int(input("Ingrese la cantidad de la lista: "))
    lista = []
    for i in range(long):
        lista.append(int(input("Ingrese un número: ")))
    for numero in lista:
        print(f"{numero} - {numero*numero} - {numero*numero*numero}")
    

def ejercicio2():
    asignaturas = []
    for i in range(5):
        asignaturas.append(input("Ingrese un asignaura: "))
    
    for asignatura in asignaturas:
        print(f"Yo estudio {asignatura}")

def ejercicio1():
    asignaturas = []
    for i in range(5):
        asignaturas.append(input("Ingrese un asignaura: "))
    
    for asignatura in asignaturas:
        print(f"{asignatura}")

def elegirOpcion(opcion: int):
  if opcion == 1:
    ejercicio1()
  elif opcion == 2:
    ejercicio2()
  elif opcion == 3:
    #ejercicio3()    
    pass
  elif opcion == 4:
    ejercicio4()
  elif opcion == 5:
    ejercicio5()    
  elif opcion == 6:
    ejercicio6()    
  elif opcion == 7:
    ejercicio7()    
  elif opcion == 8:
    ejercicio8()   

def menuPrincipal():
  opcion = 1
  while(opcion != 0):
    print(".: MENU PRINCIPAL :.")
    print("0. Salir")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("4. Ejercicio 4")
    print("5. Ejercicio 5")
    print("6. Ejercicio 6")
    print("7. Ejercicio 7")
    print("8. Ejercicio 8")
    opcion = int(input("¿Qué opción desea ejecutar?: "))
    elegirOpcion(opcion)
    
  print("MENSAJE: SALIENDO...")

# Principal
def main():
  while(True):
    try:
      menuPrincipal()
      break
    except Exception as err:
      print("MENSAJE: ERROR: ", err)

if __name__ == '__main__':
    main()