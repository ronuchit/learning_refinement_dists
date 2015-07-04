default:
	pdflatex root
	pdflatex root

clean:
	rm -f root.log root.aux root.out root.fls root.fdb_latexmk
