contagios = 0
contagio_menor = 0

def calculo_cepa_UK():
    return (contagios * 2) + 4

def calculo_cepa_Brasil():
    return (contagios + calculo_cepa_UK())//5

def alerta():
    global valores_contagios
    valores_contagios = [contagios, calculo_cepa_UK(), calculo_cepa_Brasil()]
    contagio_menor = valores_contagios[0]
    

    for x in range(3):
        if valores_contagios[x] < contagio_menor:
            contagio_menor = valores_contagios[x]
    print('Esto es contagio_menor', contagio_menor)
    if (contagio_menor >= 0 and contagio_menor <= 20):
        print('uno')
    elif (contagio_menor >= 21 and contagio_menor <= 30):
        print('dos')
    elif (contagio_menor >= 31 and contagio_menor <= 50):
        print('tres')
    elif (contagio_menor > 50):
        print('cuatro')
        
def main():
    global contagios, valores_contagios
    contagios = int(input('contagios: '));
    print(contagios, calculo_cepa_UK(), calculo_cepa_Brasil())
    alerta()

main()


