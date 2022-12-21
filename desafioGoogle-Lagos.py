class Lago:
  def __init__(self, inicio, termino, altura):
    self.inicio = inicio
    self.termino = termino
    self.altura = altura

def RegistrarLago(arrayLagos, arrayExtremidade, inicio, fim, quantidadeElementos, reverso):
  inicioAtualizado = quantidadeElementos - fim if reverso else inicio
  fimAtualizado = quantidadeElementos - inicio if reverso else fim

  arrayLagos.append(Lago(inicioAtualizado, fimAtualizado, arrayExtremidade[inicio]))

def ObterLagosExtremidades(arrayLagos, arrayExtremidade, quantidadeElementos, reverso = False):
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

# Resolução da questão
espacos = [1,3,2,4,1,3,1,4,5,2,2,1,4,2,2]
lagos = []

# Obtenção dos máximos do grático
maximo = max(espacos)

# Verificação dos máximos internos
indicesMaximos = []

for i in range(len(espacos)):
  if espacos[i] == maximo:
    indicesMaximos.append(i)

# Separação das extremidades
extremidadeEsquerda = espacos[:indicesMaximos[0] + 1]
extremidadeDireita = espacos[indicesMaximos[-1]:][::-1]

# Obter os lagos de forma ordenada
ObterLagosExtremidades(lagos, extremidadeEsquerda, len(espacos) - 1)

if len(indicesMaximos) > 1:
  for i in range(len(indicesMaximos) - 1):
    lagos.append(Lago(indicesMaximos[i], indicesMaximos[i + 1], espacos[indicesMaximos[i]]))

ObterLagosExtremidades(lagos, extremidadeDireita, len(espacos) - 1, True)

# Obtem a soma total dos lagos
somaTotal = 0

for lago in lagos:
  somaTotal = ObterAreaLago(lago.inicio, lago.termino, lago.altura, espacos, somaTotal)

print(somaTotal)
