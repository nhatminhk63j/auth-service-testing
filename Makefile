 
.ONESHELL:

.PHONY: clean install tests run all

clean:
	find . -type d -name __pycache__ -delete

system-packages:
	sudo apt install python-pip -y

python-packages:
	pip install -r requirements.txt

install: system-packages python-packages

tests: 
	python3 manage.py test

run:
	python3 manage.py run

all: clean install tests run