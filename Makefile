default:
	pdflatex root
	bibtex root
	pdflatex root
	pdflatex root

clean:
	rm -f root.log root.aux root.out root.fls root.fdb_latexmk root.bbl root.blg
