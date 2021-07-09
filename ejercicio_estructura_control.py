# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 07:20:57 2021

@author: sa_si
"""
from tabulate import tabulate


def tipo_cuenta():
    global consignacion_ahorros, consignacion_corriente

    controlador_1 = True

    while controlador_1:

        print('\nTIPO DE CUENTA')
        print('1. Cuenta de ahorros')
        print('2. Cuenta corriente')

        opcion_1 = int(input('Ingresa una opción válida: '))

        while opcion_1 < 1 or opcion_1 > 2:
            opcion_1 = int(input('Ingresa una opción válida: '))

        if opcion_1 == 1:

            consignacion_ahorros = consignacion_ahorros + consignacion

            controlador_1 = False

        elif opcion_1 == 2:

            consignacion_corriente = consignacion_corriente + consignacion

            controlador_1 = False


def tabla():
    global headers
    headers = ['Mes', 'Saldo', 'Intereses', 'Cuota', 'Abono', 'Saldo Final']
    print(tabulate(n_lista, headers,
                   tablefmt="grid", colalign=("center",)))


consignacion = 0.0
retiro = 0.0
disponible = 0.0
c_consignacion = 0.0
c_retiro = 0.0
total_consignacion = 0.0
consignacion_ahorros = 0.0
consignacion_corriente = 0.0
n_clientes = 0
n_clientes_actividad = []
n_clientes_actividad_1 = 0
n_clientes_actividad_2 = 0
n_clientes_actividad_3 = 0
controlador = True
opcion = 0
prestamo = 0
c_prestamo = 0

while controlador:

    tipo_pago = 0
    cuota_fija = 0
    abono_fijo = 0.0
    tasa = 0.0
    mes = 0
    i = 0
    n_lista = []
    interes = 0.0
    cuota_mes = 0.0
    saldo = 0.0
    abono = 0.0
    final_turno = ''
    n_prestamo = 0

    print('\n1. Consignación')
    print('2. Retiro')
    print('3. Préstamo')
    print('4. Finalizar Turno')

    opcion = int(input('Ingresa una opción: '))

    while opcion < 1 or opcion > 4:
        opcion = int(input('Ingresa una opción válida: '))

    if opcion == 1:

        n_clientes_actividad_1 = n_clientes_actividad_1 + 1

        consignacion = float(input('Ingrese el valor de la consignación: '))

        c_consignacion = c_consignacion + consignacion

        disponible = disponible + consignacion

        tipo_cuenta()

        print('\nDinero Disponible:', disponible)

    elif opcion == 2:

        n_clientes_actividad_2 = n_clientes_actividad_2 + 1

        retiro = float(input('Ingresa el valor del retiro: '))

        if disponible >= retiro:

            disponible = disponible - retiro

            c_retiro = c_retiro + retiro

            tipo_cuenta()

            print('\nDinero Disponible:', disponible)

        else:

            print('\nFondos Insuficientes')

    elif opcion == 3:

        n_clientes_actividad_3 = n_clientes_actividad_3 + 1

        prestamo = int(input('\nIngresa el monto del préstamo: '))
        t_prestamo = int(input('Ingresa la cantidad de meses a la que se diferirá las cuotas: '))

        c_prestamo = c_prestamo + prestamo

        if prestamo < 1500000 and t_prestamo < 12:
            tasa = 0.025

        elif prestamo < 1500000 and t_prestamo >= 12:
            tasa = 0.018

        elif (1500000 <= prestamo <= 3000000) and t_prestamo < 12:
            tasa = 0.019

        elif (1500000 <= prestamo <= 3000000) and t_prestamo >= 12:
            tasa = 0.017

        elif prestamo > 3000000:
            tasa = 0.015

        print('\nMODALIDAD DE PAGO')
        print('1. Cuota Fija')
        print('2. Abono Fijo')

        tipo_pago = int(input('Ingresa una opción: '))

        while tipo_pago < 1 or tipo_pago > 2:
            tipo_pago = int(input('Ingresa una opción válida: '))

        if tipo_pago == 1:

            cuota_fija = round(prestamo * ((tasa * (1 + tasa) ** t_prestamo) / (((1 + tasa) ** t_prestamo) - 1)))

            for i in range(1, (t_prestamo + 1)):

                lista = []

                interes = round(prestamo * tasa)
                saldo = round(prestamo + interes - cuota_fija)
                abono = round(cuota_fija - interes)

                if saldo < 0:
                    saldo = 0

                lista = [i, prestamo, interes, cuota_fija, abono, saldo]

                n_lista.append(lista)

                prestamo = saldo

            tabla()

        elif tipo_pago == 2:

            abono_fijo = prestamo / t_prestamo

            for i in range(1, (t_prestamo + 1)):

                lista = []

                interes = round(prestamo * tasa)
                cuota_mes = round(abono_fijo + interes)
                saldo = round(prestamo + interes - cuota_mes)

                if saldo < 0:
                    saldo = 0

                lista = [i, prestamo, interes, cuota_mes, abono_fijo, saldo]

                n_lista.append(lista)

                prestamo = saldo

            tabla()

    while opcion == 4:

        final_turno = str(input('¿Estas seguro de estas opción? Y/N: '))

        while final_turno != 'Y' and final_turno != 'y' and final_turno != 'N' and final_turno != 'n':
            final_turno = str(input('Ingresa una opción correcta Y/N: '))

        if final_turno == 'Y' or final_turno == 'y':

            n_clientes = n_clientes_actividad_1 + n_clientes_actividad_2 + n_clientes_actividad_3

            print('\nConsignaciones Realizadas:', c_consignacion)
            print('Retiros Realizados:', c_retiro)
            print('Prestamos Realizados:', c_prestamo)
            print('Numero de Clientes Totales:', n_clientes)
            print('Número Clientes Consignación:', n_clientes_actividad_1)
            print('Número Clientes Retiro:', n_clientes_actividad_2)
            print('Número Clientes Préstamo:', n_clientes_actividad_3)
            print('\nQue tengas un feliz día, hasta pronto')

            opcion = 0
            controlador = False

        elif final_turno == 'N' or final_turno == 'n':

            opcion = 0
