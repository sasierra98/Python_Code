import json

b = ''
c = ''
moneda = ''
t_moneda = ''
l_moneda = []
valor = ''
t_valor = ''
l_valor = []
li_valor = []
contador = 0
dicc = {}

# CONVERSION STRING A JSON

b = str(input('Ingresa diccionario: '))

for x in b:
    if x != '{' and x != '}' and x != '"' and x != ':' and x != ',':
        c = c + x

for x in c:
    if x != '0' and x != '1' and x != '2' and x != '3' and x != '4' and x != '5' and x != '6' and x != '7' and x != '8' and x != '9':
        moneda = moneda + x

for i in c:
    if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
        valor = valor + i
    elif i == ' ':
        valor = valor + ' '

for x in moneda:
    if x != " ":
        t_moneda = t_moneda + x
    else:
        l_moneda.append(t_moneda)
        t_moneda = ''

for i in valor:
    contador = contador + 1
    if i != " " and i != "'":
        t_valor = t_valor + i
    else:
        l_valor.append(t_valor)
        t_valor = ''

    if len(valor) == contador:
        l_valor.append(t_valor)
        t_valor = ''

for x in l_moneda:
    if x == '':
        l_moneda.remove('')

for i in l_valor:
    if i == '':
        l_valor.remove('')

for i in l_valor:
    li_valor.append(int(i))

dicc = dict(zip(l_moneda, li_valor))
Json = json.dumps(dicc)

#print(Json)

# {"peso_chileno": 5307, "dolar_canadiense": 9132, "peso_mexicano": 7972, "yuan": 9685, "dolar_australiano": 8346, "real": 4299, "sol": 6769}
# euro libra_esterlina driham rupia sol peso_mexicano dolar_canadiense

#LISTA DE DIVISAS

divisa = ''
t_divisa = ''
l_divisa = []
r_divisa = []
print_divisa = ''
rprint_divisa = ''
contador = 0
suma = 0


divisa = str(input('Ingresa las divisas: '))

for x in divisa:
    contador = contador + 1
    if x != ' ':
        t_divisa = t_divisa + x
    else:
        l_divisa.append(t_divisa)
        t_divisa = ''
    if contador == len(divisa):
        l_divisa.append(t_divisa)

for x in l_divisa:

    for i in dicc.keys():
         if i == x:
             suma = suma + dicc.get(i)
             r_divisa.append(i)

print(suma)

#LIST TO STRING

print_divisa = str(r_divisa)

for x in print_divisa:
    if x != '[' and x != "'" and x != ',' and x != ']':
        rprint_divisa = rprint_divisa + x

print(rprint_divisa)
