import time

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
    return item


# desenfileira o primeiro elemento da fila
# reduz em um o tamanho da fila
def desenfileirar(fila):
    if (vazia(fila)):
        return "Fila vazia!"
    return fila.pop(0)


arquivo_texto = "fichamento.txt"

fila_normal = criarFila()
fila_especial = criarFila()


def carrega_arquivo():

    with open(arquivo_texto, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            paciente = linha[:-1]

            if paciente[-1:].upper() == "G":
                enfileirar(fila_especial, paciente)
            elif paciente[-1:].upper() == "D":
                enfileirar(fila_especial, paciente)
            elif paciente[-1:].upper() == "L":
                enfileirar(fila_especial, paciente)
            elif int(paciente[-2:]) > 65:
                enfileirar(fila_especial, paciente)
            else:
                enfileirar(fila_normal, paciente)


def chamada(desenfileirar, vazia):

    with open(arquivo_texto, "r", encoding="utf-8") as arquivo:
        while open(arquivo_texto, "r", encoding="utf-8"):
            for indice in range(0,2):
                if vazia == True:
                    break
                else:
                    print(desenfileirar(fila_especial), "???")
                    time.sleep(2)
                # cont = 0
                # while cont <= 2:
                #     print(desenfileirar(fila_especial), "???")
                
                
                    # cont += 1
            for indice in range(0,1):
                if vazia == True:
                    break
                else:
                    print(desenfileirar(fila_normal), "!!!")
                    time.sleep(2)
                # cont = 0
                # while cont <= 1:
                
                
                    # cont += 1


#     with open(arquivo_texto, "r", encoding="utf-8") as arquivo:

#         for linha in arquivo:
            
#             normal = desenfileirar(fila_normal)
#             especial = desenfileirar(fila_especial)

#             if especial[-1:].upper() == "G" or especial[-1:].upper() == "D" or especial[-1:].upper() == "L" or int(especial[-2:]) > 65 or int(normal[-2:]) > 65:
#                 print(especial)
#                 time.sleep(2)
#             else:
#                 if pessoa == "Fila vazia!":
#                     break
#                 else:
#                     print(normal)
#                     time.sleep(2)
        

# Executando o código

carrega_arquivo()


# fila = criarFila()
# enfileirar(fila, 10)
# enfileirar(fila, 20)
# enfileirar(fila, 40)
# print(fila)
# print(desenfileirar(fila), "Desenfileirado da fila")