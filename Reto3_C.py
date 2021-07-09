lista = ''
entrada = []
entrada1 = entrada
registro = []
conteo = []
conteop = 0
conteom = 0
conteos = 0
conteoj = 0
conteov = 0
conteoi = 0
conteoa = 0
opcion = 0


opcion = int(input('Ingresa el número de vacunas: '))

for x in range(opcion):
    entrada.append(str(input('Ingresa inicial de la vacuna: ')))

entrada1.append('')

for x in entrada1:
    if x == 'p':
        conteop = conteop + 1
    else:
        if conteop > 0:
            registro.append('p')
            conteo.append(conteop)
            conteop = 0
    if x == 'j':
        conteoj = conteoj + 1
    else:
        if conteoj > 0:
            registro.append('j')
            conteo.append(conteoj)
            conteoj = 0
    if x == 'i':
        conteoi = conteoi + 1
    else:
        if conteoi > 0:
            registro.append('i')
            conteo.append(conteoi)
            conteoi = 0
    if x == 'm':
        conteom = conteom + 1
    else:
        if conteom > 0:
            registro.append('m')
            conteo.append(conteom)
            conteom = 0
    if x == 's':
        conteos = conteos + 1
    else:
        if conteos > 0:
            registro.append('s')
            conteo.append(conteos)
            conteos = 0
    if x == 'v':
        conteov = conteov + 1
    else:
        if conteov > 0:
            registro.append('v')
            conteo.append(conteov)
            conteov = 0
    if x == 'a':
        conteoa = conteoa + 1
    else:
        if conteoa > 0:
            registro.append('a')
            conteo.append(conteoa)
            conteoa = 0

entrada1.remove('')

txtconteo = (str(conteo).replace(',', ''))
txtconteo = txtconteo.replace("[", "")
txtconteo = txtconteo.replace("]", "")

print(" ".join(registro))
print(txtconteo)
