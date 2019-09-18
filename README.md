# Presentation template with Pandoc and reveal.js

Basic structure to create simple and clean HTML presentations using pandoc and reveal.js. Reveal.js and some plugins (<https://github.com/hakimel/reveal.js/wiki/Plugins,-Tools-and-Hardware>) are added as submodules, so clone this repository as:

```bash
git clone --recursive https://github.com/vitay/PandocPresentation.git
```

or call `git submodule update --init --recursive` after cloning.

## Usage

This package provides the basic files to generate a HTML5 + reveal.js presentation from Markdown code using `pandoc`. `pandoc` of course needs to be installed. 

To generate the html file:

```
make
```

The resulting HTML file has to be opened in a recent and decent browser (i.e. everything except IE).

## Shortcuts

* `F`: go fullscreen.
* `S`: open presenter's view.
* `V`: go black (pause).
* `M`: opens the menu to select slides.
* `C`: change the cursor to a pen.
* `B`: opens a chalkboard.
* `CAPSLOCK`: change the cursor to a laser pointer.