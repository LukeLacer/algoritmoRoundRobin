from time import time

class Processo:
    def __init__(self, base):
        self.base = base
        self.atual = 0
        self.preempcoes = 0

quantum = 0.001 # em segundos
processo1 = Processo(2)
processo2 = Processo(3)
processo3 = Processo(5)

fila = [processo1, processo2, processo3]
comeco = time()

while fila:
    inicio = time()
    while fila[0].atual < 100000 and time() < inicio + (quantum):
        fila[0].base * fila[0].base
        fila[0].atual += 1
    if fila[0].atual == 100000:
        fila[0].preempcoes += 1
        print(f'\n================== Processo {fila[0].base} ==================')
        print(f'Tempo de execução:   {inicio - comeco :.3f} s')
        print(f'Total de preempções: {fila[0].preempcoes} preempções')
        print(f'================================================\n')
        fila.pop(0)
    else:
        fila[0].preempcoes += 1
        fila.append(fila.pop(0))


total_preempçoes = processo1.preempcoes + processo2.preempcoes + processo3.preempcoes
print(f'Total de preempções: {total_preempçoes}')


