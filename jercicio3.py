# Reaizar un programa que calcule la suma de todos los 
# valores comprendidos entre n y m inclusive,
# donde n y m son numeros enteros que debe introducir
# el usuario por teclado.
n=int(input("Ingrese n: "))
m=int(input("Ingrese m: "))

acum=0
# Numero inclusive +1
for i in range(n,m+1):
    # Se van sumando los numeros entre 1 y 5 
    acum+=i
print(acum)