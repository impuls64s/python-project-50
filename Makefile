install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl

package-re-install:
	pip install --user --force-reinstall dist/*.whl

build:
	poetry build

publish:
	poetry publish --dry-run

start: build publish package-re-install

gendiff:
	poetry run python -m gendiff.scripts.gendiff --help

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest --cov

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

selfcheck:
	poetry check


check: selfcheck test lint
