makemigrate:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

start:
	poetry run python manage.py runserver

shell:
	poetry run python manage.py shell_plus --ipython --print-sql

rebuild:
	docker-compose up -d --no-deps --build

term:
	docker exec -it seller_project-web-1 bash