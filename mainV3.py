#Esta primera linea es para indicar

import time

print("Bienvenid@ a la calculadora de Python.")

time.sleep(1)

print("Introduzca la operación que desea relizar: ")


#sirve para que detecte cuando introduzcmos la operacion
operacion = input()

#a partir de aqui empieza la magia

#esto es para la multiplicacion

if operacion == "multiplicacion":
  print("Introduzca el primer digito:")
  multi1 = input()
  print("Introduzca el segundo digito:")
  multi2 = input()
  resultadoMulti = int(multi1) * int(multi2)
  print(resultadoMulti)
#esto es para la division
if operacion == "division":
  print("Introduzca el primer digito:")
  divi1 = input()
  print("Introduzca el segundo digito:")
  divi2 = input()
  resultadoDivi = int(divi1) / int(divi2)
  print(resultadoDivi)
  
#esto es para la suma
if operacion == "suma":

  print("Introduzca el primer digito:")
  suma1 = input()
  print("Introduzca el segundo digito:")
  suma2 = input()
  resultadoSuma = int(suma1) + int(suma2)
  print(resultadoSuma)
#esto es para la resta
if operacion == "resta":
  print("Introduzca el primer digito:")
  resta1 = input()
  print("Introduzca el segundo digito:")
  resta2 = input()
  resultadoResta = int(resta1) - int(resta2)
  print(resultadoResta)


