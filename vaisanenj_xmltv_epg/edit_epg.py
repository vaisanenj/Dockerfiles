import xml.etree.ElementTree as ET
import re
import time

tree = ET.parse('/output/guide.xml')
root = tree.getroot()

def find_and_extract_numbers(content, regex):
    output = re.findall(regex, content, re.IGNORECASE)
    if output:
        if(len(output[0]) == 2):
            output = output[0][0]
        else:
            output = output[0]

        res = [int(i) for i in output.split() if i.isdigit()]
        return res[0]

def remove_tz(val):
    i = val.index(' +')
    return val[0:i]

def add_new_tag(tag, value, att={}):
    new_field = ET.Element(tag)
    new_field.text = value
    new_field.attrib = att
    neighbor.append(new_field)

for neighbor in root.findall('programme'):
    title_elem = neighbor.find("title")
    desc = neighbor.find("desc")
    cat = neighbor.find("category")

    old_title = title_elem.text
    title_elem.text = re.split("^[0-2][0-9]\.[0-9]{2}.", title_elem.text)[1]
    title_elem.text = re.split("IMDb(.*)", title_elem.text)[0]
    title_elem.text = re.split("J[0-9]$", title_elem.text)[0]
    title_elem.text = re.split("UUSIN.JAKSO$", title_elem.text)[0]
    title_elem.text = re.split("UUSI.KAUSI$", title_elem.text)[0]
    if old_title != title_elem.text:
        print("{} -> {}".format(old_title, title_elem.text))
    if desc is None:
        continue

    season = find_and_extract_numbers(desc.text, "((season|kausi)[ ][0-9]{1,4})")
    episode = find_and_extract_numbers(desc.text, "((episode|jakso|osa|,)[ ][0-9]{1,4})")

    #Lisataan kausi ja jakso tiedot jos löytyy
    if season and episode:
      add_new_tag("episode-num", "S{}E{}".format(str(season).zfill(2), str(episode).zfill(2)), {"system": "SxxExx"})


with open('/output/guide_edited.xml', 'wb') as f:
    tree.write(f)
