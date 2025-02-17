help:	## Show the help text
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

python-makemigrations: ## Run manage.py makemigrations - shortcut: mm
	python manage.py makemigrations ${app}

mm: python-makemigrations

python-migrate: ## Run manage.py migrate_schemas - shortcut: m
	python manage.py migrate

m: python-migrate

run: 
	python manage.py runserver 0.0.0.0:8082

cs:
	python manage.py createsuperuser