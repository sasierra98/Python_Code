Producto = input('Ingresa el nombre del producto: ')
CU = int(input('Costo Unitario: '))
PVP = int(input('PVP: '))
UD = int(input('Unidades Disponibles: '))
Ganancia = ((UD * PVP) - (UD * CU))

print('Producto: ' , Producto)
print('CU: $' , CU)
print('PVP: $' , PVP)
print('Unidades Disponibles:' , UD)
print('Ganancia: $' , Ganancia)

