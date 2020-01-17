name = budget
figures :=

$(name).pdf: $(name).md header.tex $(figures)
	pandoc -s $(name).md -o $(name).pdf

clean: cleanpdf
	rm -rf tmp

cleanpdf:
	rm -f $(name).pdf
