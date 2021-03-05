# Teste Técnico Desenvolvedor(a) Python Júnior [REMOTO]

API desenvolvida para no Processo seletivo da Instruct.

## Como usar

### Servidor Local

Migrations:

$ python manage.py makemigrations

$ python manage.py migrate

Para subir o servidor utilize:

$ python manage.py runserver

### Endpoints

GET - /orgs

Listar todas as organizações cadastradas, ordenadas pelo score.

GET - /orgs/{login}

Busca uma organização por meio do respectivo login, se não é encontrada no banco, pesquisa na API do GitHub e persiste os dados

DELETE - /orgs/{login}

Apaga o registro da organização do respectivo login
