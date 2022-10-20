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

<<<<<<< HEAD
test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
=======
test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml
>>>>>>> dc84411167d1dd28d940d5377226eafcd2de94ea

selfcheck:
	poetry check

<<<<<<< HEAD
=======
test:
	poetry run pytest

>>>>>>> dc84411167d1dd28d940d5377226eafcd2de94ea
check: selfcheck test lint
