import xml.etree.ElementTree as ET
import re, sys
import time

tree = ET.parse(sys.argv[1])
root = tree.getroot()

def add_new_tag(tag, value, att={}):
    new_field = ET.Element(tag)
    new_field.text = value
    new_field.attrib = att
    neighbor.append(new_field)


for neighbor in root.findall('programme'):
    episode_elem = neighbor.find("episode-num")

    if episode_elem is None:
        continue

    season = episode_elem.text.split(' ')[0][1:]
    episode = episode_elem.text.split(' ')[1][1:]
    add_new_tag("episode-num", "S{}E{}".format(str(season).zfill(2), str(episode).zfill(2)), {"system": "SxxExx"})


with open(sys.argv[1], 'wb') as f:
    tree.write(f)
