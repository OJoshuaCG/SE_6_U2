import numpy as n

a = n.array([
    [1, 3, 5],
    [2, 4, 6]    
])

# Obtener la transpuesta de una matriz
b = a.T

print(b,'\n')

# b = n.array([
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ])

# Obtener dimension mxn de la matriz
# m -> Fila
# n -> Columna
print(a.shape)
print(b.shape)


# Para realizar la multiplicacion de matrices, la matriz 'a' debe tener las mismas filas (m) con las mismas columnas (n) de 'b', dando como resultado una matriz am X bn
# a x b -> a.dot(b)
multiplicacion = a.dot(b)
print('\n Multiplicacion a•b\n',multiplicacion)


# Obtener la matriz inversa
inversa = n.linalg.inv(multiplicacion)
print('\n Inversa a^-1\n',inversa)

