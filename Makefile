.PHONY: setup prepare_doc jenkins

setup:
	@cd alfred
	@pip install -r requirements.txt

prepare_doc:
	@pip install Sphinx

travis:
	@cd alfred && pip install -r requirements/travis.txt
	@cd alfred && python manage.py test
