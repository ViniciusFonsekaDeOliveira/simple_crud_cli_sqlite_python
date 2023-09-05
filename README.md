# Nome do Projeto

Um simples CRUD CLI para Sqlite3 feito em python,
incluido o uso da biblioteca unittest para efetuar testes unitários dos principais módulos.

## Índice

- [Instalação](#instalação)
- [Contribuição](#contribuição)
- [Notas](#notas)
- [Uso & Adaptações](#obs)
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

## Uso

O uso desta implementação de python para Sqlite3 <br>
pode ser adaptada facilmente para os bancos MySQL e Postgres através das seguintes alterações:

0. Instalar psycopg2 e o mysql-connector.
1. Alterar o objeto de conexão.
2. Alterar os placeholders de ? para %s, em ambos SGBDs.
3. Atentar-se para a mudança no table_schema na hora de criar suas tabelas.

## Licença

Você é livre para usar, adaptar e comercializar este código como quiser, apenas cite a referência da sua inspiração.
