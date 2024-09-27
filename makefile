ARGS=


manager:
	poetry run src/manage.py ${ARGS}

init:
	poetry install --with dev
	poetry run src/manage.py migrate

server:
	poetry run src/manage.py runserver

migration:
	poetry run src/manage.py migrate

generate-migrations:
	poetry run src/manage.py makemigrations

seed-mentoring:
	poetry run src/manage.py loaddata src/modules/mentoring/infra/seeds/0001_mentoring.json