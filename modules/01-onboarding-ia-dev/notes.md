# Onboarding + IA para Acelerar o Desenvolvimento

## Checklist do desafio DIO

Este arquivo concentra a execução do desafio prático no repositório e atende aos critérios solicitados:

- **Contexto e objetivos:** apresentados nas seções `Contexto do módulo` e `Objetivos de estudo`.
- **Curadoria de fontes:** registrada na seção `Curadoria de fontes`, com 5 referências abertas.
- **Engenharia de prompts e cicatrizes:** documentada na seção `Engenharia de Prompts e cicatrizes`, com prompts, problemas, refinamentos e aprendizados.
- **Miniguia de estudo:** consolidado na seção `Entrega final consolidada`.
- **Resumo estruturado:** incluído em `Resumo estruturado`.
- **Glossário:** incluído em `Glossário rápido`.
- **Prompts reutilizáveis:** incluídos em `Prompts reutilizáveis`.

## Como este desafio foi organizado

Para integrar o desafio à trajetória completa do bootcamp, ele foi registrado como parte do módulo `01-onboarding-ia-dev`. Assim, o repositório mantém uma estrutura única de portfólio, sem perder os elementos exigidos pela DIO para esta entrega específica.

## Contexto do módulo

Este módulo registra o desafio prático de usar Inteligência Artificial como ferramenta de aprendizagem ativa. O foco foi construir um caderno temático no NotebookLM sobre Engenharia de Prompts aplicada ao aprendizado em backend, documentando fontes, testes de prompts, dificuldades encontradas e o aprendizado consolidado.

## Objetivos de estudo

- Entender como a IA pode apoiar o estudo técnico.
- Praticar curadoria de fontes e organização do conhecimento.
- Aprender a refinar prompts com base nos resultados obtidos.
- Construir um material reutilizável de revisão.

## Conceitos principais

- **IA (Inteligência Artificial):** área da computação que desenvolve sistemas capazes de executar tarefas associadas à inteligência humana.
- **LLM (Large Language Model):** modelo treinado em grande volume de texto para gerar, resumir e interpretar linguagem natural.
- **Engenharia de Prompts:** prática de elaborar instruções mais claras, específicas e contextualizadas para obter respostas melhores.
- **Contexto:** informação adicional que orienta o modelo na direção da resposta desejada.
- **Refinamento iterativo:** ajuste progressivo do prompt a partir da análise das respostas.

## Como funciona

Ao interagir com um modelo de linguagem, a qualidade da resposta depende bastante da forma como o problema é apresentado. Um prompt vago tende a gerar uma resposta genérica. Já um prompt com contexto técnico, escopo definido, público-alvo e formato esperado tende a produzir uma resposta mais útil.

No desafio, a IA foi usada não como substituta do estudo, mas como apoio para:

- explicar conceitos;
- estruturar revisões;
- gerar exemplos;
- comparar abordagens;
- apontar riscos;
- acelerar o entendimento de temas de backend.

## Curadoria de fontes

As fontes escolhidas foram abertas, introdutórias e complementares entre si:

