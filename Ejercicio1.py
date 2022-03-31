# Implementa un programa que muestre por pantalla
# todos los multiplos de 7 entre 6 y 250 ambos inclusive.
# Range es una funcion,cundo le mandas argumentos separamos por una coma
# Recorro del 6 a 250
# En un for no puedes recorrer una variable de tipo entero,puedes recorrer
# una lista un range que tenga enteros,tambien puedes recorrer strings 
for i in range(6,251):
    # si se cumple es divisible para 7
    if(i%7==0):
        print(i)
# Añadido Y si quiero el producto de los digitos de un numero con un bucle for
# Lo tratamos como si fuera un string,recorres con un for esa cadena y en cada ciclo 
# lo conviertes en entero  y vas multiplicando,vas así como acumulando el producto 
