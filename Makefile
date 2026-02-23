.SILENT: update requirements format ruff check mypy pyclean
.PHONY: update requirements format ruff check mypy pyclean

precommit: ruff check test

format: ruff

ruff:
	ruff format .
	ruff check . --fix

check:
	mypy --incremental --show-error-codes --pretty .

mypy: check

pyclean:
	pyclean .

test:
	pytest tests/unit

test_coverage: pyclean
	coverage run -m pytest tests/unit && coverage report -m

test_coverage_html: pyclean
	coverage run -m pytest tests/unit && coverage html
