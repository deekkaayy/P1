def limpa_texto(texto):
    texto = ' '.join(texto.split())  #Juntar vários espaços
    texto = texto.replace('\t', '') #Substituição dos caracteres brancos
    texto = texto.replace('\n', '')
    texto = texto.replace('\v', '')
    texto = texto.replace('\f', '')
    texto = texto.replace('\r', '')
    return texto
def corta_texto(texto,numero):#DUVIDA AQUI, E SUPOSTO APARECER PALAVRA COMPLETA CASO NUM < LEN DA PRIMEIRA PALVRA
    if len(limpa_texto(texto)) > numero:
        texto1 = texto[:numero] #Primeiro string com o numero de caracteres
        texto2 = texto[numero:len(limpa_texto(texto))] #Segundo string com o resto dos caracteres\
        if texto1.count(' ') != 0:
            texto1 = texto[:texto1.rindex(' ')]
            texto2 = texto[texto1.rindex(' '):len(limpa_texto(texto))]
            return texto1,texto2
        elif texto1.count(' ') == 0:
            texto1 = ''
            texto2 = texto
            return texto1,texto2
        else:
            return texto1,texto2
    else:
        return texto
def insere_espacos(texto,numero):
    texto = limpa_texto(texto)
    i = 0
    while len(texto) < numero:
        if i == len(texto):
            i = 0
        elif texto[i] == ' ' and texto[i+1] != ' ':
            texto = texto[:i] + ' ' + texto[i:]
            i += 2
        else:
            i += 1
    return texto
print(insere_espacos('Fundamentos da programacao!!!!', 50))
def justifica_texto(texto,numero):
    if type(texto) != str or type(numero) != int:
        raise ValueError('argumentos invalidos')

    '''texto = limpa_texto(texto)
    txt = (corta_texto(texto,numero) for i in range (0, len(texto), numero)) #"Tuplificar" o texto com indice do numero introduzido
    for i in range(len(txt)):
        txt[i] = corta_texto(txt[i],numero)
        txt[i] = insere_espacos(txt[i],numero)
    return txt'''

print(corta_texto('Computers are incredibly fast, accurate and stupid. Human beings are incredibly slow inaccurate, and brilliant. Together they are powerful beyond imagination.',60))
def produto_interno(tuplo1,tuplo2):
    if len(tuplo1) != len(tuplo2):
        raise ValueError('tuplos invalidos')
    sum, i = 0, 0
    while i < len(tuplo1):
        sum += tuplo1[i] * tuplo2[i]
        i += 1
    return float(sum)
def calcula_quocientes(dicionario,inteiro):
    dic = dicionario
    dicKeys = list(dicionario)
    dicVals = list(dicionario.values())
    for i in range(len(dicionario)):
        dic[dicKeys[i]] = []
        for j in range(1, (inteiro + 1)):
            dic[dicKeys[i]] += [dicVals[i] / j]
    return dic
def reduz_listas(dic,int):
    dicKeys= list(dic.keys())
    for i in range(len(dicKeys)):
        p = 0
        while p <= i:
            if len(dicKeys[i]) != 0:
                dic[dicKeys[i]].pop()
                p += 1
    return dic
def atribui_mandatos(dicionario,inteiro):
    dic = calcula_quocientes(dicionario,inteiro)
    dicVals = []
    dicKeys = list(dic.keys())
    for i in range(len(dic)):
        dicVals += dic[dicKeys[i]]
    dicVals.sort(reverse=True)
    mdt = []
    dic = reduz_listas(dic,inteiro)
    for i in range(inteiro):
        for k,v in dic.items():
            if dicVals[i] in v:
                mdt.append(k)
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
    for n in range(len(names)):
        soma = 0
        for i, j in info.items():
            if type(j) == dict:
                for j, k in j.items():
                    if type(k) == dict:
                        for l,m in k.items():
                            if names[n] == l:
                                soma += m
                                somas[n] = soma
    somas = sorted()
    return list(somas.values())
info = {
'Endor': {'deputados': 7,
    'votos': {'A':12000, 'B':7500, 'C':5250, 'D':3000}},
'Hoth': {'deputados': 6,
    'votos': {'B':11500, 'A':9000, 'E':5000, 'D':1500}},
'Tatooine': {'deputados': 3,
    'votos': {'A':3000, 'B':1900}}}
#print(obtem_resultado_eleicoes(info))
cad = ('Computers are incredibly \n\tfast, \n\t\taccurate'
' \n\t\t\tand stupid. \n Human beings are incredibly slow '
'inaccurate, and brilliant. \n Together they are powerful '
'beyond imagination.')
print(justifica_texto(cad,60))

def verifica_convergencia(tuplo1,tuplo2,tuplo3,real):
    A1, c1 = ((1, -0.5), (-1, 2)), (-0.4, 1.9)

    return




