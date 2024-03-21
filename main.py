import csv

# Impementando algorítmo de busca linear
def executar_busca_linear(lista, valor):
    tamanho_lista = len(lista)
    for i in range(tamanho_lista):
        if valor == lista[i]:
            return True
    return False

# Função que faz dedup e tratamento no cpf
def criar_lista_dedup(lista):
    lista_dedup = []
    for cpf in lista:
        cpf = str(cpf)
        cpf = cpf.replace("-", "").replace(".", "")
        if len(cpf) == 11:
            if not executar_busca_linear(lista_dedup, cpf):
                lista_dedup.append(cpf) 

    return lista_dedup

# Função para tratar os CPFs
def tratar_cpf(cpf):
    cpf_tratado = cpf.replace(".", "").replace("-", "")
    return cpf_tratado

# Função para ler o arquivo csv
def ler_cpf_arquivo(nome_arquivo):
    cpfs = []
    with open(nome_arquivo, mode='r', newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            cpfs.append(tratar_cpf(linha[0]))
        
    return cpfs

# Função de teste
def testar_funcao(nome_arquivo):
    lista_cpfs = ler_cpf_arquivo(nome_arquivo)
    lista_dedup = criar_lista_dedup(lista_cpfs)
    print(lista_dedup)

nome_arquivo = "cpfs.csv"
testar_funcao(nome_arquivo)
