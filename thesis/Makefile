all: labo
#	labo
#	correction
	echo "done"


labo: *.tex
	#cd Figures; ./crop.sh;cd ..
	#cp ~/Documents/SIES2013add.bib .
	pdflatex -shell-escape -jobname="glossary_main" glossary_main.tex
	makeglossaries glossary_main
	#bibtex SIES_2013_YAllard.aux
	#pdflatex labo_diodes_corr.tex
	pdflatex -shell-escape -jobname="glossary_main" glossary_main.tex


clean:
	rm -f glossary_main.pdf
	rm -f *.idx *.aux *.log *.nav *.out *.snm *.toc
