GIST_FILENAME := "seiyu_5percent_off.ics"

.PHONY: all
all: deps test build

build:
	python3 generate.py > $(GIST_FILENAME)

deps:
	pip3 install --user -r requirements.txt

test:
	python3 -m py_compile *.py

clean:
	rm -f *.ics
