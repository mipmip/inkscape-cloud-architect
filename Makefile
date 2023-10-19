
ASSETS_ZIP = Asset-Package_04282023.ca9655a386a46bda0b6238cca2651e8f27fcb5c9.zip
INSCAPE_DIR = $(HOME)/.config/inkscape

all: clean build-symbols install-templates install-symbols
clean: clean-templates clean-symbols

clean-templates:
	rm -Rfv $(INSCAPE_DIR)/templates/aws-architect

clean-symbols:
	rm -Rfv $(INSCAPE_DIR)/symbols/aws-architect

clean-awslab-repo-cache:
	rm -Rfv ./aws-inkscape-symbols/awslabs-repo

install-symbols:
	rsync -av ./aws-inkscape-symbols/target/ $(INSCAPE_DIR)/symbols/aws-architect/

install-templates:
	rsync -av templates/ $(INSCAPE_DIR)/templates/aws-architect/

build-symbols:
	cd ./aws-inkscape-symbols; ./build.sh $(ASSETS_ZIP)
