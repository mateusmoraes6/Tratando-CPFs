**Tratando CPFs com Python: Algoritmo de Busca Linear**

---

Este repositório detalha os passos tomados para criar um algoritmo em Python que trata CPFs, removendo caracteres especiais como pontos e traços, e também realiza a deduplicação desses CPFs.

**Descrição**

---

**Objetivo:** Desenvolver uma solução para transformar uma lista de CPFs, realizando deduplicação, remoção de caracteres especiais e verificação de comprimento.

**Implementação:**

1. **Deduplicação e Tratamento de CPFs:**
    - Utilização de um algoritmo de busca linear para deduplicar os CPFs.
    - Remoção de caracteres especiais (ponto e traço) dos CPFs.
    - Verificação se os CPFs possuem 11 dígitos.

**Algoritmo de Busca:**

- Escolha da busca linear devido à possibilidade de CPFs desordenados na lista.

**Remoção de Caracteres Especiais:**

- Utilização da função `replace()` para remover ponto e traço dos CPFs.

**Verificação de Comprimento:**

- Utilização da função `len()` para verificar se os CPFs possuem 11 dígitos.
---
### 1. Importando Bibliotecas

No primeiro passo, importamos a biblioteca `csv`, que nos permitirá ler os CPFs a partir de um arquivo CSV.

### 2. Implementando a Busca Linear

A busca linear é um algoritmo simples de busca em que percorremos cada elemento de uma lista sequencialmente até encontrar o valor desejado. Este algoritmo é implementado na função `executar_busca_linear`. Ele é utilizado posteriormente para verificar se um CPF já está presente na lista deduplicada.

### 3. Tratando os CPFs

Na função `criar_lista_dedup`, percorremos a lista de CPFs, removemos caracteres especiais (pontos e traços) e verificamos se o CPF já está presente na lista deduplicada usando a busca linear. Se não estiver, adicionamos o CPF à lista deduplicada.

### 4. Tratando um CPF Individual

A função `tratar_cpf` recebe um CPF como entrada e retorna o CPF sem caracteres especiais, apenas com números.

### 5. Lendo o Arquivo CSV

Na função `ler_cpf_arquivo`, lemos os CPFs de um arquivo CSV e os tratamos usando a função `tratar_cpf`. Esses CPFs tratados são retornados como uma lista.

### 6. Testando a Função

Finalmente, na função `testar_funcao`, chamamos a função `ler_cpf_arquivo` para obter os CPFs do arquivo CSV e, em seguida, chamamos a função `criar_lista_dedup` para deduplicar e tratar esses CPFs. Os CPFs deduplicados e tratados são impressos no terminal.

**Conclusão:**

Este resumo detalha os passos para implementar uma solução em Python que realiza deduplicação, remoção de caracteres especiais e verificação de comprimento em uma lista de CPFs. Ao seguir estes passos, será possível manipular e tratar eficientemente os dados de CPFs em aplicações Python.