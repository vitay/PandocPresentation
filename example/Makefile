file=presentation.md

all: html

html: $(file)
	pandoc -s -t revealjs --css simple.css --template template.html --filter columns.py --variable revealjs-url=./reveal.js --mathjax $(file) -o $(patsubst %.md,%.html,$(file))

reveal:
	git clone https://github.com/hakimel/reveal.js.git
