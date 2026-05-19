# Manipulacao de Dados com Estruturas Fundamentais em Python

## Visao do modulo

Este modulo reune minhas anotacoes das cinco aulas sobre estruturas fundamentais em Python:

1. Trabalhando com Listas em Python
2. Conhecendo Tuplas em Python
3. Explorando Conjuntos em Python
4. Aprendendo a Utilizar Dicionarios em Python
5. Dominando Funcoes Python

O objetivo aqui e entender como organizar, consultar, transformar e reutilizar dados dentro de programas Python. Essas estruturas aparecem em praticamente qualquer automacao, analise de dados, API ou script mais completo.

## Aula 1 - Trabalhando com Listas em Python

### Conceitos principais

- listas como colecoes ordenadas;
- indices;
- fatiamento;
- inclusao, alteracao e remocao de itens;
- iteracao com `for`;
- listas aninhadas.

### Como funciona

Listas armazenam varios valores em uma unica variavel e mantem a ordem dos elementos. Cada item pode ser acessado por um indice, comecando em `0`. Como listas sao mutaveis, e possivel adicionar, alterar ou remover elementos depois da criacao.

Elas sao uteis quando a ordem importa ou quando o conjunto de dados pode mudar durante a execucao do programa. Em automacoes, por exemplo, uma lista pode guardar nomes de arquivos, produtos, clientes, tarefas ou resultados temporarios de uma consulta.

### Exemplo pratico

```python
tarefas = ["baixar relatorio", "limpar dados", "enviar resumo"]

tarefas.append("salvar backup")
tarefas[1] = "padronizar dados"

for tarefa in tarefas:
    print(tarefa)
```

Exemplo com fatiamento:

```python
numeros = [10, 20, 30, 40, 50]

print(numeros[0])
print(numeros[1:4])
print(numeros[-1])
```

### Aplicacao real

- armazenar resultados de uma automacao;
- percorrer linhas de uma planilha;
- montar listas de emails, arquivos ou produtos;
- guardar etapas de processamento de dados.

### Erros comuns

- esquecer que o primeiro indice e `0`;
- tentar acessar um indice que nao existe;
- alterar uma lista sem perceber que ela e mutavel;
- misturar muitos tipos diferentes na mesma lista sem necessidade;
- usar lista quando seria melhor buscar dados por chave em um dicionario.

### Insight

Lista e a estrutura mais direta quando eu penso em uma sequencia de itens. Se a pergunta principal for "quais itens existem e em que ordem?", lista costuma ser uma boa escolha.

## Aula 2 - Conhecendo Tuplas em Python

### Conceitos principais

- tuplas como colecoes ordenadas;
- imutabilidade;
- desempacotamento;
- retorno multiplo de funcoes;
- diferenca entre lista e tupla.

### Como funciona

Tuplas tambem guardam varios valores e preservam a ordem, mas nao podem ser alteradas depois de criadas. Essa imutabilidade ajuda quando os dados representam uma informacao fixa, como coordenadas, configuracoes, pares de valores ou registros que nao devem mudar acidentalmente.

Uma tupla pode ser acessada por indice da mesma forma que uma lista, mas metodos de alteracao como `append()` ou `remove()` nao existem para ela.

### Exemplo pratico

```python
usuario = ("Eduarda", 26, "Python")

nome, idade, linguagem = usuario

print(nome)
print(idade)
print(linguagem)
```

Exemplo de retorno multiplo:

```python
def calcular_total(valor, desconto):
    total = valor - desconto
    return total, desconto

total, desconto_aplicado = calcular_total(100, 15)

print(total)
print(desconto_aplicado)
```

### Aplicacao real

- representar dados fixos;
- retornar mais de um valor em uma funcao;
- proteger informacoes que nao devem ser alteradas;
- trabalhar com pares ou grupos pequenos de dados.

### Erros comuns

- tentar alterar uma tupla como se fosse lista;
- criar tupla de um unico item sem virgula;
- usar tupla para dados que precisam mudar constantemente;
- confundir imutabilidade da tupla com imutabilidade de objetos dentro dela.

### Insight

Tupla passa uma mensagem importante no codigo: esses dados formam um conjunto e nao deveriam ser modificados. Ela ajuda a deixar a intencao mais clara.

## Aula 3 - Explorando Conjuntos em Python

### Conceitos principais

- conjuntos como colecoes sem repeticao;
- ausencia de ordem garantida;
- operacoes de uniao;
- intersecao;
- diferenca;
- remocao de duplicados.

### Como funciona

Conjuntos, ou `set`, armazenam elementos unicos. Isso significa que valores repetidos sao automaticamente eliminados. Diferente de listas e tuplas, conjuntos nao devem ser usados quando a ordem dos dados e importante.

Eles sao muito uteis quando o objetivo e comparar grupos de informacoes. Por exemplo: descobrir quais clientes aparecem em duas listas, quais produtos existem em uma base mas nao em outra, ou remover duplicidades antes de processar dados.

### Exemplo pratico

```python
clientes_janeiro = {"Ana", "Bia", "Carlos", "Ana"}
clientes_fevereiro = {"Bia", "Daniel", "Eduarda"}

print(clientes_janeiro)
print(clientes_janeiro | clientes_fevereiro)
print(clientes_janeiro & clientes_fevereiro)
print(clientes_janeiro - clientes_fevereiro)
```

Exemplo removendo duplicados:

```python
emails = ["a@email.com", "b@email.com", "a@email.com"]
emails_unicos = set(emails)

print(emails_unicos)
```

### Aplicacao real

- remover duplicados de uma lista;
- comparar bases de dados;
- identificar itens em comum;
- verificar diferencas entre grupos;
- validar dados unicos.

