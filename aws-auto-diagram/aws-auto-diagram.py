import inkex
from inkex.elements import Rectangle, Group, PathElement, Line

class aws_auto_diagram(inkex.EffectExtension):

    def effect(self):
        print("jallo")
        #inkex.errormsg("Hello World Extension Started!")  # Debug message
        # Create a rectangle
        rect = Rectangle.new(10, 10, 100, 100)  # (x, y, width, height)
        rect.style = {"fill": "red", "stroke": "black"}
        # Add to the SVG document
        self.svg.append(rect)
        #inkex.errormsg("Rectangle added to the SVG!")  # Debug message
        print("jallo")
        self.blabl()

    def blabl(self):
        rect = Rectangle.new(100, 100, 100, 100)  # (x, y, width, height)
        rect.style = {"fill": "blue", "stroke": "yellow"}
        # Add to the SVG document
        self.svg.append(rect)

    def effect2(self):

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
