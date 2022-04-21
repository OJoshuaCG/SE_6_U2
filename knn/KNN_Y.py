import random

def unpack(nameFile, varSplit):
    file = open(nameFile, "r")
    dataFile = file.read().split("\n")
    file.close()
    dataFile.pop() # Eliminamos el ultimo salto de linea
        
    dataY = [list(map(eval,i.split(varSplit))) for i in dataFile]
   
    return dataY


nameFile = "Instancia_wine.csv"
data = unpack(nameFile, ',')
random.shuffle(data)

pivot = 125

entrenamiento = data[:pivot]
prueba = data[pivot:]

str_entren = str(entrenamiento)
str_entren = str_entren.replace('[', '')
str_entren = str_entren.replace('], ', '\n')
str_entren = str_entren.replace(']]', '\n')

str_prueba = str(prueba)
str_prueba = str_prueba.replace('[', '')
str_prueba = str_prueba.replace('], ', '\n')
str_prueba = str_prueba.replace(']]', '\n')

file = open('ywine_entrenamiento.csv', 'w')
file.write(str_entren)
file.close()

file = open('ywine_prueba.csv', 'w')
file.write(str_prueba)
file.close()