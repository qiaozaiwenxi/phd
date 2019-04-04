all: labo
	echo "done"


labo: *.tex
	# pdflatex -shell-escape -jobname="glossary_main" glossary_main.tex
	pdflatex -shell-escape -jobname="full" full.tex
	bibtex full
	makeglossaries full
	# pdflatex -shell-escape -jobname="glossary_main" glossary_main.tex
	pdflatex -shell-escape -jobname="full" full.tex
	pdflatex -shell-escape -jobname="full" full.tex


clean:
	rm -f glossary_main.pdf full.pdf
	rm -f *.idx *.aux *.log *.nav *.out *.snm *.toc *.glo *.gls *.glg *.ist *.xdy *.acn
