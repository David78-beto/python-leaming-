#----------------------------------------------------------------------------------
#Actividad 1
#asignacio n 
mensaje_uno = "Esto"
mensaje_uno += " "
mensaje_uno += "es"
mensaje_uno += " "
mensaje_uno += "una"
mensaje_uno += " "
mensaje_uno += "suma"
print (mensaje_uno)
numero_uno = "2"
numero_dor = "5"
numero_uno = int (numero_uno )
numero_dor = int (numero_dor )
resultado = numero_uno + numero_dor 
print ("el resultado de su suma es:"+str(resultado))
#-----------------------------------------------------------------------------------
#Actividad 2 
mensaje_dos = "Mi"
mensaje_dos += " "
mensaje_dos += "Casa"

print (mensaje_dos)
#Estraccion
print (mensaje_dos[0:6])
#sub cadena 
buscar_subcadena = mensaje_dos.find("Casa")
print(buscar_subcadena)
#True
mensaje1 = "Esta es mi casa"
mensaje2 = "Esta es mi casa"
print(mensaje1==mensaje2)
#False 
mensaje3 = "Esta casa es fea"
mensaje4 = "Esta casa es linda"
print(mensaje3==mensaje4)
#----------------------------------------------------------------3/02/2025
#Actividad Repaso
"""hacer una aplicación en la cual me muestre una suma, resta en el siguiente orden y se tiene que comentar todo 

los datos de las suma se escribirán en string  y esto se pasaran a int, esto se tiene que mostrar en pantalla

para la resta se usara la asignación para mostrar en pantalla el texto 

EJEMPLO
 
se tiene que mostrar en pantalla con asignación el siguiente texto "esto es una resta"


Se tiene que hacer dos textos diferentes (dos variables), uno explicando a un cliente como usar una licuadora y otro explicando como usar una plancha, del primer texto se tiene que extraer de la primera silaba a la novena silaba y del segundo tiene que sacarla de la tercera silaba a la octava silaba 

y buscar las palabras licuadora y plancha, tambien compararlos entre si, todo mostrandolo en pantalla y comentandolo"""

#definir 2 variables con string
numero1 = "5"
numero2 = "2"
#cambiarlas a int
numero1 = int(numero1)
numero2 = int(numero2)
#Realizamos la suma de los 2 numeros
resultado_suma = numero1 + numero2
#mostramos el resultado en pantalla
print("El resultado de la suma es: " + str(resultado_suma))
 #definimos el mensaje que aparece con asignacion
mensaje_resta = "Esto"
mensaje_resta += " "
mensaje_resta += "es"
mensaje_resta += " "
mensaje_resta += "una"
mensaje_resta += " "
mensaje_resta += "Resta: "
#concatene el mensaje con la resta y converti de int a string 
print(mensaje_resta + str(numero1 - numero2))
#Definir 2 textos explicativos
mensaje_licuadora1 = "para poder usar una licuadora primero conectamos el cable para que la licuadora tenga energia coloque el ingrediente y oprima el boton para iniciar"
mensaje_plancha = "en la plancha asegure tenerle agua si es de vapor y conectarla a la corriente"
#Extraemos segun lo que necesite el cliente
print (mensaje_licuadora1  [1:9])
print (mensaje_plancha  [3:8])
#mostrar en el terminal la busqueda de la palabra licuadora y plancha
print (mensaje_licuadora1.find("licuadora"))
print (mensaje_plancha.find("plancha"))
#comparar los mensajes de true o false
print (mensaje_licuadora1 == mensaje_plancha)
#----------------------------------------------------------------------------------------------------------6/02/2025
#Repaso
# definir 2 varibles con string
numero3 = "8"
numero4 = "10"
#Cambiarlas a int 
numero3 = int (numero3)
numero4 = int (numero4)
#hacer la opracion 
resultado_multiplicacion = numero3 * numero4
#mandarla a la teriminal 
print ("El resultado de la multiplicacion es: " + str(resultado_multiplicacion))

#asignación mensaje
#hacemos un mensaje con asignacion 
mensaje_hoy = "Hola"
mensaje_hoy += " "
mensaje_hoy += "estamos"
mensaje_hoy += " "
mensaje_hoy += "repasando"
#lo mandadmos a la terminal 
print(mensaje_hoy) 
#hacemos 2 mensajes iguales para que en la comparacion salga TRUE
mensaje_comparacion1 = "Esta esta muy linda"
mensaje_comparacion2 = "Esta esta muy linda"
#lo mandamos ala terminal
print(mensaje_comparacion1 == mensaje_comparacion2) 