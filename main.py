from time import time

class Processo:
    def __init__(self, base):
        self.base = base
        self.atual = 100000

quantum = 1
preempções = 0
processo1 = Processo(2)
processo2 = Processo(3)
processo3 = Processo(5)

fila = [processo1, processo2, processo3]
começo = time()

while fila:
    inicio = time()
    while fila[0].atual > 0 and time() < inicio + (quantum/1000):
        fila[0].base * fila[0].base
        fila[0].atual -= 1
    if fila[0].atual == 0:
        print(f'o processo {fila[0].base} terminou de executar após { inicio -começo :.4f} segundos!')
        fila.pop(0)
    else:
        fila.append(fila.pop(0))
    preempções += 1
print(f'tudo pronto, houveram {preempções} preempções no total')
