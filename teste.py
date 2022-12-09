a = ['são paulo', 'minas gerais', 'rio de janeiro']
b = ['sumaré', 'paulinia', 'hortolândia']

lista = {}
for estado in a:
    lista[estado] = []
    for cidade in b:
        lista[estado].append(cidade)


print(lista)