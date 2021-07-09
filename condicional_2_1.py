opcion = 0
retencion_fuente = 0.0
salud = 0.0
pension = 0.0
arl = 0.0
salario = 0
contrato = ''
nombre = ''
cargo = ''

nombre = str(input('Ingrese el nombre del trabajador: '))
salario = int(input('Ingrese el SMLV: '))

print('\n******CARGOS******')
print('1. Ingeniero')
print('2. Contador')
print('3. Administrativo')
print('4. Gerencia')

opcion = int(input('Ingresa una opción: '))

while (opcion == '' or opcion > 4):
  print('\nERROR, valor inválido')
  opcion = int(input('Ingresa una opción: '))

if (opcion == 1):
  cargo = 'Ingeniero (1)'
  salario = salario * 5
elif (opcion == 2):
  cargo = 'Contador (2)'
  salario = salario * 2
elif (opcion == 3):
  cargo = 'Administrativo (3)'
  salario = salario * 1.5
elif (opcion == 4):
  cargo = 'Gerencia (4)'
  salario = salario * 6
#########################################################################
opcion = 0

print('\n******TIPO DE CONTRATO******')
print('1. Prestación de Servicios')
print('2. Término Fijo')
print('3. Término Indefinido')
print('4. Aprendizaje')

opcion = int(input('Ingresa una opción: '))

while (opcion == '' or opcion > 4):
  print('\nERROR, valor inválido')
  opcion = int(input('Ingresa una opción: '))

if (opcion == 1):
  contrato = 'Prestación de Servicios'
  retencion_fuente = 0.167 * salario
  salud = 0.125 * salario
  pension = 0.16 * salario
  arl = 0 * salario
elif (opcion == 2):
  contrato = 'Término Fijo'
  retencion_fuente = 0.1 * salario
  salud = 0.085 * salario
  pension = 0.12 * salario
  arl = 0.04 * salario
elif (opcion == 3):
  contrato = 'Término Indefinido'
  retencion_fuente = 0.1 * salario
  salud = 0.04 * salario
  pension = 0.04 * salario
  arl = 0.04 * salario
elif (opcion == 4):
  contrato = 'Aprendizaje'
  retencion_fuente = 0 * salario
  salud = 0 * salario
  pension = 0 * salario
  arl = 0.04 * salario

salario_total = salario - retencion_fuente - salud - pension - arl

print('\n******RESULTADOS******')
print('Nombre del trabajador:', nombre)
print('Tipo de contrato:', contrato)
print('Cargo:', cargo)
print('Salario base: $', salario)
print('Descuento por concepto de la retención en la fuente: $', retencion_fuente)
print('Descuento por concepto de salud: $', salud)
print('Descuento por concepto de pensión: $', pension)
print('Descuento por concepto de ARL: $', arl)
print('Salario Total: $', salario_total)