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

gendiff:
	poetry run python -m gendiff.scripts.gendiff --help

lint:
	poetry run flake8 gendiff

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml
