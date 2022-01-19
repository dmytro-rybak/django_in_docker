fill_db:
	docker-compose run --rm django python manage.py fill_db

superuser:
	docker-compose run --rm django python manage.py createsuperuser
