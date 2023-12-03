str = "abcdacbdb"

lista = []

for i in range(0,len(str)-1):
    lista.append(str[i:i+2])

lista.sort()    
print(lista)