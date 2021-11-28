input_file=presentation.md
output_file=index.html

all: html

html: $(input_file)
	pandoc -s -t revealjs \
    --template=./assets/template.html \
    --css=./assets/simple.css \
    --variable revealjs-url=./assets/reveal.js \
    --filter ./assets/columns.py \
    --variable theme=white \
    --variable transition=none \
    --variable center=true \
    --variable progress=true \
    --variable controls=false \
    --variable slideNumber=true \
    --mathjax \
    $(input_file) -o $(output_file)

reveal:
	git clone https://github.com/hakimel/reveal.js.git assets/reveal.js
