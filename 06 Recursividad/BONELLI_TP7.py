#################################################################
#                                                               #
#  TUPaD - Programacion I                                       #
#  Alumno: ANDRES BONELLI                                       #
#  Práctico 11: Aplicacion de la Recursividad                   #
#                                                               #
#################################################################

"""
1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario.
"""
def factorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

# Ejemplo de uso:
numero = int(input("Ingrese un número entero: "))
for i in range(1, numero + 1):
    print(f"El factorial de {i} es: {factorial_recursivo(i)}")

"""
2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique.
"""
def fibonacci_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def fibonacci_recursivo_muestra_serie(n, actual=0, siguiente=1, contador=0, serie=None):
    # Inicio
    if serie is None:
        serie = []
    # Caso base (corta la funcion y retorna la serie completa)
    if contador > n:
        return serie
    # Añado un termino a la serie y lo paso a la funcion recursiva
    serie.append(actual)
    return fibonacci_recursivo_muestra_serie(n, siguiente, actual + siguiente, contador + 1, serie)

# Ejemplo de uso:
numero = int(input("Ingrese un número entero: "))
print(f"Serie de Fibonacci completa hasta la posiciòn {numero}:")
print(fibonacci_recursivo_muestra_serie(numero))


"""
3) Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula n^m = n * n^(m-1). Prueba esta función en un
algoritmo general.
"""
def potencia_recursiva(n, m):
    if m == 0:
        return 1
    else:
        return n * potencia_recursiva(n, m - 1)
# Ejemplo de uso:
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
resultado = potencia_recursiva(base, exponente)
print(f"{base} elevado a la {exponente} es igual a: {resultado}")

"""
4) Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.
Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este
procedimiento:
1. Dividir el número por 2.
2. Guardar el resto (0 o 1).
3. Repetir el proceso con el cociente hasta que llegue a 0.
4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.
Ejemplo:
Convertir el número 10 a binario:
10 ÷ 2 = 5 resto: 0
5 ÷ 2 = 2 resto: 1
2 ÷ 2 = 1 resto: 0
1 ÷ 2 = 0 resto: 1
Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010".
"""
def decimal_a_binario_recursivo(numero):
    if numero == 0:
        return "0"
    elif numero == 1:
        return "1"
    else:
        return decimal_a_binario_recursivo(numero // 2) + str(numero % 2)
# Ejemplo de uso:
numero = int(input("Ingrese un número entero positivo: "))
binario = decimal_a_binario_recursivo(numero)
print(f"El número {numero} en binario es: {binario}")


"""
5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
Requisitos:
- La solución debe ser recursiva.
- No se debe usar [::-1] ni la función reversed().
"""
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    else:
        if palabra[0] == palabra[-1]:
            return es_palindromo(palabra[1:-1])
        else:
            return False

# Ejemplo de uso:
palabra = input("Ingrese una palabra: ")
# eliminar espacios en caso que se ingrese una frase
palabra = palabra.lower().replace(" ", "")
print(f"{palabra}{" no" if not es_palindromo(palabra) else ""} es un palíndromo")

"""
6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
Restricciones:
- No se puede convertir el número a string.
- Usá operaciones matemáticas (%, //) y recursión.
Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5)
"""
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

# Ejemplo de uso:
numero = int(input("Ingrese un número entero positivo: "))
resultado = suma_digitos(numero)
print(f"La suma de los dígitos de {numero} es: {resultado}")

"""
7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.
Ejemplos:
contar_bloques(1) → 1 (1)
contar_bloques(2) → 3 (2 + 1)
contar_bloques(4) → 10 (4 + 3 + 2 + 1)
"""
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

# Ejemplo de uso:
numero = int(input("Ingrese el número de bloques en el nivel más bajo: "))
resultado = contar_bloques(numero)
print(f"Para construir una pirámide con base {numero}, se necesitan {resultado} bloques.")

"""
8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
Ejemplos:
contar_digito(12233421, 2) → 3
contar_digito(5555, 5) → 4
contar_digito(123456, 7) → 0
"""
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)
# Ejemplo de uso:
numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese un dígito (entre 0 y 9): "))
resultado = contar_digito(numero, digito)
print(f"El dígito {digito} aparece {resultado} veces en el número {numero}.")