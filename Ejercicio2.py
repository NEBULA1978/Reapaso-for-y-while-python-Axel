#  Implementa un programa que muestre por pantalla todos los 
# multiplos de n numeros y m*n,ambos inclusive,
# Donde n y m son los numeros introducidos por el ususario

n=int(input("Ingrese n: "))
m=int(input("Ingrese m: "))
# Le sumo 1 por que me dice que lo inclulla
m=(m*n)+1
# Otra manera
# for i in range(n,(m*n)+1):
for i in range(n,m):
    if(i%n==0):
        # Todos los multiplos de entre 10 y 2 multiplos de 2
        print(i)
    
  