1. [Prompt Engineering Guide](https://www.promptingguide.ai/)
2. [OpenAI Docs: Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering)
3. [Alura: O que são LLMs e como funcionam?](https://www.alura.com.br/artigos/o-que-e-llm)
4. [DevMedia: Como usar IA para aprender programação](https://www.devmedia.com.br/como-usar-ia-para-aprender-programacao/43809)
5. [OpenAI Help: Limitações e cuidados com IA generativa](https://help.openai.com/en/articles/6825453-chatgpt-general-faq)

## Engenharia de Prompts e cicatrizes

### Prompt 1

**Prompt inicial:**  
"Explique como modelos de linguagem podem ajudar estudantes de desenvolvimento backend a organizar o aprendizado."

**Problema:**  
Resposta ampla demais e pouco prática.

**Refinamento:**  
"Explique como modelos de linguagem podem ajudar no estudo de Node.js, APIs REST e documentação técnica, com exemplos práticos para uma desenvolvedora backend iniciante."

**Aprendizado:**  
Quanto mais contexto técnico e objetivo claro, melhor a resposta.

### Prompt 2

**Prompt:**  
"Explique o que é Engenharia de Prompts e por que ela é importante no uso de LLMs."

**Problema:**  
Boa definição, mas pouca aplicação prática.

**Refinamento:**  
Pedir exemplos voltados para backend.

**Aprendizado:**  
Explicação teórica melhora quando o prompt pede aplicação concreta.

### Prompt 3

**Prompt:**  
"Compare um prompt genérico e um prompt contextualizado no estudo de desenvolvimento backend."

**Aprendizado:**  
Ficou mais claro que o contexto reduz ambiguidade e melhora utilidade.

### Prompt 4

**Prompt:**  
"Dê exemplos de como usar IA para estudar APIs REST, testes com Jest e modelagem de banco de dados."

**Aprendizado:**  
A IA pode ser útil como guia de estudo, revisão e geração de exemplos iniciais.

### Prompt 5

**Prompt:**  
"Quais são os principais riscos de confiar em respostas de IA sem validação técnica?"

**Aprendizado:**  
Os principais riscos são alucinação, desatualização e falsa sensação de certeza.

### Prompt 6

**Prompt:**  
"Organize os principais conceitos estudados em um resumo estruturado com definições curtas e exemplos práticos."

**Aprendizado:**  
Prompts de revisão estruturada ajudam bastante na consolidação do conteúdo.

### Prompt 7

**Prompt:**  
"Por que a IA está trazendo exemplos em Python se pedi foco em Node.js?"

**Aprendizado:**  
Se a linguagem desejada não estiver explícita, a IA pode assumir outra referência padrão.

### Prompt 8

**Prompt:**  
"Reescreva o exemplo anterior usando Node.js e explique cada etapa."

**Aprendizado:**  
O refinamento iterativo é uma das partes mais valiosas do processo.

## Exemplo prático

```python
tema = "APIs REST"
linguagem = "Node.js"
nivel = "iniciante"

prompt = f"Explique {tema} com exemplos práticos em {linguagem} para uma pessoa {nivel}."
print(prompt)
```

Esse exemplo simples mostra a ideia de montar prompts a partir de contexto explícito. Na prática, isso ajuda a evitar respostas genéricas e melhora o alinhamento com o objetivo do estudo.

## Aplicação real

Esse aprendizado aparece no mundo real em situações como:

- estudo guiado de documentação técnica;
- depuração assistida por IA;
- revisão de conceitos antes de entrevistas;
- geração de exemplos iniciais para backend;
- apoio à organização de trilhas de aprendizagem.

## Erros comuns

- usar prompts genéricos demais;
- não informar stack, linguagem ou nível de experiência;
- confiar na primeira resposta sem validar;
- pedir uma solução sem definir formato de saída;
- não iterar quando a resposta vier superficial.

## Insight

O ponto menos óbvio foi perceber que aprender a perguntar bem é parte do aprendizado técnico. A IA responde melhor quando o raciocínio do usuário também está melhor estruturado.

## Entrega final consolidada

### Resumo estruturado

- **IA:** tecnologia usada como apoio para estudo, análise e geração de conteúdo.
- **LLM:** modelo de linguagem capaz de interpretar instruções e gerar respostas em linguagem natural.
- **Engenharia de Prompts:** técnica de criar instruções melhores para obter resultados mais úteis.
- **Elementos de um bom prompt:** clareza, contexto, objetivo e formato esperado.
- **Limitações da IA:** alucinação, desatualização, falta de contexto e excesso de confiança.

### Glossário rápido

- **Prompt:** instrução dada ao modelo.
- **Contexto:** detalhe que orienta a resposta.
- **Alucinação:** erro apresentado como se estivesse correto.
- **Token:** unidade de texto processada pelo modelo.
- **Refinamento iterativo:** melhoria sucessiva do prompt.

### Prompts reutilizáveis

- Explique `[conceito]` com foco em backend, incluindo definição, exemplo prático e erro comum.
- Compare `[tecnologia A]` e `[tecnologia B]` considerando um projeto backend iniciante.
- Revise este resumo técnico e aponte inconsistências, lacunas e melhorias.
- Gere exemplos de código para `[tecnologia]` aplicados a APIs REST.
- Transforme este conteúdo em um plano de estudo de 5 dias.
