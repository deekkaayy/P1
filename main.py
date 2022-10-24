def limpa_texto(texto):
    texto = ' '.join(texto.split())  # Juntar vários espaços
    return texto

cad = ('Ipsum   dolore  consectetur  sed  dolorem.  Dolor  sed  eius consectetur  consectetur dolore modi consectetur. Voluptatem sit  velit  amet  dolor neque est. Quiquia porro tempora sed dolore  adipisci  dolore.  Velit dolore numquam dolore dolor labore.')
print(limpa_texto(cad))
def corta_texto(texto, numero):
    texto = limpa_texto(texto)
    if len(texto) > numero:
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
        texto2 = ''
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
        raise ValueError('justifica_texto:argumentos invalidos')
    texto = limpa_texto(texto)

    dist = texto.index(' ', texto.index(' ') + 1) - texto.index(' ')
    if dist > numero:
        raise ValueError('justifica_texto:argumentos invalidos')
    primeiroEspaco = texto.index(' ')

    if primeiroEspaco > numero :
        raise ValueError('justifica_texto:argumentos invalidos')

    i = 0
    textoFinal = []
    while len(texto) > 0 :
        textoFinal.append(corta_texto(texto, numero)[0])
        texto = corta_texto(texto,numero)[1]
        i += 1
    for i in range(len(textoFinal)-1):
        textoFinal[i] = insere_espacos(textoFinal[i], numero)
    textoFinal[-1] = limpa_texto(textoFinal[-1])
    while len(textoFinal[-1]) < numero:
        textoFinal[-1] += ' '
    textoFinal = tuple(textoFinal)
    return textoFinal
print(justifica_texto(cad,60))

def calcula_quocientes(dicionario, inteiro):
    if len(list(dicionario.keys())) >= 1: #Ter pelomenos um partido
        dic = dict(dicionario)
        dicKeys = list(dic)
        dicVals = list(dic.values())
        for i in range(len(dic)):
            dic[dicKeys[i]] = []
            for j in range(1, (inteiro + 1)):
                dic[dicKeys[i]] += [dicVals[i] / j]
        return dic

def atribui_mandatos(dicionario,inteiro):
    dic = calcula_quocientes(dicionario,inteiro)
    keys = list(dic.keys())
    vals = list(dic.values())
    valsOrdenados = [] #Lista com os quocientes ordenados com o objetivo de descobrir os mais votados
    mdt = []
    for i in dic.values():
        valsOrdenados += i
    valsOrdenados.sort(reverse=True)
    valsOrdenados = valsOrdenados[:inteiro]
    j = 0
    k = len(vals)-1 #Percorre-se pelo ultimo para dar prioridade às menos votadas
    while len(mdt) != inteiro:
        if valsOrdenados[j] in vals[k]:
            mdt += keys[k]
            vals[k].remove(valsOrdenados[j])
            j += 1
            k = len(vals)-1
        else:
            k -= 1  #Caso não pertença, recua-se um para verificar se existe no partido seguinte
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
    if type(info) != dict:
        raise ValueError('obtem_resultado_eleicoes: argumento invalido')
    #if len(info.keys())
    names = obtem_partidos(info)
    somas = {}
    somaDep = 0
    for n in range(len(names)): #Index das letras
        soma = 0
        for i, j in info.items(): #Aceder items do info
            if type(j) == dict: #Aceder dicionarios correspondentes aos nomes dos partidos
                for j, k in j.items(): #Aceder items do dicionario dos nomes
                    if type(k) == dict: #Aceder ao dicionario que contém os votos
                        for l, m in k.items():  #Aceder votos individuais
                            if names[n] == l:   #Caso a letra dos votos coincide com o index, fazer soma
                                soma += m
                                somas[n] = soma
    for i in info.values(): #Aceder valores de info
        for j in i.values():

            if type(j) == int: #Se o tipo corresponder à um unico inteiro(numero deputados) fazer a soma dos deputados
                if j == 0:
                    raise ValueError('obtem_resultado_eleicoes: argumento invalido')
                else: somaDep += j


    for n in range(len(somas)): #Listificar as somas dos votos
        somas[n] = [somas[n]]
        somas[n].insert(0,names[n]) #Atribuir letra dos votos às somas

    somas = list(somas.values())
    resultado = somas #Fazer copia da lista para preparar o resultado final
    somas = dict(somas) #Tornar as somas para dicionario para que se possa fazer a atribuição de mandatos
    listaDep = atribui_mandatos(somas,somaDep) #Lista dos deputados atribuidos
    for n in range(len(resultado)): #Contagem do numero de deputados por letra
        resultado[n].insert(1,listaDep.count(names[n]))
        resultado[n] = tuple(resultado[n])
    resultado = sorted(resultado, key=lambda x: x[2],reverse=True) #Ordenaçao pelo numero de votos
    return resultado


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


def trocaPosicao(list, pos1, pos2): #Funcao suplementar para efetuar a troca de linhas na funcao retira zeros diagonal
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def retira_zeros_diagonal(tuplo1, tuplo2):
    tuplo1 = list(tuplo1)
    tuplo2 = list(tuplo2)
    for i in range(len(tuplo1)):
        if tuplo1[i][i] == 0:
            for k in range(len(tuplo1)):
                if tuplo1[k][i] != 0 and tuplo1[i][k] != 0:
                    trocaPosicao(tuplo1,i,k)
                    trocaPosicao(tuplo2,i,k)
    tuplo1 = tuple(tuplo1)
    tuplo2 = tuple(tuplo2)
    return tuplo1,tuplo2

def eh_diagonal_dominante(tuplo):
    tuplo = list(tuplo)
    for i in range(len(tuplo)):
        tuplo[i] = list(tuplo[i])
    for i in range(len(tuplo)):
        for j in range(len(tuplo)):
            tuplo[i][j] = abs(tuplo[i][j])
    diag = []
    for i in range(len(tuplo)):
        diag.append(tuplo[i][i])

    maxs = []
    for i in range(len(tuplo)):
        maxs.append(max(tuplo[i]))

    if diag == maxs:
        return True
    else:
        return False

def resolve_sistema(tuplo1, tuplo2, real):
    if len(tuplo1) != len(tuplo2) or type(tuplo1) != tuple or type(tuplo2) != tuple:
        raise ValueError('resolve_sistema: argumentos invalidos')
    if eh_diagonal_dominante(tuplo1) == False:
        raise ValueError('resolve_sistema: matriz nao diagonal dominante')
    x = [] #Criacao da primeira iteracao de x(vetor de zeros)
    for i in range(len(tuplo1)):
        x.append(0)
    while True:
        for i in range(len(tuplo1)):
            x[i] = x[i] + (tuplo2[i]-(produto_interno(tuplo1[i],x)))/tuplo1[i][i] #aplicacao da formula
        if verifica_convergencia(tuplo1,tuplo2,x,real) == True:
            break
    for i in range(len(x)):
        x[i] = float(round(x[i]))
    return x
