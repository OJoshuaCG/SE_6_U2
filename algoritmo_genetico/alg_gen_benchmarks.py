from benchmarks import trid, schaffer, ellipsoid, quartic, rosenbrock

bench = [trid, schaffer, ellipsoid, quartic, rosenbrock]

def fo(a):
    resultado = bench[4](a)
    return(resultado)

# 42    poblacion.append([vector, calc_fo(vector)])
# 134   hijos[indexHijo][1] = calc_fo(hijo)

def calc_FO(indv):
    return sum(indv)

#m = numero de genes
#tot_genes = 1000
tot_genes = 10

#n  = numero de vectores
#tot_individuos = 120
tot_individuos = 40  #numero de individuos

#tot_padres = 20
tot_padres = 10

tot_it = 100     # Total de iteraciones a crear
probMuta = 0.8  # Probabilidad de Mutacion

# Numero menor y mayor a realizar el rnd
rndMen, rndMay = -10,10


#Poblacion Inicial
import random as rnd
poblacion = []
for i in range(tot_individuos):
    vector = [ rnd.uniform(rndMen,rndMay)  for i in range(tot_genes)]
    ##               vector , FO
    #poblacion.append([vector, calc_FO(vector)])
    poblacion.append([vector, fo(vector)])

#print("Poblacion Inicial: ")
#for indv in poblacion:
#    print(indv)

it = 1
mejorActual = 1000000000
while it <= tot_it:
    print("Iteracion : ", it)
    it+=1

    padres = []
    
    #reverse=True ELIMINADO
    poblacion.sort(key= lambda x:x[1])
    #sorted(poblacion, key= lambda)

    # Cambio de >= a <=
    if poblacion[0][1] <= mejorActual:
        mejorActual = poblacion[0][1]

    #Me quedo con los MejoresPadres
    poblacion = poblacion[0:tot_individuos-tot_padres]
    #poblacion = poblacion[0:tot_padres]    

    ##Seleccion de los padres que seran cruzados
    for i in range(tot_padres):
        indexPadre1 = rnd.randint(0, tot_padres-1) #aleatorio entre 0 y n-1
        indexPadre2 = rnd.randint(0, tot_padres-1) #aleatorio entre 0 y n-1
        while(indexPadre1==indexPadre2):
            indexPadre2 = rnd.randint(0, tot_padres - 1)  # aleatorio entre 0 y n-1

        tempPadre1 = poblacion[indexPadre1]
        tempPadre2 = poblacion[indexPadre2]

        #print(tempPadre1)
        #print(tempPadre2)

        # Cambio de >= a <=
        if tempPadre1[1] <= tempPadre2[1]:
            padres.append(tempPadre1[0].copy())
        else:
            padres.append(tempPadre2[0].copy())


    hijos = []
    for i in range(0,tot_padres, 2):
        tempPadre1 = padres[i]
        tempPadre2 = padres[i+1]

        #Generar un aleatorio
        puntoCruza = rnd.randint(0, tot_genes-1)

        #La primera parte del padre 1, será la primera parte del hijo 1,
        # la segunda parte del padre 1, será la segunda parte del hijo 2

        # La primera parte del padre 2, será la primera parte del hijo 2,
        # la segunda parte del padre 2, será la segunda parte del hijo 1

        # Generar un aleatorio
        puntoCruza += 1  # +1 -> puntoCruza incluyente
        hijo1 = tempPadre1[:puntoCruza] + tempPadre2[puntoCruza:]
        hijo2 = tempPadre2[:puntoCruza] + tempPadre1[puntoCruza:]

        hijos.append([hijo1, 0])
        hijos.append([hijo2, 0])


    #Mutacion    
    for indexHijo in range(len(hijos)):
        hijo = hijos[indexHijo][0]

        for indexGen in range(len(hijo)):
            r = rnd.random() # 0 - 1
            if r >= probMuta:
                #se efectua la mutacion
                val = 0.5 if rnd.random() >= 0.5 else 1
                #print(val)

                hijo[indexGen] *= val

                
        #hijos[indexHijo][1] = calc_FO(hijo)
        hijos[indexHijo][1] = fo(hijo)

    ##poblacion completa
    #mejores individuos + hijos
    poblacion += hijos


    #print("Nueva Poblacion: ")
    #for indv in poblacion:
    #    print(indv)

    print("Mejor Solucion Actual:" , mejorActual)

