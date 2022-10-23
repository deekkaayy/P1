def limpa_texto(texto):
    texto = ' '.join(texto.split())  # Juntar vários espaços
    texto = texto.replace('\t', '')  # Substituição dos caracteres brancos
    texto = texto.replace('\n', '')
    texto = texto.replace('\v', '')
    texto = texto.replace('\f', '')
    texto = texto.replace('\r', '')
    return texto


def corta_texto(texto, numero):
    if len(limpa_texto(texto)) > numero:
        texto1 = texto[:numero]  # Primeiro string com o numero de caracteres
        texto2 = texto[numero:]  # Segundo string com o resto dos caracteres\
        if texto1.count(' ') != 0:
            texto1 = texto[:texto1.rindex(' ')]
            texto2 = texto[len(texto1) + 1:]
            return texto1, texto2
        elif texto1.count(' ') == 0:
            texto1 = ''
            texto2 = texto
            return texto1, texto2
        else:
            return texto1, texto2
    else:
        texto1 = texto
        texto2 = ' '
        return texto1, texto2


def insere_espacos(texto, numero):
    texto = limpa_texto(texto)
    i = 0
    while len(texto) < numero:
        if i == len(texto):
            i = 0
        elif texto[i] == ' ' and texto[i + 1] != ' ':
            texto = texto[:i] + ' ' + texto[i:]
            i += 2
        else:
            i += 1
    return texto


def justifica_texto(texto, numero):
    if type(texto) != str or type(numero) != int:
        raise ValueError('argumentos invalidos')
    texto = limpa_texto(texto)
    k = 0
    txt = list(corta_texto(texto, numero) for i in
               range(0, len(texto), numero))  # "Tuplificar" o texto com indice do numero introduzido
    for i in range(len(txt)):
        txt[i] = corta_texto(texto[k:], numero)[0]
        k += len(txt[i])
    for i in range(len(txt)):
        txt[i] = insere_espacos(txt[i], numero)
    txt[-1] = limpa_texto(txt[-1])
    while len(txt[-1]) < numero:
        txt[-1] += ' '
    txt = tuple(txt)
    return txt


def calcula_quocientes(dicionario, inteiro):
    dic = dicionario
    dicKeys = list(dicionario)
    dicVals = list(dicionario.values())
    for i in range(len(dicionario)):
        dic[dicKeys[i]] = []
        for j in range(1, (inteiro + 1)):
            dic[dicKeys[i]] += [dicVals[i] / j]
    return dic


def reduz_listas(dic, int):
    dicKeys = list(dic.keys())
    for i in range(len(dicKeys)):
        p = 0
        while p <= i:
            if len(dicKeys[i]) != 0:
                dic[dicKeys[i]].pop()
                p += 1
    return dic

def atribui_mandatos(dicionario,inteiro):
    dic = calcula_quocientes(dicionario,inteiro)
    keys = list(dic.keys())
    vals = list(dic.values())
    valsOrdenados = []
    mdt = []
    for i in dic.values():
        valsOrdenados += i
    valsOrdenados = list(set(valsOrdenados))
    valsOrdenados.sort(reverse=True)
    valsOrdenados = valsOrdenados[:inteiro]
    j = 0
    k = len(vals)
    while len(mdt) != inteiro:
        if valsOrdenados[j] in vals[k-1]:
            mdt += keys[k-1]
            j += 1
            k = len(vals)
        else:
            k -= 1
    return mdt






def obtem_partidos(info):
    names = []
    for i, j in info.items():
        if type(j) == dict:
            for j, k in j.items():
                if type(k) == dict:
                    names += k.keys()
    names = list(set(names))
    names = sorted(names)
    return names


def obtem_resultado_eleicoes(info):
    names = obtem_partidos(info)
    somas = {}
    soma = 0
    somaDep = 0
    for n in range(len(names)):
        soma = 0
        for i, j in info.items():
            if type(j) == dict:
                for j, k in j.items():

                    if type(k) == dict:
                        for l, m in k.items():
                            if names[n] == l:

                                soma += m
                                somas[n] = soma
    for i in info.values():
        for j in i.values():
            if type(j) == int:
              somaDep += j

    for n in range(len(somas)):
        somas[n] = [somas[n]]
        somas[n].insert(0,names[n])
    somas = list(somas.values())
    somasFin = somas
    somas = dict(somas)
    listaDep = atribui_mandatos(somas,somaDep)
    for n in range(len(somasFin)):
        somasFin[n].insert(1,listaDep.count(names[n]))
        somasFin[n] = tuple(somasFin[n])
    somasFin = sorted(somasFin, key=lambda x: x[2],reverse=True)
    return somasFin






def produto_interno(tuplo1, tuplo2):
    if len(tuplo1) != len(tuplo2):
        raise ValueError('tuplos invalidos')
    sum, i = 0, 0
    while i < len(tuplo1):
        sum += tuplo1[i] * tuplo2[i]
        i += 1
    return float(sum)


def verifica_convergencia(tuplo1, tuplo2, tuplo3, real):
    soluc = list(produto_interno(tuplo1[i], tuplo3) for i in range(len(tuplo1)))
    for i in range(len(soluc)):
        soluc[i] -= tuplo2[i]
        if soluc[i] >= real:
            return False
    return True


def trocaPosicao(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


def retira_zeros_diagonal(tuplo1, tuplo2):
    lista1 = list(tuplo1)
    lista2 = list(tuplo2)
    x = 0
    y = 0
    for i in range(len(lista1)):
        x = y
        if lista1[x][y] == 0:
            for j in range(2):
                if lista1[j][y] != 0:
                    break
            trocaPosicao(lista1,j,x)
            trocaPosicao(lista2, j, x)
            y += 1
        else:
            y += 1
    tuplo1 = tuple(lista1)
    tuplo2 = tuple(lista2)
    return tuplo1, tuplo2

def eh_diagonal_dominante(tuplo):
    for x in range(len(tuplo)):
        if max(tuplo[x]) == tuplo[x][x]:
            return True
        else:
            return False
def resolve_sistema(tuplo1, tuplo2, real):
    x = []
    for i in range(len(tuplo1)):
        x.append(0)
    return x
A4, c4 = ((2, -1, -1), (2, -9, 7), (-2, 5, -9)), (-8, 8, -6)
print(resolve_sistema(A4, c4, 1e-20))

