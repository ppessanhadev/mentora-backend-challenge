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

**Makefile**

1. `make init`
2. `make server`

**Docker compose**

1. `poetry install`
2. `poetry run src/manage.py runserver`

Um Swagger com as rotas disponiveis poderá ser visualizado na rota `http://127.0.0.1:8000/api/docs`
