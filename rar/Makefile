all: main
	echo "done"


main: *.tex
	pdflatex -shell-escape -jobname="rar" rar.tex
	bibtex rar
	makeglossaries rar
	pdflatex -shell-escape -jobname="rar" rar.tex
	pdflatex -shell-escape -jobname="rar" rar.tex


clean:
	rm -f rar.pdf
	rm -f *.idx *.aux *.log *.nav *.out *.snm *.toc
