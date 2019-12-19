RUN = poetry run
SNYK = $(RUN) snyk test
CHALICE = $(RUN) chalice

default: requirements security

requirements: requirements.txt requirements-dev.txt

requirements.txt: poetry.lock
	poetry export -f requirements.txt > requirements.txt

requirements-dev.txt: poetry.lock
	poetry export --dev -f requirements.txt > requirements-dev.txt

security: snyk snyk-dev

snyk-dev:
	$(SNYK) --package-manager=pip --file=requirements-dev.txt

snyk:
	$(SNYK)

local:
	$(CHALICE) local

deploy:
	$(CHALICE) deploy

delete:
	$(CHALICE) delete

test:
	$(RUN) pytest


.PHONY: default requirements security snyk snyk-dev local deploy delete test
