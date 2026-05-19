# Exercicios sobre Estruturas Fundamentais em Python
# Cada bloco foi comentado para ajudar na revisao dos conceitos.

# ----------------------------------------
# 1. Listas
# ----------------------------------------
# Listas guardam varios valores em ordem e podem ser alteradas.

tarefas = ["estudar listas", "praticar tuplas", "revisar dicionarios"]

print("Lista inicial:", tarefas)

tarefas.append("resolver exercicios")
print("Depois do append:", tarefas)

tarefas[1] = "praticar conjuntos"
print("Depois da alteracao:", tarefas)

tarefas.remove("estudar listas")
print("Depois da remocao:", tarefas)

print("Primeira tarefa:", tarefas[0])
print("Ultima tarefa:", tarefas[-1])

print("Percorrendo a lista:")
for tarefa in tarefas:
    print("-", tarefa)


# ----------------------------------------
# 2. Tuplas
# ----------------------------------------
# Tuplas guardam valores em ordem, mas nao podem ser alteradas.

aluno = ("Eduarda", 26, "Python")

nome, idade, curso = aluno

print("Nome:", nome)
print("Idade:", idade)
print("Curso:", curso)
print("Quantidade de dados na tupla:", len(aluno))


# ----------------------------------------
# 3. Conjuntos
# ----------------------------------------
# Conjuntos nao guardam valores repetidos e ajudam em comparacoes.

alunos_python = {"Ana", "Bia", "Carlos", "Ana"}
alunos_sql = {"Bia", "Daniel", "Eduarda"}

print("Alunos de Python:", alunos_python)
print("Alunos de SQL:", alunos_sql)
print("Todos os alunos:", alunos_python | alunos_sql)
print("Alunos nos dois cursos:", alunos_python & alunos_sql)
print("Apenas em Python:", alunos_python - alunos_sql)

emails = ["a@email.com", "b@email.com", "a@email.com", "c@email.com"]
emails_unicos = set(emails)

print("Emails sem repeticao:", emails_unicos)


# ----------------------------------------
# 4. Dicionarios
# ----------------------------------------
# Dicionarios organizam informacoes em pares de chave e valor.

produto = {
    "nome": "Notebook",
    "preco": 3500.00,
    "estoque": 8
}

print("Produto:", produto["nome"])
print("Preco:", produto["preco"])
print("Estoque:", produto["estoque"])

produto["estoque"] -= 1
produto["categoria"] = "informatica"

print("Produto atualizado:", produto)
print("Fornecedor:", produto.get("fornecedor", "nao informado"))

print("Dados do produto:")
for chave, valor in produto.items():
    print(chave, ":", valor)


# ----------------------------------------
# 5. Funcoes
# ----------------------------------------
# Funcoes ajudam a organizar e reutilizar regras.

def calcular_media(notas):
    total = sum(notas)
    quantidade = len(notas)
    return total / quantidade


def verificar_aprovacao(media, nota_minima=7):
    if media >= nota_minima:
        return "Aprovado"

    return "Reprovado"


notas = [8.5, 7.0, 9.0]
media = calcular_media(notas)
status = verificar_aprovacao(media)

print("Media:", media)
print("Status:", status)


# ----------------------------------------
# 6. Exercicio pratico integrador
# ----------------------------------------
# Objetivo:
# Criar um pequeno resumo de alunos usando lista, dicionario,
# conjunto e funcao.

alunos = [
    {"nome": "Ana", "curso": "Python", "nota": 8.5},
    {"nome": "Bia", "curso": "Python", "nota": 6.0},
    {"nome": "Carlos", "curso": "SQL", "nota": 9.0},
    {"nome": "Daniel", "curso": "SQL", "nota": 5.5}
]


def gerar_resumo(alunos):
    aprovados = []
    cursos = set()

    for aluno in alunos:
        cursos.add(aluno["curso"])

        if aluno["nota"] >= 7:
            aprovados.append(aluno["nome"])

    return {
        "total_alunos": len(alunos),
        "total_aprovados": len(aprovados),
        "aprovados": aprovados,
        "cursos": cursos
    }


resumo = gerar_resumo(alunos)

print("Resumo final:")
print("Total de alunos:", resumo["total_alunos"])
print("Total de aprovados:", resumo["total_aprovados"])
print("Aprovados:", resumo["aprovados"])
print("Cursos encontrados:", resumo["cursos"])
