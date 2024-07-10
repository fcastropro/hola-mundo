print("Ejercicio 4")
print("Calculadora básica: Escribe un programa que realice operaciones básicas (suma, resta, multiplicación y división) entre dos números introducidos por el usuario.")
num1=int(input("Por favor ingrese un número: "))
num2=int(input("Por favor ingrese el segundo número: "))
op=""
while op!=0:
  print("Elije una operación basica:\nIngresa 1 para sumar\nIngresa 2 para restar\nIngresa 3 para multiplicar\nIngresa 4 para dividir\nIngresa 0 para salir")
  op=int(input("Ingrese la opción "))
  if op==0:
    break
  elif op==1:
    print(f"La suma de {num1} + {num2} = "+str(num1+num2))
  elif op==2:
    print(f"La resta de {num1} - {num2} = "+str(num1-num2))
  elif op==3:
    print(f"La multiplicación de {num1} x {num2} = "+str(num1*num2))
  elif op==4:
    print(f"La división de {num1} / {num2} = "+str(num1/num2))
     