# Preparação de Dados

## Conceitos principais

- limpeza de dados
- padronização
- tratamento de valores ausentes
- transformação
- análise exploratória inicial

## Como funciona

Explique aqui por que dados brutos raramente estão prontos para análise e como a preparação impacta a qualidade do resultado final.

## Exemplo prático

```python
import pandas as pd

df = pd.DataFrame({"idade": [20, None, 35]})
df["idade"] = df["idade"].fillna(df["idade"].mean())
```

## Aplicação real

- preparação para dashboards
- preparação para modelos de ML
- padronização de bases para análise

## Erros comuns

- ignorar dados faltantes
- transformar sem entender impacto
- limpar demais e perder informação útil

## Insight

Anote aqui o que mudou na sua visão sobre qualidade de dados.
