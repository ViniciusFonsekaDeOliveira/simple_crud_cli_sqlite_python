# Nome do Projeto

Um simples CRUD CLI para Sqlite3 feito em python.

## Índice

- [Instalação](#instalação)
- [Contribuição](#contribuição)
- [Notas](#notas)
- [Licença](#licença)

## Instalação

1. Clone o repositorio
2. Faça suas adaptações

## Constribuição

De forma geral, este repositório pode servir de base para muitas implementações utilizando outros bancos de dados.

## Notas

O sqlite3 já vem incorporado ao python por padrão.  
Para manipular arquivos de extensão .env utilizei a biblioteca decouple.

```bash
pip install python-decouple
```

<pre>

from decouple import AutoConfig
config = AutoConfig()
nome_da_variavel_dentro_do_env_file = config("NOME_DA_VARIAVEL", default=None)

</pre>

## Licença

Você é livre para usar, adaptar e comercializar este código como quiser, apenas cite a referência da sua inspiração.
