mig:
	./manage.py makemigrations
	./manage.py migrate


user:
	./manage.py createsuperuser --username=admin


app:
	./manage.py startapp apps



