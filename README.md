## Mentora backend challenge

Essa aplicação tem como objetivo conter toda a regra de negócio, armazenamento de informações e gerenciamneto de uma aplicação centralizada para lista de mentorias, no qual contém feedbacks personalizados.

### Overview

Para o desenvolvimento, foram utilizadas as seguintes ferramentas:

- [Django](https://www.djangoproject.com/) como framework principal para o desenvolvimento da API
- [Django-ninja](https://django-ninja.dev/) para o desenvolvimento simplificado de rotas e schemas
- [Poetry](https://python-poetry.org/docs/) para gereciamento de pacotes externos
- [makefile](https://www.gnu.org/software/make/manual/make.html) para reduzir ações em comandos simplificados
- [Docker](https://docs.docker.com/) + [docker-compose](https://docs.docker.com/compose/) para conteinarização da aplicacão

A aplicação está em nuvem e funcionando no [render](https://render.com/), e as rotas com os parâmetros disponíveis podem ser visualizadas nesse link: https://mentora-backend-challenge.onrender.com/api/docs

**OBS**: por ser free tier, a API "dorme" a cada 15 minutos por inatividade, então caso esteja demorando um pouco basta aguardar.

**Tabelas**

As tabelas disponiveis para armazenamento de dados foram criadas com os seguintes modelos e relações:

_mentories (referente as mentorias)_
| id | title | description | price |
|:--:|:-------------------------:|:-----------------------------------------:|:-----:|
| 27 | Criando uma marca pessoal | Construa sua marca pessoal e destaque-se! | 35.00 |
| 28 | Habilidades de negociação | Aprenda a negociar como um profissional! | 50.00 |

_feedbacks (referente aos feedbacks ligado as mentorias)_
| id | name | message | stars | mentoring_id |
|:--:|:-----------------:|:-------------------:|:-----:|--------------|
| 1 | João Paulo | Poderia ser melhor. | 3 | 1 |
| 2 | Euclides de souza | Legal! | 4 | 1 |
| 3 | Thais Carla | TOOOOOP | 5 | 1 |

### Rodando a aplicação

Como avisado na seção de [overview](#overview) a aplicação está disponivel em cloud e pode ser visualizada a partir desse link: https://mentora-backend-challenge.onrender.com/api/docs, entretando, caso haja interesse em rodar localmente, basta seguir a próximas orientações.

Para rodar a aplicacão localmente é necessário ter o [poetry](https://python-poetry.org/) com o python instalado em sua versão 3.12

**Rodando com docker compose (Recomendado)**

Para evitar configurações de ambiente, setups e criação de banco de dados, <strong>basta entrar na raiz e rodar os comandos</strong>:

1. `cp .env.example .env`
2. `docker-compose up -d`

**Makefile**

Para usar os comandos do makefile é necessário ter uma instancia postgres local e configurada para rodar de maneira individual. 

Siga os próximos passos com as dados do banco em mãos:

1. Rode o comando `cp .env.example .env`
2. Preecha o .env com as configurações do seu banco postgres
3. Rode o comando `make init`
4. Inicialize o server com o comando `make server`

Um Swagger com as rotas disponiveis poderá ser visualizado na rota `http://127.0.0.1:8000/api/docs`
