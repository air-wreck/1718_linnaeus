#!/bin/bash

# setup the repository for web hosting
# meant for Unix systems
# if this is run in the web server, it might need to be run as superuser
# you also might need to mark it as executable first:
# 
# sudo chmod +x setup.sh
# sudo ./setup.sh

# create a dummy image buffer and set the permissions
touch cgi-bin/colortable.png
chmod 777 cgi-bin/colortable.png  # probably not the safest way to do it

# set up hard links for Python to compile correct modules
ln punnett/allele.py cgi-bin/allele.py
ln punnett/colortable.py cgi-bin/colortable.py
