# PresentationTemplatePandoc

Basic structure to create simple and clean HTML presentations using pandoc and reveal.js. 

## Usage

* This package only prepares the basic files to generate a HTML5 + reveal.js presentation from Markdown code using `pandoc`.

* `pandoc` of course needs to be installed.

* To clone the `reveal.js` library:

~~~~
make reveal
~~~~

* To generate the html file:

~~~~
make
~~~~

* The resulting HTML file has to be opened in a recent and decent browser (i.e. everything except IE).

* The `Makefile` can be modified if you reuse the library/templates between different presentations.

* The slides can be exported to pdf by opening them in Chrome (only), adding `?print-pdf` to the address and printing to file. Ex:

~~~~
file:///home/user/presentationtemplatepandoc/presentation.html?print-pdf#/usage
~~~~