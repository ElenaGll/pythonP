install:
	poetry install

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
