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