### Erros comuns

- esperar que o conjunto mantenha a ordem original;
- tentar acessar item por indice;
- usar conjunto com dados que precisam ser duplicados;
- esquecer que alguns tipos mutaveis, como listas, nao podem ser itens de um conjunto.

### Insight

Conjunto e uma boa escolha quando a pergunta nao e "em que ordem?", mas sim "existe?", "esta repetido?", "esta em comum?" ou "esta faltando?".

## Aula 4 - Aprendendo a Utilizar Dicionarios em Python

### Conceitos principais

- pares de chave e valor;
- acesso por chave;
- alteracao de valores;
- metodos `keys()`, `values()` e `items()`;
- dicionarios aninhados;
- uso de `get()`.

### Como funciona

Dicionarios organizam dados em pares de chave e valor. Em vez de acessar informacoes por posicao, como em listas, o acesso acontece por uma chave descritiva. Isso torna o codigo mais legivel quando os dados possuem significado proprio.

Um dicionario pode representar um cadastro, uma configuracao, uma resposta de API, uma linha estruturada de uma planilha ou qualquer objeto com atributos nomeados.

### Exemplo pratico

```python
aluno = {
    "nome": "Eduarda",
    "curso": "Python",
    "nota": 9.5
}

aluno["status"] = "aprovada"

print(aluno["nome"])
print(aluno.get("email", "email nao informado"))
```

Exemplo percorrendo itens:

```python
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
```

Exemplo com estrutura aninhada:

```python
pedido = {
    "cliente": "Ana",
    "itens": ["notebook", "mouse"],
    "pagamento": {
        "forma": "cartao",
        "parcelas": 2
    }
}

print(pedido["pagamento"]["forma"])
```

### Aplicacao real

- representar cadastros;
- organizar dados vindos de APIs;
- criar configuracoes de scripts;
- montar registros para relatorios;
- transformar dados antes de salvar em banco ou arquivo.

### Erros comuns

- tentar acessar uma chave que nao existe;
- confundir chave com indice;
- criar dicionarios muito aninhados sem necessidade;
- usar nomes de chave inconsistentes;
- alterar dados sem validar se a chave existe.

### Insight

Dicionario e ideal quando cada valor precisa de um nome. Ele deixa o codigo mais expressivo porque mostra o que cada informacao representa.

## Aula 5 - Dominando Funcoes Python

### Conceitos principais

- criacao de funcoes com `def`;
- parametros;
- argumentos;
- retorno com `return`;
- escopo de variaveis;
- funcoes com valores padrao;
- organizacao e reutilizacao de codigo.

### Como funciona

Funcoes agrupam instrucoes que realizam uma tarefa especifica. Elas ajudam a evitar repeticao, deixam o codigo mais organizado e facilitam testes. Uma funcao pode receber dados de entrada por parametros, processar esses dados e devolver um resultado com `return`.

O ponto principal e pensar em funcoes como blocos reutilizaveis. Em vez de espalhar a mesma logica em varios lugares, a regra fica centralizada em uma funcao com nome claro.

### Exemplo pratico

```python
def calcular_media(notas):
    total = sum(notas)
    quantidade = len(notas)
    return total / quantidade

notas_aluno = [8.5, 9.0, 7.5]
media = calcular_media(notas_aluno)

print(media)
```

Exemplo com parametro padrao:

```python
def saudacao(nome, linguagem="Python"):
    return f"Ola, {nome}! Bons estudos em {linguagem}."

print(saudacao("Eduarda"))
print(saudacao("Eduarda", "SQL"))
```

### Aplicacao real

- reaproveitar regras de calculo;
- organizar etapas de automacao;
- validar dados antes de processar;
- separar responsabilidades dentro do codigo;
- facilitar manutencao e testes.

### Erros comuns

- criar funcao que faz tarefas demais;
- esquecer de usar `return`;
- confundir `print()` com retorno;
- depender de variaveis globais sem necessidade;
- usar nomes genericos que nao explicam a responsabilidade da funcao.

### Insight

Funcao bem escrita reduz bagunca no codigo. Se eu consigo explicar a tarefa em um nome claro, provavelmente consigo transformar essa parte em uma funcao reutilizavel.

## Fechamento do modulo

### Aprendizado aplicado

Este modulo mostrou que manipular dados em Python depende tanto da estrutura escolhida quanto da logica usada para percorrer e transformar esses dados. A decisao principal e entender o formato do problema:

- uso lista quando preciso de uma sequencia mutavel;
- uso tupla quando os dados formam um grupo fixo;
- uso conjunto quando quero unicidade ou comparacao entre grupos;
- uso dicionario quando preciso relacionar chaves e valores;
- uso funcao quando quero reaproveitar uma regra ou organizar melhor o codigo.

### Exemplo integrando o modulo

```python
def resumir_alunos(alunos):
    aprovados = []
    cursos = set()

    for aluno in alunos:
        cursos.add(aluno["curso"])

        if aluno["nota"] >= 7:
            aprovados.append(aluno["nome"])

    return {
        "total_alunos": len(alunos),
        "aprovados": aprovados,
        "cursos": cursos
    }

alunos = [
    {"nome": "Ana", "curso": "Python", "nota": 8.5},
    {"nome": "Bia", "curso": "Python", "nota": 6.0},
    {"nome": "Carlos", "curso": "SQL", "nota": 9.0}
]

resumo = resumir_alunos(alunos)

print(resumo)
```

### Proximos pontos para aprofundar

- compreensao de listas;
- funcoes lambda;
- tratamento de erros;
- leitura e escrita de arquivos;
- manipulacao de dados com bibliotecas como `csv`, `json` e `pandas`.
