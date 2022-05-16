from time import time

class Processo:
  def __init__(self, base):
    self.base = base
    self.atual = 0

def runProcesso(processo):
  if processo.atual < 100000:
    inicio = time()
    while processo.atual < 100000:
      processo.base * processo.base
      processo.atual += 1
      if time() >= inicio + quantum:
        print('foi')
        break
  else:
    fila.remove(processo)
    print(f'Processo {processo.base} terminou!')

quantum = 1

processo1 = Processo(2)
processo2 = Processo(3)
processo3 = Processo(5)

fila = [processo1, processo2, processo3]

while fila:
  runProcesso(processo1)
  runProcesso(processo2)
  runProcesso(processo3)
