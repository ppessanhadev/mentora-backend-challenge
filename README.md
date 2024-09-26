## Mentora backend challenge

**Como rodar localmente**

A aplicacão está hospeda em um servidor da AWS, no qual é gerenciado pelas pipes de CI/CD inclusas em `.github/*.yml` pelo Github Actions.

Para rodar a aplicacão localmente é necessário ter o [poetry](https://python-poetry.org/) com o python instalado em sua versão 3.12

Os comandos para rodar são:

**API**

1. `poetry install`
2. `poetry run serve`

Um Swagger com as rotas disponiveis poderá ser visualizado na rota `http://127.0.0.1:8000/api/docs`

**Testes**

1. `poetry install --with dev`
2. `poetry run test`
