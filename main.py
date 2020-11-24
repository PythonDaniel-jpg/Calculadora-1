
print("introduzca la operacion que desea realizar:")



operacion = input()

if operacion == "multiplicacion":
  print("introduzca el primer digito:")
  multi1 = input()
  print("introduzca el segundo digito:")
  multi2 = input()
  resultadoMulti = int(multi2) * int(multi1)
  print(resultadoMulti)

if operacion == "division":
  print("introduzca el primer digito:")
  divi1 = input()
  print("introduzca el segundo digito:")
  divi2 = input()
  resultadoDivi = int(divi2) / int(divi1)
  print(resultadoDivi)
  

if operacion == "suma":

  print("introduzca el primer digito:")
  suma1 = input()
  print("introduzca el segundo digito:")
  suma2 = input()
  resultadoSuma = int(suma2) + int(suma1)
  print(resultadoSuma)

if operacion == "resta":
  print("introduzca el primer digito:")
  resta1 = input()
  print("introduzca el segundo digito:")
  resta2 = input()
  resultadoResta = int(resta2) - int(resta1)
  print(resultadoResta)


