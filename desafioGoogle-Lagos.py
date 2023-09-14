class Lago:
    def __init__(self, inicio, termino, altura):
        self.inicio = inicio
        self.termino = termino
        self.altura = altura

def RegistrarLago(arrayLagos, arrayExtremidade, inicio, fim, quantidadeElementos, reverso):
    inicioAtualizado = quantidadeElementos - fim if reverso else inicio
    fimAtualizado = quantidadeElementos - inicio if reverso else fim

    arrayLagos.append(Lago(inicioAtualizado, fimAtualizado, arrayExtremidade[inicio]))

def ObterLagosExtremidades(arrayLagos, arrayExtremidade, quantidadeElementos, reverso=False):
    inicio = 0

    for i in range(inicio, len(arrayExtremidade)):
        if arrayExtremidade[i] >= arrayExtremidade[inicio] and i - inicio == 1:
            inicio = i
        elif i - inicio >= 2 and arrayExtremidade[i] >= arrayExtremidade[inicio]:
            RegistrarLago(arrayLagos, arrayExtremidade, inicio, i, quantidadeElementos, reverso)
            inicio = i

def ObterAreaLago(indiceInicial, indiceFinal, alturaTotal, arrayOriginal, somaTotal):
    for i in range(indiceInicial + 1, indiceFinal):
        somaTotal += alturaTotal - arrayOriginal[i]

    return somaTotal

espacos = []
n = int(input("Quantos espaços deseja inserir? "))

for i in range(n):
    valor = int(input(f"Digite o do espaço {i + 1}: "))
    espacos.append(valor)

lagos = []

maximo = max(espacos)

indicesMaximos = []

for i in range(len(espacos)):
    if espacos[i] == maximo:
        indicesMaximos.append(i)

extremidadeEsquerda = espacos[:indicesMaximos[0] + 1]
extremidadeDireita = espacos[indicesMaximos[-1]:][::-1]

ObterLagosExtremidades(lagos, extremidadeEsquerda, len(espacos) - 1)

if len(indicesMaximos) > 1:
    for i in range(len(indicesMaximos) - 1):
        lagos.append(Lago(indicesMaximos[i], indicesMaximos[i + 1], espacos[indicesMaximos[i]]))

ObterLagosExtremidades(lagos, extremidadeDireita, len(espacos) - 1, True)

somaTotal = 0
for lago in lagos:
    somaTotal = ObterAreaLago(lago.inicio, lago.termino, lago.altura, espacos, somaTotal)

print(f"Soma total das áreas dos lagos: {somaTotal}")