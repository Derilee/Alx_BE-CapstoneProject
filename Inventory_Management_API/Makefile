.PHONY: allcommands

git:
	git add .
	git commit -m 'BE capstone project - Building an Inventory Management API'
	git push

migrate:
	python manage.py makemigrations
	python manage.py migrate

server:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver