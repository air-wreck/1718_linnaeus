# 1718_linnaeus
CSE 2017-18 final project by Nelson, Karena and Eric

### introduction
Biology is the world around us. This is therefore a very powerful tool for the
world around us.

### repository
This repository is organized into a few different directories. The root
directory contains all of the `*.html` pages. These pages reference files in
the `/img` and `/css` directories for the appropriate resources. `/pedigree`
constains all of the Python scripts for drawing and solving pedigrees, and
`/punnett` contains all of the scripts for Punnett Squares. These scripts will
eventually be integrated into the website for functionality. Overall, it looks
like this:

```
.
├── README.md
├── *.html
├── css
│   └── *.css
├── img
│   ├── illustrator
│   │   └── *.ai
│   └── png
│       └── *.png
├── pedigree
│   └── *.py
├── punnett
│   └── *.py
```

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
