#!/bin/bash

tv_grab_fi --days 7 --output /output/guide.xml --config-file /EPG/tv_grab.conf
python3 edit_epg.py /output/guide.xml