# Exercicios sobre Tipos de Operadores com Python
# Cada bloco foi comentado para ajudar na revisao dos conceitos.

# ----------------------------------------
# 1. Operadores aritmeticos
# ----------------------------------------
# Usados para fazer contas basicas.

numero_a = 10
numero_b = 3

print("Soma:", numero_a + numero_b)
print("Subtracao:", numero_a - numero_b)
print("Multiplicacao:", numero_a * numero_b)
print("Divisao:", numero_a / numero_b)
print("Divisao inteira:", numero_a // numero_b)
print("Resto da divisao:", numero_a % numero_b)
print("Potencia:", numero_a ** numero_b)


# ----------------------------------------
# 2. Operadores de comparacao
# ----------------------------------------
# Retornam True ou False.

idade = 20

print("Idade eh maior que 18?", idade > 18)
print("Idade eh menor que 18?", idade < 18)
print("Idade eh igual a 20?", idade == 20)
print("Idade eh diferente de 21?", idade != 21)
print("Idade eh maior ou igual a 18?", idade >= 18)
print("Idade eh menor ou igual a 17?", idade <= 17)


# ----------------------------------------
# 3. Operadores logicos
# ----------------------------------------
# Servem para combinar condicoes.

tem_cadastro = True
pagamento_aprovado = True

print("Pode liberar acesso?", tem_cadastro and pagamento_aprovado)
print("Uma das condicoes eh verdadeira?", tem_cadastro or False)
print("Negacao do cadastro:", not tem_cadastro)


# ----------------------------------------
# 4. Operadores de atribuicao
# ----------------------------------------
# Atualizam o valor da variavel.

pontos = 100
print("Pontos iniciais:", pontos)

pontos += 20
print("Depois de somar 20:", pontos)

pontos -= 10
print("Depois de subtrair 10:", pontos)

pontos *= 2
print("Depois de multiplicar por 2:", pontos)

pontos /= 5
print("Depois de dividir por 5:", pontos)


# ----------------------------------------
# 5. Exercicio pratico
# ----------------------------------------
# Regra simples:
# A pessoa pode entrar se tiver 18 anos ou mais
# e se tiver documento.

idade_usuario = 19
tem_documento = True

if idade_usuario >= 18 and tem_documento:
    print("Entrada permitida.")
else:
    print("Entrada negada.")

