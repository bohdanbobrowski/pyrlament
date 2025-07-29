.SILENT: update requirements format ruff check mypy pyclean
.PHONY: update requirements format ruff check mypy pyclean

update:
	poetry lock
	poetry install

requirements:
	pipreqs . --force

precommit: ruff check test

format: ruff

ruff:
	poetry run ruff format .
	poetry run ruff check . --fix

check:
	poetry run mypy --incremental --show-error-codes --pretty .

mypy: check

pyclean:
	poetry run pyclean .

test:
	poetry run pytest tests/unit

test_coverage: pyclean
	poetry run coverage run -m pytest tests/unit && poetry run coverage report -m

test_coverage_html: pyclean
	poetry run coverage run -m pytest tests/unit && poetry run coverage html