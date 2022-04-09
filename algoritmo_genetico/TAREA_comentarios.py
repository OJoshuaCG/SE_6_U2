import random as rnd # Libreria para generar nums random

# Funcion objetivo, nos permite obtener la suma
# de las caracteristicas (genes) del individuo
def calc_FO(indv):
    return sum(indv)

# numero total de genes (caracteristicas)
tot_genes = 10
# numero total de individuos a generar en un principio
tot_individuos = 100  

# Lista donde almacenaremos la poblacion total
poblacion = []

# Generamos la poblacion inicial con 'tot_individuos' individuos
for i in range(tot_individuos):    
    # Generamos un individuo con 'tot_genes' denominadas con un 0 o 1 aleatoriamente
    individuo = [ rnd.randint(0,1)  for i in range(tot_genes)]    
    # Añadimos el individuo, junto con el resultado de la funcion objetivo
    # el cual vendria siendo la suma de los genes, estos dos anexados en una lista
    poblacion.append([individuo, calc_FO(individuo)])


# Lista de padres, y un total de padres que vamos a generar
padres = []
tot_padres = 50

# Ordenamos la poblacion en base al resultado de la funcion objetivo
# de mayor a menor.

# La funcion 'sort' iterara sobre la lista
# La 'key' a considerar para ordenar sera el valor de lambda
# el valor de lambda sera el valor que se esta iterando en su posicion [1]
# la posicion [1] contamos con el resultado de la funcion objetivo
# el segundo parametro de la funcion 'sort' 
# es para indicar que ordenaremos de mayor a menor
poblacion.sort(key= lambda x:x[1], reverse=True)

# Me quedo con los mejores, que va desde el 0 hasta el 'tot_padres'
# siendo este ultimo, valor excluyente, recordando que fue ordenado previamente
poblacion = poblacion[0:tot_padres]

# Establecemos ahora el valor de total de padres a la mitad del total, 
# para el torneo binario, asi obtendremos la mitad de padres
tot_padres = int(tot_padres/2)
if((tot_padres & 1) == 1):
    tot_padres += 1

# Torneo binario
for i in range(tot_padres):
    # Obtenemos indices aleatorios los cuales seran los padres a competir
    indexPadre1 = rnd.randint(0, tot_padres-1) #aleatorio entre 0 y n-1
    indexPadre2 = rnd.randint(0, tot_padres-1) #aleatorio entre 0 y n-1

    # Si los indices son iguales, cambiamos uno de los 2 hasta que sean diferentes
    while(indexPadre1==indexPadre2):
        indexPadre2 = rnd.randint(0, tot_padres - 1)  # aleatorio entre 0 y n-1

    # Vamos a obtener los genes de los padres resultantes para la 'batalla'
    tempPadre1 = poblacion[indexPadre1][0]
    tempPadre2 = poblacion[indexPadre2][0]

    # Quien en base al funcion objetivo sea mayor o
    # en base a quien tenga los mejores genes, seran padres
    # obteniendo una copia de sus genes
    if calc_FO(tempPadre1) >= calc_FO(tempPadre2):
        padres.append(tempPadre1.copy())
    else:
        padres.append(tempPadre2.copy())

# print("Padres para cruza: ")
# for index, padre in enumerate(padres):
#    print(index,".-", padre)


# Lista donde guardaremos los hijos a crear
hijos = []
# Vamos a iterar sobre los padres de 2 en 2
for i in range(0,tot_padres, 2):
    # Obtenemos el primer y segundo padre (consecutivo a este)
    tempPadre1 = padres[i]
    tempPadre2 = padres[i+1]

    # Generar un aleatorio que nos servira de punto de cruza
    # el cual nos permitira saber hasta donde obtendremos los genes
    # del primer y segundo padre para el hijo 1 y 2
    puntoCruza = rnd.randint(0, tot_genes-1)

    # La primera parte del padre 1, será la primera parte del hijo 1,
    # la segunda parte del padre 1, será la segunda parte del hijo 2

    # La primera parte del padre 2, será la primera parte del hijo 2,
    # la segunda parte del padre 2, será la segunda parte del hijo 1

    puntoCruza += 1  # +1 -> puntoCruza incluyente
    hijo1 = tempPadre1[:puntoCruza] + tempPadre2[puntoCruza:]
    hijo2 = tempPadre2[:puntoCruza] + tempPadre1[puntoCruza:]

    # Añadimos el hijo 1 y 2 a la lista de hijos
    hijos.append([hijo1, 0])
    hijos.append([hijo2, 0])

for i, j in enumerate(hijos):
    print(i, " ", j)

# Mutacion
# Establecemos una probabilidad de mutacion
probMuta = 0.8
# vamos a recorrer nuestro arreglo de hijos
for indexHijo in range(len(hijos)):
    # Creamos una variable apuntando al hijo
    # sobre el que estamos iterando
    hijo = hijos[indexHijo][0]

    # Iteramos sobre sus genes
    for indexGen in range(len(hijo)):
        # Generamos un numero random float entre 0 y 1
        r = rnd.random() # 0 - 1
        # Si el numero random es mayor a la probabilidad de mutar...
        if r >= probMuta:            
            # Se efectua la mutacion
            # Ahora para saber si va a ser un 1 o un 0
            # Generamos otro numero random float entre 0 y 1
            # Si es mayor a un 50%, el valor del gen iterado sera un 1
            # Si no, el valor sera un 0
            # En otras palabras, hay misma probabilidad de "mejorar"
            # como de "empeorar"
            val = 1 if rnd.random() >= 0.5 else 0            

            # Asignamos entre valor en su gen 
            # (reemplazando el que ya tiene (el indice en el que vamos))
            hijo[indexGen] = val            

    # Calculamos la funcion objetivo del hijo ya mutado
    hijos[indexHijo][1] = calc_FO(hijo)


for i, j in enumerate(hijos):
    print(i, " ", j)

