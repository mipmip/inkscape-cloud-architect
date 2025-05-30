import inkex
from inkex.elements import Rectangle, Group, PathElement, Line, Symbol
from inkex import Use, Transform
import json
import os
from ica_utils import jsonloader
from ica_utils import resource_vpc
from pathlib import Path
import requests
from ica_utils.icalog import debug

class aws_auto_diagram(inkex.EffectExtension):

    # move to example
    def rect(self):
        rect = Rectangle.new(100, 100, 100, 100)  # (x, y, width, height)
        rect.style = {"fill": "blue", "stroke": "yellow"}
        # Add to the SVG document
        self.svg.append(rect)

    # move to example
    def shape_test(self):
        layer = self.svg.add(Group.new('my_label', is_layer=True))
        #create shape
        my_shape = PathElement()

        # You can set the path through many different methods.
        # Lists of numbers, pythonic objects, Cubic curves etc.
        my_shape.path = "M 0 0 L 0 100 L 100 100 L 100 0 z"

        # Transform can be modified in many ways too
        my_shape.transform.add_translate(self.svg.namedview.center)
        my_shape.style="fill:red"

        #create line
        line1 = layer.add(Line(x1='0', y1= '0', x2='100', y2='100'))
        line1.style = {'stroke-width': 3, 'stroke': 'blue'}

    # not working
    def delete_all(self):
        debug("DELETE ALL")
        for node in self.svg.xpath('//svg:path'):
            debug(node)
            node.delete()

    # move to example
    def remote_json_test(self):
        debug("remote_json_test")
        response = requests.get('https://api.restful-api.dev/objects')
        data = response.json()
        debug(data)

    # move to example
    def make_symbol_id_list(self):
        symbol_list = self.svg.defs.xpath('svg:symbol')
        if len(symbol_list) < 1:
            debug('No Symbols Found In Document')
            return []
        else:
            symbol_id_list = [x.get_id() for x in symbol_list]
            return symbol_id_list

    ## MOVE TO utils
    def make_symbol_instance(self, symbol_id, parent):
        use_element = Use()
        use_element.set('xlink:href', f'#{symbol_id}')
        parent.append(use_element)

        # Move new element to 0,0
        # Make a negative translate from elements current x, y and apply
        bbox = use_element.bounding_box()
        origin_translate = -Transform().add_translate(bbox.left, bbox.top)
        use_element.transform = use_element.transform @ origin_translate

        return use_element

    def parse_test_data(self):
        config_data = jsonloader.load_json_file('/home/pim/.config/inkscape/extensions/aws-auto-diagram/test-data.json')
        if config_data:

            vpcs = list(filter(lambda node: node['data']['type'] == 'vpc', config_data))
            subnets = list(filter(lambda node: node['data']['type'] == 'subnet', config_data))
            debug(subnets)

            for vpc in vpcs:
                resource_vpc.render_vpc(self);

            for subnet in subnets:
                resource_vpc.render_subnet(self, subnet);

    # move to example
    def doc_symbols(self):
        symbol_id_list = self.make_symbol_id_list()
        debug(symbol_id_list)

        for symbol_id in symbol_id_list:
            self.make_symbol_instance(symbol_id, self.svg.get_current_layer())

    def this_works(self):
        self.parse_test_data()
        #self.render_vpc()
        self.delete_all()
        self.rect()
        self.remote_json_test()
        self.shape_test()

    def import_defs_from_external_file_in_document(self):

        symbol_group = "AWS-Group-light.svg"
        inkhome = str(Path.home()) + "/.config/inkscape"
        svg_file_path = f"{inkhome}/symbols/aws-architect/{symbol_group}"

        try:
            # Load the external SVG file using inkex
            external_svg = inkex.load_svg(svg_file_path)

            if external_svg:
                debug(f"Successfully loaded SVG from {svg_file_path}")

                # Find the defs section in the external SVG
                external_defs = external_svg.getroot().find('{http://www.w3.org/2000/svg}defs')

                if external_defs is not None:
                    # Find all symbol elements in the external defs
                    external_symbols = external_defs.findall('{http://www.w3.org/2000/svg}symbol')

                    if external_symbols:
                        debug(f"Found {len(external_symbols)} symbols in external SVG")

                        # Get or create the defs section in the current document
                        if self.svg.defs is None:
                            self.svg.defs = self.svg.getroot().add(inkex.elements._defs.Defs())

                        # Copy each symbol to the current document's defs
                        for symbol in external_symbols:
                            # Create a copy of the symbol
                            symbol_copy = symbol.copy()

                            # Check if a symbol with the same ID already exists
                            symbol_id = symbol.get('id')
                            symbol_dest_id = f"{symbol_group}:{symbol_id}"
                            symbol_copy.set('id',symbol_dest_id)
                            symbol_copy_id = symbol_copy.get("id")
                            existing_symbols = self.svg.defs.findall(f".//*[@id='{symbol_dest_id}']")

                            if not existing_symbols:
                                # Add the symbol to the current document's defs
                                self.svg.defs.append(symbol_copy)
                                debug(f"Imported symbol: {symbol_id} > {symbol_copy_id}")
                            else:
                                debug(f"Symbol {symbol_id} already exists in document, skipping")

                        debug("Symbol import completed")
                    else:
                        debug("No symbols found in external SVG")
                else:
                    debug("No defs section found in external SVG")
            else:
                debug(f"Failed to load SVG from {svg_file_path}")
        except Exception as e:
            debug(f"Error importing symbols: {str(e)}")

    def effect(self):
        self.import_defs_from_external_file_in_document()
        #self.doc_symbols()
        self.parse_test_data()


if __name__ == '__main__':
    aws_auto_diagram().run()

