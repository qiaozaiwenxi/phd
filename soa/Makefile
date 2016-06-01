all: labo
#	labo
#	correction
	echo "done"


labo: *.tex
	#cd Figures; ./crop.sh;cd ..
	#cp ~/Documents/SIES2013add.bib .
	pdflatex -shell-escape -jobname="soa" soa.tex
	bibtex soa
	makeglossaries soa
	#bibtex SIES_2013_YAllard.aux
	#pdflatex labo_diodes_corr.tex
	pdflatex -shell-escape -jobname="soa" soa.tex
	pdflatex -shell-escape -jobname="soa" soa.tex


clean:
	rm -f soa.pdf
	rm -f *.idx *.aux *.log *.nav *.out *.snm *.toc
