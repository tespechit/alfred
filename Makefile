.PHONY: setup prepare_doc

setup:
	@cd alfred
	@pip install -r requirements.txt

prepare_doc:
	@pip install Sphinx
