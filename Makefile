SHELL := /bin/bash

help:
	@echo "Usage:"
	@echo " make release | Release to pypi."

release:
	python setup.py register sdist upload

test:
	@coverage run test_project/manage.py test
	@flake8 .
	@DJANGO_SETTINGS_MODULE=test_project.settings coverage report
