import inkex
from inkex.elements import Rectangle, Group, PathElement, Line, Symbol
from inkex import Use, Transform
import json
import os
import jsonloader

class aws_auto_diagram(inkex.EffectExtension):

    def make_symbol_id_list(self):

        # Get a list of all symbols contained in defs
        symbolsvg = jsonloader.load_svg_file("/home/pim/.config/inkscape/symbols/aws-architect/AWS-Group-light.svg")
        #inkex.errormsg(self.svg)
        inkex.errormsg(symbolsvg.svg)

        symbol_list = self.svg.defs.xpath('svg:symbol')
        if len(symbol_list) < 1:
            inkex.errormsg('No Symbols Found In Document')
            sys.exit()
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


    def effect2(self):

        config_data = jsonloader.load_json_file('/home/pim/cInkscape/inkscape-cloud-architect/aws-auto-diagram/test-data.json')
        if config_data:

            vpcs = list(filter(lambda node: node['data']['type'] == 'vpc', config_data))
            #inkex.errormsg(vpcs)

            for vpc in vpcs:
                self.render_vpc();


        symbol_id_list = self.make_symbol_id_list()

        for symbol_id in symbol_id_list:
            self.make_symbol_instance(symbol_id, self.svg.get_current_layer())


    def render_vpc(self):

        rect = Rectangle.new(10, 10, 300, 200)  # (x, y, width, height)
        rect.style = {"fill": "none", "stroke-width": 0.5, "stroke": "purple"}


        # Add to the SVG document
        self.svg.append(rect)



    def blabl(self):
        rect = Rectangle.new(100, 100, 100, 100)  # (x, y, width, height)
        rect.style = {"fill": "blue", "stroke": "yellow"}
        # Add to the SVG document
        self.svg.append(rect)

        symbol = Symbol.new("virtual-private-network-vpc.svg")

    def effect(self):

        #create layer
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
        #delete all elements
        #for node in self.svg.xpath('//svg:path'):
            #node.delete()

if __name__ == '__main__':
    aws_auto_diagram().run()

