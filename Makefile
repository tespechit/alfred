.PHONY: setup prepare_doc jenkins

setup:
	@cd alfred
	@pip install -r requirements.txt

prepare_doc:
	@pip install Sphinx

jenkins:
	@cd alfred
	@pip install -r requirements/jenkins.txt
	@python manage.py test
