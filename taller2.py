
def elegirOpcion(opcion: int):
  if opcion == 1:
    ejercicio1()
  elif opcion == 2:
    ejercicio2()
  elif opcion == 3:
    ejercicio3()    
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
  elif opcion == 9:
    ejercicio9()    
  elif opcion == 10:
    ejercicio10()    
  elif opcion == 11:
    ejercicio11()    
  elif opcion == 12:
    ejercicio12()    
  elif opcion == 13:
    ejercicio13()    
  elif opcion == 14:
    ejercicio14()    
  elif opcion == 15:
    ejercicio15()    

def menuPrincipal():
  opcion = 1
  while(opcion != 0):
    print(".: MENU PRINCIPAL :.")
    print("0. Salir")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    print("5. Ejercicio 5")
    print("6. Ejercicio 6")
    print("7. Ejercicio 7")
    print("8. Ejercicio 8")
    print("9. Ejercicio 9")
    print("10. Ejercicio 10")
    print("11  Ejercicio 11")
    print("12. Ejercicio 12")
    print("13. Ejercicio 13")
    print("14. Ejercicio 14")
    print("15. Ejercicio 15")
    opcion = int(input("¿Qué opción desea ejecutar?: "))
    elegirOpcion(opcion)
    
  print("MENSAJE: SALIENDO...")

#Ejercicios
  
#Ejercicio 1
def ejercicio1():
  num1 = float(input("Ingrese un numero decimal: "))
  num2 = int(input("Ingrese un número entero: "))
  suma = num1 + num2
  print("El resultado de la suma es: ", suma)

#Ejercicio 2
def ejercicio2():
  num1 = int(input("Ingrese un número entero: "))
  num2 = int(input("Ingrese otro número entero: "))
  suma = num1 + num2
  print("Suma: ", suma)
  num3 = int(input("Ingrese otro número entero: "))
  print("Multiplicación: ", num3 * suma)

#Ejercicio 3
def ejercicio3():
  valor = float(input("Ingrese un valor: "))
  descuento = float(input("Ingrese el porcentaje de descuento: "))

  valorConDescuento = valor - (valor * (descuento / 100))
  print(f"Descontando el {descuento}% el valor queda {int(valorConDescuento)}")  

#Ejercicio 4
def ejercicio4():
    num1 = int(input("Ingrese un numero entero: "))
    num2 = int(input("Ingrese otro numero entero: "))
    num3 = int(input("Ingrese otro numero entero: "))
    print("El númeor mayor es: ", mayor(mayor(num1, num2), num3))

def mayor(a:int, b:int):
    return a if a > b else b

#Ejercicio 5
def ejercicio5():
    cadena = input("Ingrese una cadena: ")
    print("Cantidad de caracteres de la cadena es impar: ", len(cadena) % 2 != 0)

#Ejercicio 6
def ejercicio6():
    cad1 = input("Ingrese una cadena: ")
    cad2 = input("Ingrese otra cadena: ")
    print("La primera cadena es menor que la segunda: ", len(cad1) < len(cad2))

#Ejercicio 7
def ejercicio7():
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    print("El menor de los dos numeros es: ", num1 if num1 < num2 else num2)

#Ejercicio 8
def ejercicio8():
    nombre = input("Ingrese el nombre: ")
    contraseña = input("Ingrese la contraseña: ")
    if (nombre == "UTP" and contraseña == "utp123"):
        print("Usuario y contraseña correcto")
    else:
        print("Acceso denegado")

#Ejercicio 9
def ejercicio9():
    for i in range(100, 49, -1):
        if i != 50:
            print(i, end=" - ")
        else:
            print(i)    

#Ejercicio 10
def ejercicio10():
    for i in range(0, 29, 4):
        if i != 28:
            print(i, end="-")
        else:
            print(i)

#Ejercicio 11
def ejercicio11():
    for i in range(100, 200, 1):
        if i != 199:
            print(i, end="-")
        else:
            print(i)

#Ejercicio 12
def ejercicio12():
    num = int(input("Ingrese un número: "))
    for i in range(num, num * 2 + 1, 1):
        if i != num * 2:
            print(i, end="-")
        else:
            print(i)

#Ejercicio 13
def ejercicio13():
    frase = input("Ingrese una frase: ")
    vocales = ['a', 'e', 'i', 'o', 'u']
    vocalesEnFrase = [vocal for vocal in vocales if vocal in frase.lower()]
    print("La cantidad de vocales que hay en la frase es: ", len(vocalesEnFrase))

#Ejercicio 14
def ejercicio14():
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    elementos = [i for i in range(num1, num2 + 1, 1)]
    print("La sumatoria de los numeros desde ", num1, " hasta ", num2, " es ", sum(elementos))

#Ejercicio 15
def ejercicio15():
    num = int(input("Ingrese la altura del triangulo rectangulo: "))
    for i in range(1, num + 1, 1):
        print("*" * i)
    #for linea in range(num+1):
    #    for simbolo in range(linea):
    #        print("*", end="")
    #    print("")

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
