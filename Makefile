.SILENT: help
.PHONY: help

help:
	echo "Pyrlament"

test:
	pytest tests/unit -W ignore::DeprecationWarning

requirements:
    pipreqs . --force