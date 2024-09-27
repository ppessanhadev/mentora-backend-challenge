## Mentora backend challenge

Essa aplicação tem como objetivo conter toda a regra de negocio, armazenamento de informações e gerenciamneto de uma aplicação centralizada para compra/venda de mentorias, no qual contém feedbacks personalizados.

#### Overview

Para o desenvolvimento, utilizei algumas as seguintes ferramentas:

- [] [Django]() como framework principal para o desenvolvimento da API
- [] [Django-ninja]() para o desenvolvimento simplificado de rotas e schemas

**Como rodar localmente**

A aplicacão está hospeda em um servidor da AWS, no qual é gerenciado pelas pipes de CI/CD inclusas em `.github/*.yml` pelo Github Actions.

Para rodar a aplicacão localmente é necessário ter o [poetry](https://python-poetry.org/) com o python instalado em sua versão 3.12

Os comandos para rodar são:

**Docker compose (Recomendado)**

Para evitar configurações de ambiente, setups e criação de banco de dados, <strong>basta entrar na raiz e rodar os comandos</strong>:

1. `cp .env.example .env`
2. `docker-compose up -d`

**Makefile**

OBS: é necessário ter uma instancia postgres local e configurada para rodar de maneira individual

1. Rode o comando `cp .env.example .env`
2. Preecha o .env com as configurações do seu banco postgres
3. Rode o comando `make init`
4. Inicialize o server com o comando `make server`

Um Swagger com as rotas disponiveis poderá ser visualizado na rota `http://127.0.0.1:8000/api/docs`
