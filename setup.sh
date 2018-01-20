#!/bin/bash

# setup the repository for web hosting, meant for Unix systems
# if this is run in the document root, it might need to be run as superuser
# you also might need to mark it as executable first:
#
# sudo chmod +x setup.sh
# sudo ./setup.sh

# create a dummy image buffer and set the permissions
touch cgi-bin/colortable.png
chmod 777 cgi-bin/colortable.png  # probably not the safest way to do it

# copy the modules that Python needs to compile, since the unprivileged apache
# user can't compile them from hard links
touch cgi-bin/tmp.py
rm cgi-bin/*.py
cp punnett/allele.py cgi-bin/allele.py
cp punnett/colortable.py cgi-bin/colortable.py
