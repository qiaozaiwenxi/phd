all: main
	echo "done"


main: *.tex
	pdflatex -shell-escape -jobname="rar" rar.tex
	bibtex rar
	makeglossaries rar
	pdflatex -shell-escape -jobname="rar" rar.tex
	pdflatex -shell-escape -jobname="rar" rar.tex
	gs -sOutputFile=rar-grayscale.pdf -sDEVICE=pdfwrite -sColorConversionStrategy=Gray -dProcessColorModel=/DeviceGray -dCompatibilityLevel=1.4 -dNOPAUSE -dBATCH rar.pdf


clean:
	rm -f rar.pdf
	rm -f *.idx *.aux *.log *.nav *.out *.snm *.toc
