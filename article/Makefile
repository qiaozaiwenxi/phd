all: esl
	echo "done"


esl: soa_esl.tex
	pdflatex -halt-on-error soa_esl.tex
	bibtex soa_esl.aux
	pdflatex -halt-on-error soa_esl.tex
	pdflatex -halt-on-error soa_esl.tex

clean:
	rm -f soa_esl.pdf
	rm -f *.idx *.aux *.log *.nav *.out *.snm *.toc *.bbl *.fdb_latexmk *.fls
