#################################################################
#                                                               #
#  TUPaD - Programacion I                                       #
#  Alumno: ANDRES BONELLI                                       #
#  Práctico 5: Funciones en Python                              #
#                                                               #
#################################################################

def main():
    while True:
        print("===============================================")
        print("Menu de Ejercicios de funciones")
        print("1. Imprimir Hola Mundo")
        print("2. Saludar Usuario")
        print("3. Informacion Personal")
        print("4. Calcular Area y Perimetro de un Circulo")
        print("5. Segundos a Horas")
        print("6. Tabla de Multiplicar")
        print("7. Operaciones basicas")
        print("8. Calcular IMC")
        print("9. Convertir Celsius a Fahrenheit")
        print("10. Calcular Promedio")
        print("0. Salir")
        opcion = input("Ingrese una opcion: ")
        match opcion:
            case "1":
                imprimir_hola_mundo()
            case "2":
                print(saludar_usuario(input("Ingrese su nombre: ")))
            case "3":
                nombre = input("Ingrese su nombre: ")
                apellido = input("Ingrese su apellido: ")
                edad = ingresar_numero("Ingrese su edad: ", 1, 100)
                residencia = input("Ingrese su residencia: ")
                informacion_personal(nombre, apellido, edad, residencia)
            case "4":
                radio = ingresar_numero("Ingrese el radio del circulo: ", 1, decimal=True)
                print(f"El area del circulo es: {calcular_area_circulo(radio)}")
                print(f"El perimetro del circulo es: {calcular_perimetro_circulo(radio)}")
            case "5":
                segundos = ingresar_numero("Ingrese la cantidad de segundos: ", 1, decimal=True)
                print(f"La cantidad de horas es: {segundos_a_horas(segundos)}")
            case "6":
                numero = ingresar_numero("Ingrese un numero: ", 1)
                for i in range(1, 11):
                    print(f"{numero} x {i} = {numero * i}")
            case "7":
                numero1 = ingresar_numero("Ingrese un numero: ", decimal=True)
                numero2 = ingresar_numero("Ingrese otro numero: ", decimal=True)
                suma, resta, multiplicacion, division = operaciones_basicas(numero1, numero2)
                print(f"La suma de los numeros es: {suma}")
                print(f"La resta de los numeros es: {resta}")
                print(f"La multiplicacion de los numeros es: {multiplicacion}")
                print(f"La division de los numeros es: {division}")
            case "8":
                altura = ingresar_numero("Ingrese su altura en metros: ", 0.01, decimal=True)
                peso = ingresar_numero("Ingrese su peso en kg: ", 1, decimal=True)
                imc = peso / altura ** 2
                print(f"Su indice de masa corporal es: {round(imc, 2)}")
            case "9":
                temperatura = ingresar_numero("Ingrese la temperatura en grados Celsius: ", -273.15, decimal=True)
                fahrenheit = (9 / 5) * temperatura + 32
                print(f"La temperatura en grados Fahrenheit es: {round(fahrenheit, 2)}")
            case "10":
                numero1 = ingresar_numero("Ingrese el primer numero: ", 1)
                numero2 = ingresar_numero("Ingrese el segundo numero: ", 1)
                numero3 = ingresar_numero("Ingrese el tercer numero: ", 1)
                print(f"El promedio de los numeros es: {calcular_promedio(numero1,numero2,numero3)}")
            case "0":
                break
            case _:
                print("Opcion incorrecta")


"""
1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal.
"""
def imprimir_hola_mundo():
    print("Hola Mundo!")

"""
2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario.
"""
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

"""
3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
"""
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

"""
4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
"""
def calcular_area_circulo(radio):
    return 3.14 * radio ** 2
def calcular_perimetro_circulo(radio):
    return 2 * 3.14 * radio

"""
5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
"""
def segundos_a_horas(segundos):
    return segundos / 3600

"""
6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función.
"""
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

"""
7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
"""
def operaciones_basicas(a, b):
    return a + b, a - b, a * b, a / b if b != 0 else "No se puede dividir por cero"

"""
8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
"""
def calcular_imc(peso, altura):
    return peso / altura ** 2

"""
9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.
"""
def celsius_a_fahrenheit(celsius):
    return (9 / 5) * celsius + 32

"""
10. Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
"""
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Funciones auxiliares:
def ingresar_numero(mensaje, minimo = float("-inf"), maximo = float("inf"), decimal = False):
    while True:
        try:
            numero = float(input(mensaje)) if decimal else int(input(mensaje))
            if numero < minimo or numero > maximo:
                raise ValueError
            break
        except ValueError:
            print(f"Error: Numero no valido")
    return numero

if __name__ == "__main__":
    main()

