 # program.py
sum = 1 + 2
print(sum)

# Imprimir en consola
print('Hola desde la consola')

# Variables #
sum = 1 + 2 # 3
product = sum * 2
print(product)

# Declaramos la variable
distancia_a_alfa_centauri = 4.367

# Descubrimos su tipo de dato
print(type(distancia_a_alfa_centauri))

# Fechas #

# Importamos la biblioteca 
from datetime import date

# Obtenemos la fecha de hoy
date.today()

# Mostramos la fecha en la consola
print(date.today())

# Conversión de tipo de datos #

print("Today's date is: " + str(date.today()))

# Entrada del usuario #

print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: " + name)

print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(int(first_number) + int(second_number))