#!/usr/bin/sh

# setup the repository for web hosting
# meant for Unix systems
# if this is run in the web server, it might need to be run as superuser

# create a dummy image buffer and set the permissions
touch cgi-bin/colortable.png
chmod 777 cgi-bin/colortable.png  # probably not the safest way to do it

# set up hard links for Python to compile correct modules
ln punnett/allele.py cgi-bin/allele.py
ln punnett/colortable.py cgi-bin/colortable.py
