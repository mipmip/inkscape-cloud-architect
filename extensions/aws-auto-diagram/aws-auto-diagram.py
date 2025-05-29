import inkex
from inkex.elements import Rectangle, Group, PathElement, Line, Symbol
from inkex import Use, Transform
import json
import os
import jsonloader
import requests


LOGFILE = True
def debug(var):
    if LOGFILE:
        with open("/tmp/aws-auto-diagram.log", "a") as text_file:
            text_file.write(str(var))
            text_file.write("\n")
    else:
        inkex.errormsg((var))


class aws_auto_diagram(inkex.EffectExtension):

    def render_vpc(self):
        rect = Rectangle.new(10, 10, 300, 200)  # (x, y, width, height)
        rect.style = {"fill": "none", "stroke-width": 0.5, "stroke": "purple"}
        # Add to the SVG document
        self.svg.append(rect)

    def rect(self):
        rect = Rectangle.new(100, 100, 100, 100)  # (x, y, width, height)
        rect.style = {"fill": "blue", "stroke": "yellow"}
        # Add to the SVG document
        self.svg.append(rect)

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


    def delete_all(self):
        debug("DELETE ALL")
        for node in self.svg.xpath('//svg:path'):
            debug(node)
            node.delete()

    def remote_json_test(self):
        debug("remote_json_test")
        response = requests.get('https://api.restful-api.dev/objects')
        data = response.json()
        debug(data)

    def symbol_test(self):
        debug("symbol test")
        symbol = Symbol.new("virtual-private-network-vpc.svg")
        debug(symbol)


    def make_symbol_id_list(self):

        # Get a list of all symbols contained in defs
        symbolsvg = jsonloader.load_svg_file("/home/pim/.config/inkscape/symbols/aws-architect/AWS-Group-light.svg")
        #debug(symbolsvg)

        symbol_list = self.svg.defs.xpath('svg:symbol')
        if len(symbol_list) < 1:
            debug('No Symbols Found In Document')
            return []
        else:
            symbol_id_list = [x.get_id() for x in symbol_list]
            return symbol_id_list

    def make_symbol_instance(self, symbol_id, parent):
        use_element = Use()
        use_element.set('xlink:href', f'#{symbol_id}')
        parent.append(use_element)

        # Move new element to 0,0
        # Make a negative translate from elements current x, y and apply
        bbox = use_element.bounding_box()
        origin_translate = -Transform().add_translate(bbox.left, bbox.top)
        use_element.transform = use_element.transform @ origin_translate

    def parse_test_data(self):
        config_data = jsonloader.load_json_file('/home/pim/.config/inkscape/extensions/aws-auto-diagram/test-data.json')
        if config_data:

            vpcs = list(filter(lambda node: node['data']['type'] == 'vpc', config_data))
            debug(vpcs)

            for vpc in vpcs:
                self.render_vpc();


        symbol_id_list = self.make_symbol_id_list()
        debug(symbol_id_list)

        for symbol_id in symbol_id_list:
            self.make_symbol_instance(symbol_id, self.svg.get_current_layer())

    def effect(self):
        self.parse_test_data()

#        self.render_vpc()
#        self.delete_all()
#        self.rect()
#        self.remote_json_test()
#        self.symbol_test()
#        self.shape_test()





if __name__ == '__main__':
    aws_auto_diagram().run()

