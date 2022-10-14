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
            texto
            return texto
        '''else:
            return texto1,texto2'''
    else:
        return texto
def insere_espacos(texto,numero):
    texto = limpa_texto(texto)
    i = 0
    if len(texto) < numero:
        while i < numero:
            if texto[i] == ' ' and len(texto) < numero: #Introduzir mais um espaço caso o caracter selecionado é espaço
                texto = texto[:i] + ' ' + texto[i:]
                i += 2 #Tendo em conta ao espaço adicionado, procede-se dois caracteres para chegar à proxima palavra
            else: i += 1
    return texto
def justifica_texto(texto,numero):
    if type(texto) != str or type(numero) != int:
        raise ValueError('argumentos invalidos')
    texto = texto.replace('\t''\n''\v''\f''r', '') #Remoção dos caracteres brancos exceto espaços
    txt = tuple(texto[i:i+numero] for i in range (0, len(texto), numero)) #"Tuplificar" o texto com indice do numero introduzido
    return txt
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
        dic[dicKeys[i]] = list(dicKeys[i])
        for j in range(1,inteiro):
            dic[dicKeys[i]] += [dicVals[i]/j]

    '''
    for i in range(len(dicionario)):
        for j in range(1,inteiro):
            dic[dicKeys[i]].append(dicVals[i]/j)
    '''
    return dic


def verifica_convergencia(tuplo1,tuplo2,tuplo3,real):
    A1, c1 = ((1, -0.5), (-1, 2)), (-0.4, 1.9)

    return


'''
texto = str(input('introduza texto: '))
print(limpa_texto(texto))
numero = int(input('introduza um numero: '))
print(limpa_texto(texto))
print(corta_texto(texto,numero))
print(insere_espacos(texto,numero))
print(justifica_texto(texto,numero))
for l in justifica_texto(texto, numero): print(l)
tuplo1 = print(input('Introduza o primeiro tuplo'))
tuplo2 = print(input('Introduza o segundo tuplo'))
calcula_quocientes({'A':12000, 'B':7500, 'C':5250, 'D':3000}, 7)
print( produto_interno((1,2,3,4,5),(-4,5,-6,7,-8)))
'''
print(calcula_quocientes({'A':12000, 'B':7500, 'C':5250, 'D':3000}, 7))


