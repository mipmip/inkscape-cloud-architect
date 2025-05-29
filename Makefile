ASSETS_ZIP = Asset-Package_04282023.ca9655a386a46bda0b6238cca2651e8f27fcb5c9.zip
UNAME:=$(shell uname)
ifeq ($(UNAME), Darwin)
	INKSCAPE_DIR := $(HOME)/Library/Application\ Support/org.inkscape.Inkscape/config/inkscape
else
	INKSCAPE_DIR := $(HOME)/.config/inkscape
endif

all: clean build-symbols install-templates install-symbols
clean: clean-templates clean-symbols

clean-templates:
	rm -Rfv $(INKSCAPE_DIR)/templates/aws-architect

clean-symbols:
	rm -Rfv $(INKSCAPE_DIR)/symbols/aws-architect

clean-awslab-repo-cache:
	rm -Rfv ./symbols/aws-inkscape-symbols/awslabs-repo

install-symbols:
	rsync -av ./symbols/aws-inkscape-symbols/target/ $(INKSCAPE_DIR)/symbols/aws-architect/

install-templates:
	rsync -av templates/ $(INKSCAPE_DIR)/templates/aws-architect/

build-symbols:
	cd ./symbols/aws-inkscape-symbols; ./build.sh $(ASSETS_ZIP)
