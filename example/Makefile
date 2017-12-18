file=presentation.md

all: html

html: $(file)
	pandoc -s -t revealjs --css ./simple.css --template ./template.html \
	--variable revealjs-url=../reveal.js --filter ./columns.py \
	--variable theme=black \
	--variable transition=none \
	--variable center=true \
	--variable progress=false \
	--variable controls=false \
	--variable slideNumber=true \
	--mathjax \
	$(file) -o $(patsubst %.md,%.html,$(file))

reveal:
	git clone https://github.com/hakimel/reveal.js.git
	cp pdf.css reveal.js/css/print/
