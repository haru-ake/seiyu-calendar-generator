GIST_ITEM_ID  := "3d7c760974f1449480e30a5cd6bd062c"
GIST_FILENAME := "seiyu_5percent_off.ics"

.PHONY: all
all: deps build

deps:
	sudo apt-get install -y ruby
	sudo gem install gist

build:
	./gist.sh -u $(GIST_ITEM_ID) ../$(GIST_FILENAME)
