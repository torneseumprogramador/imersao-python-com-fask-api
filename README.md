# Código feito na imersão de python api com flask 
## Feito na comunidade do torne-se um programador
- https://www.torneseumprogramador.com.br/aulas/logica_programacao_python

## Dependências:
- mysql

## Configuração:
```shell
# arquivo env_vars.sh
export HOST="localhost"
export USER="root"
export PASS="root"
export DATABASE="imersao_python_flask"
```

## Para startar a aplicação digite: 
```shell
sh mysql_migration.sh # rodar migrações do mysql
sh bundle.sh # instalar dependências
sh start.sh # startar a aplicação
```

## Exemplos em testes feitos com curl via sh
```shell
sh testes/curl/get.sh
sh testes/curl/post.sh
sh testes/curl/put.sh
sh testes/curl/delete.sh
```