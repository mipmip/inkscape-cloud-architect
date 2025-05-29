import inkex
from inkex.elements import Rectangle, Group, PathElement, Line
import json
import os

import xml.etree.ElementTree as etree

def load_svg_file(file_path):

    try:
        # Check if file exists
        if not os.path.isfile(file_path):
            inkex.errormsg(f"File not found: {file_path}")
            return None

        data = etree.parse(file_path)
        return data

#        with open(file_path, 'r') as file:
#            data = inkex.elements._parser.load_svg(file)
#            return data

    except json.JSONDecodeError as e:
        inkex.errormsg(f"Error parsing JSON file: {e}")
        return None
    except Exception as e:
        inkex.errormsg(f"Error loading file: {e}")
        return None


def load_json_file(file_path):

    try:
        # Check if file exists
        if not os.path.isfile(file_path):
            inkex.errormsg(f"File not found: {file_path}")
            return None

        with open(file_path, 'r') as file:
            data = json.load(file)
            return data

    except json.JSONDecodeError as e:
        inkex.errormsg(f"Error parsing JSON file: {e}")
        return None
    except Exception as e:
        inkex.errormsg(f"Error loading file: {e}")
        return None

