import csv
import re

# Implementando algoritmo de oerdenação merge sort
# def executar_merge_sort(lista, inicio=0, fim=None):
#     if not fim:
#         fim = len(lista)

#     if fim - inicio > 1:
#         meio = (inicio + fim) // 2
#         executar_merge_sort(lista, inicio, meio)
#         executar_merge_sort(lista, meio, fim)
#         executar_merge(lista, inicio, meio, fim)

#     return lista

# def executar_merge(lista, inicio, meio, fim):
#     esquerda = lista[inicio:meio]
#     direita = lista[meio:fim]
#     topo_esquerda = topo_direita = 0

#     for p in range(inicio, fim):
#         if topo_esquerda >= len(esquerda):
#             lista[p] = direita[topo_direita]
#             topo_direita += 1
#         elif topo_direita >= len(direita):
#             lista[p] = esquerda[topo_esquerda]
#             topo_esquerda += 1
#         elif esquerda[topo_esquerda] < direita[topo_direita]:
#             lista[p] = esquerda[topo_esquerda]
#             topo_esquerda += 1
#         else:
#             lista[p] = direita[topo_direita]
#             topo_direita += 1

# # Implementando algoritmo de busca binária
# def executar_busca_binaria(lista, valor):
#     minimo = 0
#     maximo = len(lista) - 1

#     while minimo <= maximo:
#         meio = (minimo + maximo) // 2
#         if valor < lista[meio]:
#             maximo = meio - 1
#         elif valor > lista[meio]:
#             minimo = meio + 1
#         else:
#             return True

#     return False
         
# Impementando algorítmo de busca linear
def executar_busca_linear(lista, valor):
    tamanho_lista = len(lista)
    for i in range(tamanho_lista):
        if valor == lista[i]:
            return True
    return False

# Função que faz dedup e tratamento no cpf
def criar_lista_dedup(lista):
    lista_dedup = set()
    for cpf in lista:
        cpf = str(cpf)
        cpf = cpf.replace("-", "").replace(".", "")
        if len(cpf) == 11:
            lista_dedup.add(cpf)

    return list(lista_dedup)

# Função para tratar os CPFs
def tratar_cpf(cpf):
    return re.sub(r"[.-]", "", cpf)

# Função para ler o arquivo csv
def ler_cpf_arquivo(nome_arquivo):
    cpfs = []
    with open(nome_arquivo, mode='r', newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            if linha:
                cpfs.append(tratar_cpf(linha[0]))

    return cpfs

# Função para formatar CPF
def formatar_cpf(cpf):
    cpf = re.sub(r"[.-]", "", cpf)
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

# Função de teste
def testar_funcao(nome_arquivo):
    lista_cpfs = ler_cpf_arquivo(nome_arquivo)
    lista_dedup = criar_lista_dedup(lista_cpfs)
    
    cpfs_formatados = [formatar_cpf(cpf) for cpf in lista_dedup]
    cpfs_formatados.sort(key=None)
    
    print(f'Quantidade de CPFs deduplicados: {len(lista_dedup)}\n')
    print('CPFs corrigidos e tratados:')
    print(lista_dedup)
    print('\nCPFs formatados:')
    print(cpfs_formatados)

nome_arquivo = "cpfs.csv"
testar_funcao(nome_arquivo)
