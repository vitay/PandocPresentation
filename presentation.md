% Title of the presentation
% Author name
% Date

# Usage

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

* The `Makefile` can be modified if you reuse the library/templates between different presentations.

* The slides can be exported to pdf by opening them in Chrome (only), adding `?print-pdf` to the address and printing to file. Ex:

~~~~
file:///home/user/presentationtemplatepandoc/presentation.html?print-pdf#/usage
~~~~

# Basic markup

[leftcol]

* You can write in **Bold**, *Italic* or `Literal`

* [Links](http://www.example.com) have two parts, the text and the target.

* Lists can start with a `*`, a `.` or a `-`.

* Enumerations start with `1.`, `2.`, etc.

* Sub-lists or sub-enumerations are possible by indenting:
    1. Item 1
    2. Item 2
    3. Item 3  

* Equations in LaTeX format:

$$
\tau \cdot \frac{d r(t)}{dt} + r(t) = 
\sum_\text{exc} w_i \cdot r_i(t) + B
$$

* Rest of the syntax on [Pandoc's Markown]()...

[rightcol]

~~~~{.md}

* **Bold**, *Italic* or `Literal`

* [Links](http://www.example.com) 

* Lists `*`, a `.` or a `-`

* Enumerations  `1.`, `2.`, etc.

* Sub-lists or sub-enumerations:
    1. Item 1
    2. Item 2
    3. Item 3  

* Equations in LaTeX format:

$$\tau \cdot \frac{d r(t)}{dt} + r(t) = 
\sum_\text{exc} w_i \cdot r_i(t) + B$$

* [Pandoc's Markown]()
~~~~

# Images {.image50}

![**Figure 1**: A nice figure](pixies.jpg)

~~~~{.markdown}
# Images {.image50}

![**Figure 1**: A nice figure](pixies.jpg)
~~~~

* A figure is basically a link preceded by `!`

* Setting the slide class to `{.image50}` defines the width of the image in the slide (available from 5% to 95% in steps of 5%)

# Two columns

[leftcol]

* The main limitation of the md $\rightarrow$ html conversion is that the slides have only one column.

* The script `columns.py` allows to define two simple columns by surrounding each content with:

~~~~
[leftcol]
...
[rightcol]
...
[endcol]
~~~~

* You can control the width of the left column by defining it in percents:

~~~~
[leftcol 40]
~~~~

[rightcol]

* The right column fills the rest.

* You will need to install the python bindings to Pandoc.

* Images scale to the column:

![](pixies.jpg)

[endcol]

# HTML5 and videos

[leftcol]

* You can use HTML code directly, it will be simply escaped by pandoc.

* Videos (in webm, ogv, mp4) can be inserted using the HTML5 `<video>` tag:

~~~~{.html}
<video style="text-align:center; 
float:center" width="100%" controls>
<source src="cover.mp4" type="video/mp4">
</video> 
~~~~

[rightcol]

<br>
<video style="text-align:center; float:center" width="100%" controls>
<source src="cover.mp4" type="video/mp4">
</video> 

[endcol]

# Highlighted code

* Code can be highlighted using `highlight.js`:

~~~~ {.python}
import numpy as np

A = np.ones((10, 10))

B = A + 1.0
~~~~

~~~~ 
    ~~~~ {.python}
    import numpy as np

    A = np.ones((10, 10))

    B = A + 1.0
    ~~~~
~~~~
