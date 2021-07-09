team_a = ''
team_b = ''
best_exp = ''
contador_a = 0
contador_b = 0
resultado = []

team_a = str(input('Equipo A, ingresa las herramientas: ')).upper()
team_b = str(input('Equipo B, ingresa las herramientas: ')).upper()
best_exp = str(input('Mejor experiencia de los integrantes: ')).upper()

for x in best_exp:

    if team_a.find(x) >= 0:

        contador_a = contador_a + 1

        print(team_a.find(x))

    else:

        pass

    if team_b.find(x) >= 0:

        contador_b = contador_b + 1

        print(team_b.find(x))

    else:

        pass

    if contador_a > contador_b:

        resultado.append('A')

    elif contador_b > contador_a:

        resultado.append('B')

    elif contador_b == contador_a:

        resultado.append('E')

print(''.join(resultado))
