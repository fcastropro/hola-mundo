print("Ejercicio 11")
print("Sumar números hasta un límite: Escribe un programa que sume todos los números naturales hasta un número límite introducido por el usuario")
num=int(input("Ingrese un número: "))
suma=0
for i in range(1,num+1):
  suma+=i
print(f"La suma es: {suma}")