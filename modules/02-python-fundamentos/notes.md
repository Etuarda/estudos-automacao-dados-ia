# Python Fundamentos

## Visão do módulo

Este módulo reúne minhas anotações das três aulas iniciais de fundamentos:

1. Ambiente de Desenvolvimento e Primeiros Passos com Python
2. Conhecendo a Linguagem de Programação Python
3. Tipos de Operadores com Python

O objetivo aqui é registrar entendimento técnico do começo da linguagem, sem copiar aula, mas organizando o que faz diferença para usar Python na prática.

## Aula 1 - Ambiente de Desenvolvimento e Primeiros Passos com Python

### Conceitos principais

- instalação e configuração do ambiente;
- interpretador Python;
- execução de scripts;
- terminal e editor de código;
- primeiro contato com sintaxe.

### Como funciona

Python pode ser usado de forma interativa, pelo terminal, ou por arquivos `.py`. O interpretador lê o código e executa instrução por instrução. No início, entender o ambiente é tão importante quanto entender a sintaxe, porque muitos erros aparecem não pela lógica do código, mas por configuração incorreta, caminho errado ou versão diferente do Python.

Também fez sentido perceber que editor e terminal cumprem papéis diferentes: o editor ajuda a escrever melhor, enquanto o terminal mostra como o programa realmente roda.

### Exemplo prático

```python
print("Olá, Python!")
```

Exemplo de execução no terminal:

```bash
python app.py
```

### Aplicação real

- rodar scripts locais de automação;
- testar pequenos programas rapidamente;
- iniciar projetos de dados e backend;
- criar hábito de executar código fora do editor.

### Erros comuns

- instalar Python e não configurar corretamente no PATH;
- confundir terminal do sistema com console do editor;
- salvar arquivo com extensão errada;
- tentar executar código sem verificar a versão instalada.

### Insight

No começo, programar não é só escrever código. É aprender a preparar o ambiente para que o código realmente rode de forma previsível.

## Aula 2 - Conhecendo a Linguagem de Programação Python

### Conceitos principais

- variáveis;
- tipos primitivos;
- entrada e saída de dados;
- identação;
- comentários;
- sintaxe simples e legível.

### Como funciona

Python tem uma sintaxe mais enxuta do que muitas outras linguagens e usa identação para delimitar blocos. Isso significa que o espaço em branco não é só estética: ele faz parte da estrutura do programa.

Variáveis guardam valores em memória e podem receber diferentes tipos de dados, como texto, inteiro, decimal e booleano. A linguagem facilita começar rápido, mas isso também exige atenção com conversão de tipos, porque nem toda entrada vem no formato que o programa precisa.

### Exemplo prático

```python
nome = "Eduarda"
idade = 26
estuda_python = True

print(nome)
print(idade)
print(estuda_python)
```

Exemplo com entrada de dados:

```python
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")
```

### Aplicação real

- captura de informações em scripts simples;
- manipulação de dados de entrada;
- criação de protótipos rápidos;
- base para qualquer programa maior em Python.

### Erros comuns

- misturar `str` com `int` sem conversão;
- esquecer que identação errada quebra o código;
- escolher nomes de variáveis pouco claros;
- acreditar que `input()` já retorna número.

### Insight

Python parece simples no começo, mas essa simplicidade cobra disciplina. Se eu não prestar atenção em identação, nome de variável e tipo de dado, o código rapidamente fica confuso.

## Aula 3 - Tipos de Operadores com Python

### Conceitos principais

- operadores aritméticos;
- operadores de comparação;
- operadores lógicos;
- operadores de atribuição;
- precedência entre operações.

### Como funciona

Operadores são os elementos que permitem calcular, comparar e combinar condições. Eles aparecem o tempo todo em regras de negócio, validações e decisões do programa.

Os aritméticos manipulam números. Os de comparação retornam `True` ou `False`. Os lógicos combinam expressões booleanas, o que é essencial para criar regras mais completas. Já os de atribuição ajudam a atualizar valores durante a execução.

Entender precedência também importa, porque a ordem de avaliação pode mudar o resultado se a expressão não estiver clara.

### Exemplo prático

```python
idade = 20
tem_documento = True

if idade >= 18 and tem_documento:
    print("Acesso autorizado")
```

Exemplo com operadores aritméticos e de atribuição:

```python
saldo = 100
saldo += 50
saldo -= 20

print(saldo)
```

### Aplicação real

- validação de cadastro;
- regras de acesso;
- filtros em dados;
- cálculos básicos em automações e relatórios.

### Erros comuns

- confundir `=` com `==`;
- montar condição lógica sem pensar na ordem;
- esquecer uso de parênteses em expressões maiores;
- criar regra que funciona em um caso e falha em outro.

### Insight

Os operadores parecem um detalhe pequeno, mas são a base de quase toda decisão do programa. Quando eu entendo bem comparação e lógica, começo a escrever código com mais intenção e menos tentativa e erro.

## Fechamento do módulo

### Aprendizado aplicado

Essas três aulas constroem a base para todo o resto da trilha. O principal aprendizado não foi só "como escrever Python", mas como pensar no fluxo mínimo de um programa:

- preparar o ambiente;
- escrever instruções válidas;
- armazenar dados;
- receber entradas;
- aplicar regras;
- produzir uma saída.

### Próximos pontos para aprofundar

- conversão de tipos;
- condicionais;
- laços de repetição;
- funções;
- coleções de dados.
