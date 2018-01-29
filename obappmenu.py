""" Produce an openbox pipe menu from a list of items

The goal is to get a simple (two-level menu) that would agreggate available applications by user-defined categorie.

The format for an item is as follows:
    'name': display name (optional)
    'command': command to execute (will be displayed if no name is given)
    'category': first-level menu to add this item to

TODO:
    - Aggregate menu from two locations (system-wide and user)
    - Switch input to Yaml or use a better format
"""

try:
  from xml.etree import cElementTree as etree
except ImportError:
  from xml.etree import ElementTree as etree

class OpenBoxAppMenu:
  def __init__(self):
    self.menuItems = []
  
  def add(self, data):
    """ Add contents of items array to the internal list"""
    self.menuItems += data
  
  def flush(self):
    """ Clear accumulated data """
    self.menuItems = []

  def render(self):
    """ Produce XML for openbox pipe menu based on the items"""
    # Root menu element
    menu = etree.Element('openbox_pipe_menu')
    # App categories
    categories = {}
    
    # Compose the menu
    for item in self.menuItems:
      cat = item['category']
      if (not cat in categories):
        menu_category = etree.SubElement(menu, 'menu', id=cat, label=cat)
        categories[cat] = menu_category
      # Name is optional
      if ('name' in item):
        menu_label = item['name']
      else:
        menu_label = item['command']
      menu_item = etree.SubElement(categories[cat], 'item', label=menu_label)
      action = etree.SubElement(menu_item, 'action', name='execute')
      etree.SubElement(action, 'command').text = item['command']
      
    print etree.tostring(menu)

obAppMenu = OpenBoxAppMenu()
