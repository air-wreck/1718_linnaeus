# 1718_linnaeus
CSE 2017-18 final project by Nelson, Karena and Eric

### introduction
Biology is the world around us. This is therefore a very powerful tool for the
world around us. Try it [here](http://54.191.167.183/1718_linnaeus/home.html).

### getting started
If you just want to use the service, you can access the website from the link
above. If you want to try and tweak the code for yourself, you will need to get
more involved. Obviously, you first need to clone this repository over your
favorite protocol.

If you just want to run some of the example scripts on your computer, you may
need to write `no-agg` in the `punnett/ct_config` file that the setup script
will automatically generate. If you are hosting this on a server, this step is not needed, but you will need to read on.

If you want to set up the server yourself, you will need to first install the
dependencies listed at the bottom of this guide. Then, you need to set up your
Apache server correctly. Edit your `httpd.conf` file with the lines:

```
<Directory <ROOT>/1718_linnaeus/cgi-bin>
  Options ExecCGI
  SetHandler cgi-script
</Directory>
<Directory <ROOT>/1718_linnaeus>
  Options +ExecCGI
  AddHandler cgi-script .py
</Directory>
```

where `<ROOT>` stands in for the document root of your server. These changes
will take effect after you restart Apache.

Additionally, you will need to load the CGI module to run the scripts. This
will vary according to your system, but it will generally take the form:

```
LoadModule cgi_module <...>
```

The rest of the setup can be handled automatically by the `setup.sh` script,
which you may have to run with `sudo`. There is one important exception: due
to issues with the Apache user's PATH, the absolute path to the  `dot` binary
on your system is required. Paste this into the `cgi-bin/dot_path` once you've
run `setup.sh`, or you'll get a nasty bug.

### repository
This repository is organized into a few different directories. The root
directory contains all of the `*.html` pages. These pages reference files in
the `/img`, `/css`, and `/cgi-bin` directories for the appropriate resources.
`/pedigree` contains all of the Python scripts for drawing and solving
pedigrees, and `/punnett` contains all of the scripts for Punnett Squares.

### dependencies
This software requires the Python packages `matplotlib`, `numpy`, and
`graphviz`. `numpy` is already a dependency of `matplotlib`, so you likely do
not need to install it separately. For `graphviz`, you will need to install
both the actual program and the Python bindings. You can find installation
instructions for your specific system here:

* [matplotlib](https://matplotlib.org/)
* [numpy](http://www.numpy.org/)
* [graphviz Python](http://graphviz.readthedocs.io/en/stable/manual.html)
* [graphviz](https://graphviz.gitlab.io/)

Additionally, the server is currently hosted as an Apache web server, so you
will need Apache if you want to mirror this.
