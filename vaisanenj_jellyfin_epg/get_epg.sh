#!/bin/bash

wget https://epghub.xyz/epg/EPG-${COUNTRY}.xml -O /output/EPG-${COUNTRY}.xml
python3 edit_xml.py /output/EPG-${COUNTRY}.xml /output/EPG-${COUNTRY}.xml