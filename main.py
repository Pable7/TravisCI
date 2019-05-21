
archivo = open('./Data/nacimientos.txt', mode='r', encoding='UTF-8')
data = archivo.readline()
data = data.split("'], ['")
aux = []
for i in data:
    if i[0] == ' ':
        i = i[1:]
    i = i.replace("[['", '')
    i = i.replace("']]", '')
    i = i.replace("' ", "'")
    i = i.split("', '")
    aux.append(i)
archivo.close
archivo = open('./Data/cabecera.txt', mode='r', encoding='UTF-8')
cabecera = archivo.readline()
cabecera = cabecera.replace("['", '')
cabecera = cabecera.replace("']", '')
cabecera = cabecera.split("', '")
archivo.close()
archivo = open('./Data/seleccion.txt', mode='r', encoding='UTF-8')
seleccion = archivo.readline()
seleccion = seleccion.replace("['", '')
seleccion = seleccion.replace("']", '')
seleccion = seleccion.split("', '")
archivo.close()

final = []
for i in aux:
    final.append([])
for i in seleccion:
    for j in range(len(cabecera)):
        if i == cabecera[j]:
            for k in range(len(aux)):
                final[k].append(aux[k][j])
print(final)