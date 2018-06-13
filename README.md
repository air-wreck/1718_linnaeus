# 1718_linnaeus
CSE 2017-18 final project by Nelson, Karena and Eric

```
This repository is a clone of the original, which is private and has been
submitted as our final project.
```

### introduction
Biology is the world around us. This is therefore a very powerful tool for the
world around us. Try it
[here](https://air-wreck.github.io/1718_linnaeus/home.html).

### new! april 2018
The code has been rewritten to work entire in-browser, so there is no longer
any need for the Apache server environment or all of the aforementioned
dependencies. All you need is a reasonably recent version of a major browser
and you're set to go. Maybe we'll look to transpiling to ES5 later on.

This project now uses Graphviz through the `viz.js` project, which you can
find [here](http://viz-js.com/). (Yay for asm.js?) However, you don't
need to install it before developing, since this repository is almost entirely
self-contained (except for the icons at the bottom of the home page).
Actually, you don't even need internet access anymore.

### getting started
You can get started by simply visiting the link above. You can look through the
source code in this repository. I guess you can submit a pull request if you
feel so inclined, but I have no clue why you would want to do that.

### this repository
This repository is organized into a few different directories. The root
directory contains all of the `*.html` pages. These pages reference files in
the `/img`, `/css`, and `/js` directories for the appropriate resources. In
addition, `/js` has the additional subdirectory `/js/other`, which stores all
external code (read: dependencies).

`/pedigree` contains all of the Python scripts for drawing and solving
pedigrees, and `/punnett` contains all of the scripts for Punnett Squares. We
are in the process of converting these to Javascript targeting the client-side.

### dependencies
This project relies on the outside dependencies `viz.js` (+ associated worker
script `full.js.opaque`) and `html2canvas`. The necessary Javascript is already
included in this repository under `/js/other`.

All you then need is a reasonably recent version of a major browser. The latest
version of Chrome is recommended.
