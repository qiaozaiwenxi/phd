all: labo
#	labo
#	correction
	echo "done"


labo: *.tex
	pdflatex -shell-escape -jobname="soa" soa.tex
	bibtex soa
	makeglossaries soa
	pdflatex -shell-escape -jobname="soa" soa.tex
	pdflatex -shell-escape -jobname="soa" soa.tex

	pdflatex -shell-escape -jobname="soa-3D" soa-3D.tex
	bibtex soa-3D
	# makeglossaries soa-3D
	pdflatex -shell-escape -jobname="soa-3D" soa-3D.tex
	pdflatex -shell-escape -jobname="soa-3D" soa-3D.tex


clean:
	rm -f soa.pdf soa-3D.pdf
	rm -f *.idx *.aux *.log *.nav *.out *.snm *.toc *.bbl *.glo *.glg *.ist *.fls *.fdb_latexmk *.blg *.gls
