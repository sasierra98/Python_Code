lista = ''
entrada = []
registro = []
conteo = []
conteop_ = 0
conteom_ = 0
conteos_ = 0
conteoj_ = 0
conteov_ = 0
conteoi_ = 0
conteoa_ = 0
con = True

try:
    while con:
        conteop = 0
        conteom = 0
        conteos = 0
        conteoj = 0
        conteov = 0
        conteoi = 0
        conteoa = 0
        entrada = []

        entrada.append(str(input('Ingresa inicial de la vacuna: ')))


        for x in entrada:

            if x == 'p':
                conteom_ = 0
                conteos_ = 0
                conteoj_ = 0
                conteov_ = 0
                conteoi_ = 0
                conteoa_ = 0

                conteop = conteop + 1

                if conteop == 1 and conteop_ == 0:
                    conteop_ = conteop_ + 1
                    registro.append('p')
                    conteo.append(conteop_)
                    conteop = 0

                elif conteop_ >= 1 and conteop == 1:
                    conteop_ = conteop_ + 1
                    conteo[registro.__len__() - 1] = conteop_

            elif x == 'j':
                conteom_ = 0
                conteos_ = 0
                conteop_ = 0
                conteov_ = 0
                conteoi_ = 0
                conteoa_ = 0

                conteoj = conteoj + 1

                if conteoj == 1 and conteoj_ == 0:
                    conteoj_ = conteoj_ + 1
                    registro.append('j')
                    conteo.append(conteoj_)
                    conteoj = 0

                elif conteoj_ >= 1 and conteoj == 1:
                    conteoj_ = conteoj_ + 1
                    conteo[registro.__len__() - 1] = conteoj_

            elif x == 'i':
                conteom_ = 0
                conteos_ = 0
                conteoj_ = 0
                conteov_ = 0
                conteop_ = 0
                conteoa_ = 0

                conteoi = conteoi + 1

                if conteoi == 1 and conteoi_ == 0:
                    conteoi_ = conteoi_ + 1
                    registro.append('i')
                    conteo.append(conteoi_)
                    conteoi = 0

                elif conteoi_ >= 1 and conteoi == 1:
                    conteoi_ = conteoi_ + 1
                    conteo[registro.__len__() - 1] = conteoi_

            elif x == 'm':
                conteop_ = 0
                conteos_ = 0
                conteoj_ = 0
                conteov_ = 0
                conteoi_ = 0
                conteoa_ = 0

                conteom = conteom + 1

                if conteom == 1 and conteom_ == 0:
                    conteom_ = conteom_ + 1
                    registro.append('m')
                    conteo.append(conteom_)
                    conteom = 0

                elif conteom_ >= 1 and conteom == 1:
                    conteom_ = conteom_ + 1
                    conteo[registro.__len__() - 1] = conteom_
            elif x == 's':
                conteom_ = 0
                conteop_ = 0
                conteoj_ = 0
                conteov_ = 0
                conteoi_ = 0
                conteoa_ = 0

                conteos = conteos + 1

                if conteos == 1 and conteos_ == 0:
                    conteos_ = conteos_ + 1
                    registro.append('s')
                    conteo.append(conteos_)
                    conteos = 0

                elif conteos_ >= 1 and conteos == 1:
                    conteos_ = conteos_ + 1
                    conteo[registro.__len__() - 1] = conteos_

            elif x == 'v':
                conteom_ = 0
                conteop_ = 0
                conteoj_ = 0
                conteos_ = 0
                conteoi_ = 0
                conteoa_ = 0

                conteov = conteov + 1

                if conteov == 1 and conteov_ == 0:
                    conteov_ = conteov_ + 1
                    registro.append('v')
                    conteo.append(conteov_)
                    conteov = 0

                elif conteov_ >= 1 and conteov == 1:
                    conteov_ = conteov_ + 1
                    conteo[registro.__len__() - 1] = conteov_
            elif x == 'a':
                conteom_ = 0
                conteop_ = 0
                conteoj_ = 0
                conteov_ = 0
                conteoi_ = 0
                conteos_ = 0

                conteoa = conteoa + 1

                if conteoa == 1 and conteoa_ == 0:
                    conteoa_ = conteoa_ + 1
                    registro.append('a')
                    conteo.append(conteoa_)
                    conteoa = 0

                elif conteoa_ >= 1 and conteoa == 1:
                    conteoa_ = conteoa_ + 1
                    conteo[registro.__len__() - 1] = conteoa_

        txtconteo = (str(conteo).replace(',', ''))
        txtconteo = txtconteo.replace("[", "")
        txtconteo = txtconteo.replace("]", "")

        print(" ".join(registro))
        print(txtconteo)

except EOFError as e:
    print(e)
