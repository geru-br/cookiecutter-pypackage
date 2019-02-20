.PHONY: clean-build clean-pyc clean-test clean lint coverage test test-all

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

clean: clean-build clean-pyc clean-test

build:
	poetry build

install: clean
	poetry install

update-deps: clean
	poetry update
	poetry install

lint:
	poetry run flake8 {{cookiecutter.project_slug}}

coverage: lint
	poetry run py.test --cov={{cookiecutter.project_slug}} --cov-fail-under=95

test: lint
	poetry run pytest

test-all:
	poetry run tox

bump-version:
	poetry version

publish: clean bump-version build
	twine upload --repository-url https://geru-pypi.geru.com.br/ dist/*

# 	Using twine because of this poetry's issue: https://github.com/sdispater/poetry/issues/239
#	poetry config repositories.geru-pypi https://geru-pypi.geru.com.br/
#	poetry publish -r geru-pypi --username ${PYPI_USERNAME} --password ${PYPI_PASSWORD}
