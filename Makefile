new:
	poetry new  # создание базовой структуры

install:
	poetry install  # установка зависимостей

longest-lenght:
	poetry run longest-lenght

examples:
	poetry run examples

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_tasks

test:
	env PYTHONPATH="$(pwd)" python3 tests/test_longest_length.py

pytest:
	poetry run pytest

pytest-print:
	poetry run pytest -s  # видно все, что выводится с помощью print

pytest-current:
	poetry run pytest tests/test_.py

