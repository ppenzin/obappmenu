try:
  from xml.etree import cElementTree as etree
except ImportError:
  from xml.etree import ElementTree as etree

def obAppMenu(data):
  # Root menu element
  menu = etree.Element('openbox_pipe_menu')
  # App categories
  categories = {}
  
  # Compose the menu
  for item in data:
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
