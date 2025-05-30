import inkex
from inkex.elements import TextElement, Rectangle, Group, PathElement, Line, Symbol
from inkex import Use, Transform
from ica_utils.icalog import debug

COLOR_GREEN="#7aa116"
COLOR_PURPLE="#8c4fff"
COLOR_BLUE="#00a4a6"

def aws_rect(inkdoc, xy, wh, color, name, symid):
    rect = Rectangle.new(xy[0], xy[1], wh[0], wh[1])
    rect.style = {"fill": "none", "stroke-width": 0.5, "stroke": color}
    inkdoc.svg.append(rect)

    icon_el = inkdoc.make_symbol_instance(symid, inkdoc.svg.get_current_layer())
    tr = Transform(f'translate({xy[0]}, {xy[1]}) scale(0.275)')
    icon_el.transform = tr

    """Add a text label at the given location"""
    elem = TextElement(x=str(xy[0]+15), y=str(xy[1]+8))
    elem.text = str(name)
    elem.style = {
        'font-size': inkdoc.svg.unittouu('18pt'),
        'fill-opacity': '1.0',
        'stroke': 'none',
        'font-weight': 'normal',
        'font-style': 'normal' }

    inkdoc.svg.append(elem)

def render_vpc(inkdoc):
    aws_rect(inkdoc,
             [10,10], [180,150], COLOR_PURPLE, "vpc",
             "AWS-Group-light.svg:virtual-private-network-vpc.svg")

def render_subnet(inkdoc, props):
    debug("")
    debug("")
    debug(props['data']['name'])
    name = props['data']['name']

    if "private" not in name:

        aws_rect(inkdoc, [20,40], [160, 50], COLOR_GREEN, name,
                 "AWS-Group-light.svg:public-subnet.svg")

    else:
        aws_rect(inkdoc, [20,100], [160, 50], COLOR_BLUE, name,
                 "AWS-Group-light.svg:private-subnet.svg")
