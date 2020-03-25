# Presentation template with Pandoc and reveal.js

Basic structure to create simple HTML presentations using Pandoc's markdown and reveal.js. Reveal.js and some plugins (<https://github.com/hakimel/reveal.js/wiki/Plugins,-Tools-and-Hardware>) are added as submodules, so clone this repository as:

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

* `f`: goes fullscreen.
* `e`: switches to printing mode (`?print-pdf` in the location bar). 
* `s`: opens presenter's view.
* `v`: goes black (pause).
* `m`: opens the menu to select slides.
* `c`: changes the cursor to a pen.
* `b`: opens a chalkboard.
* `CAPSLOCK`: changes the cursor to a laser pointer.

## Pandoc's markdown

Refer to <https://pandoc.org/MANUAL.html#pandocs-markdown> for most of the syntax.

The YAML header should look like:

```yaml
---
title: Title of the presentation
subtitle: Subtitle
author: Author name
date: Date or Institution

logo: img/tuc.svg
logo-width: 35%
---
```

Headers with level 1 (`#`) or 2 (`##`) create new slides, as well as the horizontal ruler (`---`).

Recent versions of `pandoc` allow two columns slides:

```markdown
::: {.columns}
::: {.column width="50%"}

* Column 1

:::
::: {.column width="50%"}

* Column 2

:::
:::
``` 

For backward compatibility, the script `assets/columns.py` (you will have to install `pandoc-filters`) allows a simpler variant:

```markdown
[leftcol 50]

* Column 1

[rightcol 50]

* Column 2

[endcol]
```

For credits and citation, the following `<div>` with a font size at 50% is available:

```
[citation Credits: Julien Vitay <julien-vitay.net>]