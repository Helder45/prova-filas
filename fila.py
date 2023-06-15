# Criar fila
# determinado tamanho 0
def criarFila():
    fila = []
    return fila


# Verifica se a fila está vazia
def vazia(fila):
    return len(fila) == 0


# Verifica o primeiro elemento da fil
# sem removê - lo
def verificarPrimeiro(fila):
    if (vazia(fila)):
        return "Fila Vazia"
    return fila[0]


# insere elementos na fila ao final
# acrescendo em 1 o tamanho da fila
def enfileirar(fila, item):
    fila.append(item)
    print(item, " enfileirado ")


# desenfileira o primeiro elemento da fila
# reduz em um o tamanho da fila
def desenfileirar(fila):
    if (vazia(fila)):
        return "Fila vazia!"
    return fila.pop(0)


arquivo_texto = "fichamento.txt"

fila_normal = criarFila()
fila_especial = criarFila()

lista_pacientes = []

def carrega_arquivo(lista_pacientes):

    with open(arquivo_texto, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            paciente = linha[:-1]

            lista_pacientes.append(paciente)
        print(lista_pacientes)
    

# Executando o código
# fila = criarFila()
# enfileirar(fila, 10)
# enfileirar(fila, 20)
# enfileirar(fila, 40)
# print(fila)
# print(desenfileirar(fila), "Desenfileirado da fila")