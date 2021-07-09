def cal_grado_peligrosidad():
    global grado_peligrosidad
    grado_peligrosidad = C * E * P 

    if (grado_peligrosidad <= 350):
        interpretacion = 'Bajo'
    elif (grado_peligrosidad > 350 and grado_peligrosidad <= 650):
        interpretacion = 'Medio'
    elif (grado_peligrosidad > 650):
        interpretacion = 'Alto'

    print('\nGrado de peligrosidad:', grado_peligrosidad, 'Interpretación:', interpretacion)

def cal_factor_ponderacion():
    global factor_ponderacion
    if (porcentaje_expuestos <= 21):
        factor_ponderacion = 1
    elif (porcentaje_expuestos > 21 and porcentaje_expuestos <= 41):
        factor_ponderacion = 2
    elif (porcentaje_expuestos > 41 and porcentaje_expuestos <= 61):
        factor_ponderacion = 3
    elif (porcentaje_expuestos > 61 and porcentaje_expuestos <= 81):
        factor_ponderacion = 4
    elif (porcentaje_expuestos > 81):
        factor_ponderacion = 5

    print('Factor de ponderación:', factor_ponderacion)

def cal_grado_repercusion():
    grado_repercusion = grado_peligrosidad * factor_ponderacion
    
    if (grado_repercusion <= 1000):
        interpretacion = 'Bajo'
    elif (grado_repercusion > 1000 and grado_repercusion <= 3000):
        interpretacion = 'Medio'
    elif (grado_repercusion > 3000):
        interpretacion = 'Alto'

    print('Grado de Repercusión:', grado_repercusion, 'Interpretación:', interpretacion)

C = 0.0
E = 0.0
P = 0.0
grado_peligrosidad = 0.0
grado_repercusion = 0.0
porcentaje_expuestos = 0.0
Ntrabajadores_expuestos = 0
total_trabajadores = 0
factor_ponderacion = 0
interpretacion = ''

C = float(input('Ingresa el valor de Consecuencia: '))
E = float(input('Ingresa el valor de Exposición: '))
P = float(input('Ingresa el valoe de Probabilidad: '))
Ntrabajadores_expuestos = int(input('Ingresa el número de trabajadores expuesto: '))
total_trabajadores = int(input('Ingresa el numero total de todos los trabajadores: '))

porcentaje_expuestos = (Ntrabajadores_expuestos / total_trabajadores) * 100

cal_grado_peligrosidad()
print('Porcentaje de Expuestos:', porcentaje_expuestos)
cal_factor_ponderacion()
cal_grado_repercusion()