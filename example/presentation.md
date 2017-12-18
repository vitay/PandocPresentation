---
title: Using Pandoc for academical presentations
author: Julien Vitay
date: December 2017
---

# Usage

* This package only prepares the basic files to generate a HTML5 + reveal.js presentation from Markdown code using `pandoc`.

* `pandoc` of course needs to be installed.

* To clone the `reveal.js` library:

```
make reveal
```

* To generate the html file:

```
make
```

* The `Makefile` can be modified if you reuse the library/templates between different presentations.

* The slides can be exported to pdf by opening them in Chrome (only), adding `?print-pdf` to the address and printing to file. Ex:

```
file:///home/user/presentationtemplatepandoc/presentation.html?print-pdf#/usage
```

* Make sure to copy pdf.css into the reveal.js folder at `reveal.js/css/print`.

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

* Rest of the syntax on [Pandoc's Markown](https://pandoc.org/)...

[rightcol]

```
* **Bold**, *Italic* or `Literal`

* [Links](http://www.example.com) 

* Lists `*`, a `.` or a `-`

* Enumerations  `1.`, `2.`, etc.

* Sub-lists or sub-enumerations:

    1. Item 1
    2. Item 2
    3. Item 3  
```
```
* Equations in LaTeX format:

$$
\tau \cdot \frac{d r(t)}{dt} + r(t) = 
   \sum_\text{exc} w_i \cdot r_i(t) + B
$$

* Rest of the syntax on 
  [Pandoc's Markown](https://pandoc.org/)
```

# Images

![**Figure 1**: A nice image](pixies.jpg){width=50%}

```
![**Figure 1**: A nice image](pixies.jpg){width=50%}
```

* A figure is basically a link preceded by `!`.

* The width is controlled in percentages only.


# Two columns

[leftcol]

* The main limitation of the md $\rightarrow$ html conversion is that the slides have only one column.

* The script `columns.py` allows to define two simple columns by surrounding each content with:

```
[leftcol]
...
[rightcol]
...
[endcol]
```

* You can control the width of the left column by defining it in percents:

```
[leftcol 40]
```

[rightcol]

* The right column fills the rest.

* You will need to install the Python package `pandocfilters`.

* Images scale to the column:

![](pixies.jpg)

[endcol]

# HTML5 and videos

[leftcol]

* You can use HTML code directly, it will be simply escaped by pandoc.

* Videos (in webm, ogv, mp4) can be inserted using the HTML5 `<video>` tag:

```html
<video width="100%" controls>
<source src="cover.mp4" type="video/mp4">
</video>
```

[rightcol 45]

<video width="100%" controls>
<source src="cover.mp4" type="video/mp4">
</video>

[endcol]

# Highlighted code

* Code in many languages can be highlighted using `highlight.js`.

* The provided css uses the Inconsolata fixed font, feel free to change it.

[leftcol]

* Code:

```
    ```python
    if __name__ == '__main__':
        for i in range(20)
            if i > 10:
                print(i)
    ```
```

* Result:

```python
if __name__ == '__main__':
    for i in range(20)
        if i > 10:
            print(i)
```


[rightcol]

* Code:


```
    ```cpp
    int main(){
        for(int i=0; i<20; i++){
            if(i>10)
                printf("%i", i)
        }
    }
    ```
```

* Result:

```cpp
int main(){
    for(int i=0; i<20; i++){
        if(i>10)
            printf("%i", i)
    }
}
```


[endcol]

# Citations

* There is not much control possible over the font size.

* For citations inside a slide, you can use the `citation` command and it will be printed using a smaller font in a left-aligned block.

```
[citation Source: Einstein, a. (1905). Zur Elektrodynamik bewegter Körper. Annalen der Physik (ser. 4), 17, 891–921]
``` 

[citation Source: Einstein, a. (1905). Zur Elektrodynamik bewegter Körper. Annalen der Physik (ser. 4), 17, 891–921]
