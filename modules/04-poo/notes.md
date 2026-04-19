# Programação Orientada a Objetos

## Conceitos principais

- classes
- objetos
- atributos
- métodos
- encapsulamento
- herança

## Como funciona

Explique como objetos ajudam a modelar comportamento e estado, e quando POO melhora a organização do código.

## Exemplo prático

```python
class Usuario:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        return f"Olá, eu sou {self.nome}"
```

## Aplicação real

- modelagem de entidades de negócio
- organização de sistemas maiores
- reaproveitamento de comportamento

## Erros comuns

- criar classes sem necessidade
- misturar responsabilidade demais em um único objeto
- usar herança quando composição seria melhor

## Insight

Registre aqui quando POO fez sentido de verdade para você.
