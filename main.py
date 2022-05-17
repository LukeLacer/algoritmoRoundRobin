from time import time

class Processo:
    def __init__(self, base):
        self.base = base
        self.atual = 0
        self.preempcoes = 0
        self.tempo_execucao = 0

def runProcessos(i, quantum):
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
            fila[0].tempo_execucao = inicio - comeco
            fila.pop(0)
        else:
            fila[0].preempcoes += 1
            fila.append(fila.pop(0))

    with open("dados.csv","a") as arquivo:
        arquivo.write(f'{i};{quantum};processo1;{processo1.tempo_execucao};{processo1.preempcoes}\n')
        arquivo.write(f'{i};{quantum};processo2;{processo2.tempo_execucao};{processo2.preempcoes}\n')
        arquivo.write(f'{i};{quantum};processo3;{processo3.tempo_execucao};{processo3.preempcoes}\n')
    arquivo.close()

    total_preempçoes = processo1.preempcoes + processo2.preempcoes + processo3.preempcoes
    print(f'Processo {quantum} da execução {i} terminou. Total de preempções: {total_preempçoes}')

for i in range(1,11):
    runProcessos(i, 0.001)
    runProcessos(i, 0.01)
    runProcessos(i, 0.1)
    runProcessos(i, 1)
