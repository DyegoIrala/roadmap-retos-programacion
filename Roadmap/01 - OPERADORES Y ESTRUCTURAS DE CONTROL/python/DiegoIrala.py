'''/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */'''


#OPERADORES ARITMÉTICOS
num_one = 10
num_two = 5
print(num_one + num_two) #SUM
print(num_one - num_two) #SUBSTRACTION
print(num_one * num_two) #MULTIPLICATION
print(num_one / num_two) #DIVISION
print(num_one ** num_two) #POWER
print(num_one % num_two) #REMAINDER


#OPERADORES DE ASIGNACIÓN
a =  3                  #Asignacion de valor
print(f"El valor de a es : {a}")
incremento = 1
a += incremento         #Incremeto
print(f"Incrementamos a en un valor de {incremento}  : {a}")
decremento = 1
a -= decremento         #Decremento
print(f"Decrementamos a en un valor de {decremento}  : {a}")
multiplicacion = 2
a *= multiplicacion     #Multiplicacion
print(f"Multiplicamos a en un valor de {multiplicacion}  : {a}")
division = 2
a /= division           #Division
print(f"Dividimos a en un valor de {division}  : {a}")
potencia = 2
a **= potencia          #Exponenciacion
print(f"Potenciamos a en un valor de {potencia}  : {a}")
modulo = 2
a %= modulo             #Modulo
print(f"Revisamos el remanente a en un valor de {modulo}  : {a}")




