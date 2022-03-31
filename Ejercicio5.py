# Escriba un programa que sume los numeros aleatorios de 1 al 5 hasta
# que el total sea al menos 15. Al final imprime los numeros
# aleatorios y el total
# Ejercicios asi no se puede hacer el bucle for,no tengo una cantidad determinada de ciclos


import random as rd
acum=0
aleatorioL=[]
while acum < 15:
    aleatorio=rd.randint(1,5)
    acum+= aleatorio
    aleatorioL.append(aleatorio)
print("Total: ",acum)#Total:  15
print("Lista de aleatrorios:",aleatorioL)#Lista de aleatrorios: [2, 2, 1, 5, 4, 1]

