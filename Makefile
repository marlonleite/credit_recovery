runserver:
	python manage.py runserver 0.0.0.0:8000

clean:
	@find . -name "*.pyc" -exec rm -rf {} \;
	@find . -name "__pycache__" -delete

export_requirements:
	poetry export -f requirements.txt -o requirements.txt

export_requirements_dev:
	poetry export --dev -f requirements.txt -o requirements-dev.txt

black:
	black --target-version py38 --verbose --check --exclude=venv .

black_reformat:
	black --target-version py38 --verbose --exclude=venv .

shell:
	DEBUG=true python manage.py shell_plus