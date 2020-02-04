name = optional_attachments
figures :=

$(name).pdf: $(name).md header.tex $(figures)
	pandoc --variable fontsize=12pt -s $(name).md -o $(name).pdf

clean: cleanpdf
	rm -rf tmp

cleanpdf:
	rm -f $(name).pdf
