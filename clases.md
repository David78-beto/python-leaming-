
Clase 1
Actividad 1
En Python no se utiliza el punto y coma (;).

Compilador vs. Intérprete
Compilador: Es un programa que traduce el código fuente de un lenguaje de programación a código máquina para que la computadora lo ejecute.
Intérprete: Es un programa que traduce y ejecuta el código fuente línea por línea, sin generar un archivo de código máquina.
Actividad 2: Variables
Una variable es un espacio en la memoria donde se almacenan datos que un programa puede utilizar y recuperar.

Reglas para nombrar variables:
Cada variable debe tener un nombre único para poder identificarse.
No puede tener espacios en blanco (por ejemplo, nombre_completo en lugar de nom bre).
No puede utilizar nombres reservados de Python como print, if, while, etc.
Tipos de datos comunes en variables:
String (str): Almacena texto y siempre se encuentra entre comillas ("texto" o 'texto').
Enteros (int): Almacenan números enteros (ejemplo: 10, -5).
Flotantes (float): Almacenan números decimales (ejemplo: 3.14, -2.5).
📌 Nota: Siempre que se usan comillas ("" o ''), el valor se considera un String.
#---------------------------------------------------------------------------------------------------------------------------------------------------------
Clase 2: Manipulación de Cadenas (Strings)
Un String es una serie de caracteres que pueden incluir letras, números, signos y símbolos. En Python, existen diversas operaciones para manipularlos.

Actividad 1: Asignación de Strings
La asignación de cadenas consiste en almacenar texto dentro de una variable. También se pueden modificar usando +=.

python
Copiar
Editar
mensaje = "Hola"
mensaje += " "  # Agrega un espacio en blanco
mensaje += "David"

print(mensaje)  # Salida: Hola David

Concatenación de Cadenas
La concatenación consiste en unir dos o más cadenas para formar una más grande. Se utiliza el operador +.

Ejemplo de Concatenación
python
Copiar
Editar
numero_uno = 4
numero_dos = 6
resultado = numero_uno + numero_dos  # Resultado: 10
resultado = str(resultado)  # Convertimos el número a String

print("El resultado de la suma es: " + resultado)
📌 Nota: Para convertir un String a Entero, usamos int().

python
Copiar
Editar
numero_uno = int(numero_uno)  # Convierte a entero

Búsqueda en Cadenas
La búsqueda consiste en localizar una palabra o un carácter dentro de una cadena.

Extracción de Subcadenas
La extracción permite obtener una parte de una cadena según su posición. Se usa la notación [inicio:fin].

Ejemplo:

python
Copiar
Editar
cadena = "Python es increíble"
subcadena = cadena[0:6]  # Extrae "Python"
print(subcadena)

Comparación de Cadenas
Se utiliza para comparar dos cadenas de texto con el operador ==.

Ejemplo:

python
Copiar
Editar
cadena1 = "Hola"
cadena2 = "Hola"

print(cadena1 == cadena2)  # Devuelve True si son iguales, False si no lo son

#---------------------------------------------------------------------------------------------------------------
