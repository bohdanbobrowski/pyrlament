.SILENT: help
.PHONY: help


help:
	echo "Pyrlament"


test:
	pytest tests/unit -W ignore::DeprecationWarning


requirements:
	pipreqs . --force



format: black ruff autoflake isort no_implicit_optional


ruff:
	poetry run ruff --fix .


autoflake:
	poetry run autoflake --remove-all-unused-imports -i .


black:
	poetry run black .


isort:
	poetry run isort  --profile black .


no_implicit_optional:
	poetry run no_implicit_optional .

check_mypy:
	poetry run mypy --incremental --show-error-codes --pretty .

mypy: check_mypy

pyclean:
	poetry run pyclean .

check_coverage: pyclean
	poetry run coverage run -m pytest tests/unit && poetry run coverage report -m

check_coverage_html: pyclean
	poetry run coverage run -m pytest tests/unit && poetry run coverage html