#!/bin/bash

# setup the repository for web hosting, meant for Unix systems
# if this is run in the document root, it might need to be run as superuser
# you also might need to mark it as executable first:
#
# sudo chmod +x setup.sh
# sudo ./setup.sh

# mark CGI scripts as executable, in case they weren't
chmod +x cgi-bin/punnett-square
chmod +x cgi-bin/pedigree

# create a dummy image buffer and set the permissions
touch cgi-bin/colortable.png
chmod 777 cgi-bin/colortable.png  # probably not the safest way to do it
touch cgi-bin/ped.dot
chmod 777 cgi-bin/ped.dot
touch cgi-bin/ped.dot.png
chmod 777 cgi-bin/ped.dot.png

# copy the modules that Python needs to compile, since the unprivileged apache
# user can't compile them from hard links
touch cgi-bin/tmp.py
rm cgi-bin/*.py
cp punnett/allele.py cgi-bin/allele.py
cp punnett/colortable.py cgi-bin/colortable.py
cp pedigree/ped_draw.py cgi-bin/ped_draw.py
cp pedigree/ped_solve.py cgi-bin/ped_solve.py

# setup the location of the dot binary
touch cgi-bin/dot_path
chmod +r cgi-bin/dot_path

# this config file exists only so that colortable.py can be used outside the
# production server environment (i.e. load matplotlib with a non-Agg 
# backend)
touch punnett/ct_config
chmod +r punnett/ct_config

# friendly warning to finish setup
echo 'WARNING: make sure you set up cgi-bin/dot_path, or else'
echo 'if you are not on a deployment server, set up punnett/ct_config too'

