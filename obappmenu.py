""" Produce an openbox pipe menu from a list of items

The goal is to get a simple (two-level menu) that would agreggate available applications by user-defined categorie.

Items are stored as a dictionary with 'leaf' entries treated as executable
commands.

TODO:
    - Aggregate menu from two locations (system-wide and user)
    - Consider switching input to Yaml or JSON
"""

try:
  from xml.etree import cElementTree as etree
except ImportError:
  from xml.etree import ElementTree as etree

def walk(node, parent):
  """ Recursively produce XML for nested dictionary"""
  for name, item in node.iteritems():
    if type(item) is dict:
      cat = etree.SubElement(parent, 'menu', id=name, label=name)
      walk (item, cat)
    else:
      menu_item = etree.SubElement(parent, 'item', label=name)
      action = etree.SubElement(menu_item, 'action', name='execute')
      etree.SubElement(action, 'command').text = item

class OpenBoxAppMenu:
  def __init__(self):
    self.menuItems = {}
  
  def add(self, data):
    """ Add contents of items array to the internal list"""
    self.menuItems.update(data)
  
  def flush(self):
    """ Clear accumulated data """
    self.menuItems = {}

  def render(self):
    """ Produce XML for openbox pipe menu based on the items"""
    menu = etree.Element('openbox_pipe_menu')
    
    walk(self.menuItems, menu)
      
    print etree.tostring(menu)

obAppMenu = OpenBoxAppMenu()
