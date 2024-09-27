init:
	poetry install --with dev
	poetry run src/manage.py migrate

server:
	poetry run src/manage.py runserver

migration:
	poetry run src/manage.py migrate

generate-migrations:
	poetry run src/manage.py makemigrations

generate-requirements:
	poetry export --without-hashes --format=requirements.txt > requirements.txt

seed-mentoring:
	poetry run src/manage.py loaddata src/modules/mentoring/infra/seeds/0001_mentoring.json

server-container:
	poetry run src/manage.py runserver 0.0.0.0:8000

server-container-with-content: migration seed-mentoring
	poetry run src/manage.py runserver 0.0.0.0:8000
