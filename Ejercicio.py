# Bucle For
# No Se puede hacer lo mismo que en el whiile
# Es para cuando sabemos el nº de ciclos

#Primer caso
# from imp import cache_from_source
# rang=list(range(5))
# print(rang)
# Segundo caso 
# rang2= list(range(2,10))
# print(rang2)

# print("Inicio bucle For")
# range(5) > [0,1,2,3,4]
# va a hacer dentro del for 5veces
# for i in range(5): #{i=0,i=1,i=2,i=3,i=4}Toma valores de 0 a 5
    # Bloque
    # print(i)
    # print("Hola")
# Fuera del bucle for, por la identación
# print("Fin bucle For")


# Bucle while //////////////////////////*/////////////////
# No se puede hacer lo mismo que en el for siempre
# En el bucle while siempre se pone una condicion

# print("Inicio fuera de while")
# i=0
# si quiero obtener de el 0 al 5 print("Hola while", i)
#  pongo abajo while i<=5
# while i<5:
#     print("Hola while", i)
#     # i+=1
#     i=i+1
# print("Fin fuera while")

# Ejercicio:
# Para este ejercicio no se podria hacer con un bucle FOR

# Validar que el usuario ingrese un numero,
# si ingresa algo que no es un numero imprimir error y
# vuelva a pedir el numero

# Asi daría error,tenemos que hacer cuando sabemos que es un numero
# num=int(input("Ingrese un numero: "))
# Asi bien con while
# num=(input("Ingrese un numero: "))
# Mientras el numero no sea un digito entra al bucle while
# while  not num.isdigit():
#     print("Error ,no ingreso un numero")
#     num=(input("Ingrese un numero: "))
# CUando sale del while vuelvo a convertir a entero
# num=int(num)
# print(type(num))

# print("FIn")

# Ejercicio
# Ingresar 10 notas  guardarlas en una lista al final de ingresar la ultima nota

# En cada ciclo me pide una nota y en cada ciclo lo guarde en una lista y esa lista
# la imprimo al final
# notaL=[]
# for i in range(10):
#     nota=int(input("Ingrese nota: "))
#     notaL.append(nota)
# print(notaL)

# range///////////////////////////////////////////////////
# Una lista de n numeros
# Es como si recorrieramos una lista
# for i in range(4):
#     print(i)

# cadena
# cadena="Ramon"
# print("Inicio")
# for caracter in cadena:
#     print(caracter)
# print("Fin")

# lista
# tiene 5 elementos mi lista se hace 5 veces el bucle for
# Ejemplo1
# lista=[4,5,8,6,7]
# for elemento in lista:
#     print(elemento)
# Ejemplo2
# Recorremos tantas veces como elementos tenga la lista
# lista=["Ramon","Luis","Pepe","Loli","Paco"]
# for elemento in lista:
#     print(elemento)
# Ejemplo3
# Saber los estudiantes que empiezan por la letra A
# lista=["Ramon","Luis","Pepe","Loli","Paco"]
# for nomestudiante in lista:
#     if nomestudiante[0] == "A":
#         print(nomestudiante)

# Ejemplo3
# Wardar en otra lista y luego imprimimos sino queremos implimir en cada ciclo
lista=["Ramon","Luis","Pepe","Loli","Paco"]
cumplen=[]
for nomestudiante in lista:
    if nomestudiante[0] == "R":
        cumplen.append(nomestudiante)
# Cuando recorre toda la lista de estudiantes imprimimos los que empiezan por R 
print(cumplen)

