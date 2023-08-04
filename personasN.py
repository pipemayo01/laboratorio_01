import numpy as np
f = open("persons.txt","r")
lista = [[cordenadas for cordenadas in row.split()[-3:]] for row in f.readlines()[4:]]
f.close()
print(lista)
