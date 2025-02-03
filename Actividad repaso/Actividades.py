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